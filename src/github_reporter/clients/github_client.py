import requests


class GithubClient:
    def __init__(self, pat_token: str):
        self.__pat_token = pat_token

    def get_user(self, username):
        url = f'https://api.github.com/users/{username}'
        response = requests.get(
            url, headers={'Authorization': f'token {self.__pat_token}'})
        return response.json()

    def get_repos(self, username):
        url = f'https://api.github.com/users/{username}/repos'
        response = requests.get(
            url, headers={'Authorization': f'token {self.__pat_token}'})
        return response.json()
