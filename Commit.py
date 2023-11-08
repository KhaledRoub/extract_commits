from requests.auth import HTTPBasicAuth
import os
import my_token
import requests
from requests.auth import HTTPBasicAuth
import os

def get_data(github_username, private_url, tries=5):
    for i in range(tries):
        try:
            response = requests.get(url=private_url, auth=HTTPBasicAuth(github_username, os.environ.get("priv_token")))
            if response.status_code in (200, 201):  
                return response.json()
            else: 
                print("Failed to fetch data from GitHub API")
        except Exception as e:
                exit(-1)



def json_to_file(json_content, file_path):

    if type(json_content) == list:
        with open(file_path, "w") as file:
            for term in json_content:
                # json.dump(content['commit']['message'], file)
                json.dump(term['commit'], file)



def main(github_username, private_url):
    json_content = get_data(github_username, private_url)
    json_to_file(json_content, "Output.txt")


if __name__ == "__main__":
    github_username ='KhaledRoub'
    repo_name = "HTML-CSS"
    private_url = f"https://api.github.com/repos/{github_username}/{repo_name}/commits"
    main(github_username, private_url)


