from github import Github
# Replace <access_token> with your personal access token
g = Github("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")
for repo in g.get_user().get_repos():
    print(repo.name)
    contents = repo.get_contents("")
    for file in contents:
          print("file : ",file.name)
