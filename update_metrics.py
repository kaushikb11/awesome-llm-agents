import argparse
import os
import re
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()


def get_repo_metrics(repo_url):
    match = re.search(r"github\.com/([^/]+)/([^/]+)", repo_url)
    if not match:
        return None

    owner, repo = match.groups()
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    contributors_url = f"{api_url}/contributors"

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_TOKEN}",
    }

    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()

            contributor_count = 0
            page = 1
            while True:
                page_url = f"{contributors_url}?per_page=100&page={page}"
                contributors_response = requests.get(page_url, headers=headers)
                if (
                    contributors_response.status_code != 200
                    or not contributors_response.json()
                ):
                    break
                contributor_count += len(contributors_response.json())
                page += 1

            return {
                "stars": data["stargazers_count"],
                "forks": data["forks_count"],
                "open_issues": data["open_issues_count"],
                "contributors": contributor_count,
                "language": data.get("language", "Unknown"),
                "license": data.get("license", {}).get("spdx_id", "Unknown"),
            }
    except Exception as e:
        print(f"Error fetching metrics for {repo_url}: {str(e)}")

    return None


def format_metrics_badges(metrics):
    return (
        f"{metrics['stars']:,} stars · {metrics['forks']:,} forks · "
        f"{metrics['contributors']:,} contributors · "
        f"{metrics['open_issues']:,} issues · "
        f"{metrics['language']} · {metrics['license']}"
    )


def update_readme_with_metrics(readme_path, args):
    with open(readme_path, "r") as f:
        content = f.read()

    current_time = datetime.now().strftime("%Y-%m-%d")
    pattern = r"Last updated: \d{4}-\d{2}-\d{2}"
    try:
        if not re.search(pattern, content):
            raise Exception(
                "Could not find 'Last updated: YYYY-MM-DD' pattern in the text"
            )
        content = re.sub(pattern, f"Last updated: {current_time}", content)
    except Exception as e:
        raise e

    parts = content.split("## Frameworks")
    if len(parts) < 2:
        raise Exception("Frameworks empty!")

    header = parts[0]
    frameworks_section = parts[1]
    new_frameworks_section = ""

    framework_entries = re.split(r"\n(?=- \[)", frameworks_section)

    for entry in framework_entries:
        match = re.search(
            (
                r"- \[([^\]]+)\]\((https://github\.com/"
                r"[^/]+/[^/)\s]+)\)(.*?)(?=\n\n|\n  -|$)"
            ),
            entry,
            re.DOTALL,
        )
        if match:
            name, url, desc = match.groups()
            metrics = get_repo_metrics(url)

            if metrics:
                first_line = (
                    f"- [{name}]({url}){desc}\n\n  " f"{format_metrics_badges(metrics)}"
                )

                features_start = entry.find("\n  -")
                if features_start != -1:
                    rest_of_entry = entry[features_start:]
                else:
                    rest_of_entry = ""

                entry = f"{first_line}\n\n  {rest_of_entry.strip()}\n\n\n"

        new_frameworks_section += entry

    if args.url and args.name:
        first_line = (
            f"- [{args.name}]({args.url}) - Description\n\n  "
            f"{format_metrics_badges(metrics)}"
        )
        new_frameworks_section += f"{first_line}\n\n  - Add description here."

    with open(readme_path, "w") as f:
        f.write(header + "## Frameworks\n" + new_frameworks_section)


def process_readme(readme_path, args):
    update_readme_with_metrics(readme_path, args)
    print("✨ README updated successfully with repository metrics!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update README with repository metrics"
    )
    framework = parser.add_argument_group("framework")
    framework.add_argument("--url", help="URL of the GitHub repository")
    framework.add_argument("--name", help="Name of the repository")
    args = parser.parse_args()

    if bool(args.url) != bool(args.name):
        parser.error("--url and --name must be given together")

    process_readme("README.md", args)
