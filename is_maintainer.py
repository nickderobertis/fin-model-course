"""
Script to check within Github Actions whether current actor is one of the package maintainers
"""
import os

from conf import REPO_MAINTAINERS

if __name__ == '__main__':
    user = os.environ['GITHUB_PR_USER']
    if user in REPO_MAINTAINERS:
        print(f'Github PR user {user} was in maintainers, will auto merge PR')
        exit(0)
    print(f"Github PR user was {user}, not in maintainers {REPO_MAINTAINERS}, so will not auto merge PR")
    exit(1)
