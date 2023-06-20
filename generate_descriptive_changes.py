import os
from github import Github

#set up your desired variables  or environment
repo_name = os.environ.get('REPO_NAME')
github_token = os.environ.get('GITHUB_TOKEN')

g=Github(github_token)
repo = g.get_repo(repo_name)

release_notes = " "
for commits in repo.get_commits():
    release_notes += commits.commit.message + "\n"

print(release_notes)