import sys
import subprocess
import argparse
from urllib.parse import urlparse

def is_valid_url(URL):
    parsed = urlparse(URL)
    if (
    parsed.scheme in ("http", "https")
    and parsed.hostname in ("github.com", "gitlab.com", "bitbucket.org")
    and "" not in parsed.path.split("/")[1:-1]
    ):
        return True
    else:
        return False


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    deploy_parser = subparsers.add_parser("deploy")
    deploy_parser.add_argument("--repo", required=True)

    subparsers.add_parser("status")

    args = parser.parse_args()

    if args.command == "deploy":
        if is_valid_url(args.repo):
            print("Deployment request accepted.")
            print("Repository:", args.repo)
        else:
            print("Invalid URL")
            sys.exit(1)

    elif args.command == "status":
        print("Platform status: ready")


if __name__ == "__main__":
    main()
