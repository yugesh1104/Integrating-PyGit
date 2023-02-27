from github import Github
# Replace <access_token> with your personal access token
g = Github("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")
for repo in g.get_user().get_repos():
    print(repo.name)
    contents = repo.get_contents("")
    for file in contents:
          print("file : ",file.name)
          
file = repo.get_contents("integration.py")
file_contents = file.decoded_content.decode("utf-8")
print(file_contents)
