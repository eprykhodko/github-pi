from github import Github
import requests

from .utils import is_wheel
from .. import settings

github_client = Github(settings.GITHUB_AUTH_TOKEN)


def get_assets(repo_name):
    releases = github_client.get_repo(repo_name).get_releases()
    response = requests.get(f'https://api.github.com/repos/{repo_name}/releases')
    print(response.headers['Link'], type(response.headers['Link']), len(response.headers['Link']))
    releases = response.json()
    for release in releases:
        for asset in release['assets']:
            if is_wheel(asset):
                yield asset['name'], asset['browser_download_url']
