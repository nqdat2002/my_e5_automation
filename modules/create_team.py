import requests

def create_teams(pat_token, org, project, repo_name):
    url = f"https://dev.azure.com/{org}/{project}/_apis/git/repositories?api-version=6.0"
    headers = {
        "Authorization": f"Basic {pat_token}",
        "Content-Type": "application/json"
    }
    body = {
        "name": repo_name
    }
    response = requests.post(url, headers=headers, json=body)
    print(response.status_code, response.json())
