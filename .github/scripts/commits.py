#!/usr/bin/env python3
"""Write _data/commits.json: the latest five commits of every repository
(and branch) the site shows an "Updated" date or a commit list for,
leaving out commits that change only .github/ (CI, not the port).

Keys are "<owner>/<repo>@<branch>" ("@" alone for the default branch),
as _includes/updated.html and commits.html look them up. Run before
`jekyll build`; GITHUB_TOKEN, when set, raises the API's rate limit.
A repository that cannot be read is left out, and its pages fall back
to a link to its commits.
"""
import glob
import json
import os
import re
import urllib.request

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")


def front_matter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return dict(re.findall(r"^(\w+):\s*(.+?)\s*$", m.group(1), re.M)) if m else {}


def slug(url):
    return url.strip("\"'").removeprefix("https://github.com/")


site_repo = slug(re.search(
    r"^repo:\s*(\S+)", open(os.path.join(ROOT, "_config.yml")).read(), re.M).group(1))
keys = {site_repo + "@"}
branches = {}
for path in glob.glob(os.path.join(ROOT, "_systems", "*.md")):
    fm = front_matter(path)
    branches[os.path.basename(path)[:-3]] = fm.get("branch", "")
    keys.add(site_repo + "@" + fm.get("branch", ""))
for path in glob.glob(os.path.join(ROOT, "_projects", "*", "*.md")):
    fm = front_matter(path)
    if "repo" in fm:
        keys.add(slug(fm["repo"]) + "@" + fm.get("branch", ""))
    else:
        keys.add(site_repo + "@" + branches.get(os.path.basename(os.path.dirname(path)), ""))

headers = {"Accept": "application/vnd.github+json"}
if os.environ.get("GITHUB_TOKEN"):
    headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return json.load(r)


def ci_only(repo, sha):
    files = get(f"https://api.github.com/repos/{repo}/commits/{sha}")["files"]
    return bool(files) and all(f["filename"].startswith(".github/") for f in files)


data = {}
for key in sorted(keys):
    repo, branch = key.split("@")
    url = f"https://api.github.com/repos/{repo}/commits?per_page=20"
    if branch:
        url += "&sha=" + branch
    try:
        commits = []
        for c in get(url):
            if not ci_only(repo, c["sha"]):
                commits.append(c)
            if len(commits) == 5:
                break
    except Exception as e:
        print(f"{key}: {e}")
        continue
    data[key] = [{
        "time": c["commit"]["committer"]["date"],
        "date": c["commit"]["committer"]["date"][:10],
        "message": c["commit"]["message"].split("\n")[0],
        "url": c["html_url"],
    } for c in commits]
    print(f"{key}: {data[key][0]['date'] if data[key] else 'no commits'}")

os.makedirs(os.path.join(ROOT, "_data"), exist_ok=True)
with open(os.path.join(ROOT, "_data", "commits.json"), "w") as f:
    json.dump(data, f, indent=1)
