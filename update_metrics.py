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
        f"{metrics['stars']:,} stars · {metrics['forks']:,} forks · {metrics['contributors']:,} contributors · "
        f"{metrics['open_issues']:,} issues · {metrics['language']} · {metrics['license']}"
    )


def update_readme_with_metrics(readme_path):
    with open(readme_path, "r") as f:
        content = f.read()

    current_time = datetime.now().strftime("%Y-%m-%d")
    intro_end = content.find("suggestion, feel free to open an issue or pull request.")
    if intro_end != -1:
        content = (
            content[
                : intro_end
                + len("suggestion, feel free to open an issue or pull request.")
            ]
            + f" (Last updated: {current_time})\n"
            + content[
                intro_end
                + len("suggestion, feel free to open an issue or pull request.") :
            ]
        )

    parts = content.split("## Frameworks")
    if len(parts) < 2:
        return

    header = parts[0]
    frameworks_section = parts[1]
    new_frameworks_section = ""

    framework_entries = re.split(r"\n(?=- \[)", frameworks_section)

    for entry in framework_entries:
        match = re.search(
            r"- \[([^\]]+)\]\((https://github\.com/[^/]+/[^/)\s]+)\)(.*?)(?=\n\n|\n  -|$)",
            entry,
            re.DOTALL,
        )
        if match:
            name, url, desc = match.groups()
            metrics = get_repo_metrics(url)

            if metrics:
                first_line = (
                    f"- [{name}]({url}){desc}\n  {format_metrics_badges(metrics)}"
                )

                features_start = entry.find("\n  -")
                if features_start != -1:
                    rest_of_entry = entry[features_start:]
                else:
                    rest_of_entry = ""

                entry = f"{first_line}\n{rest_of_entry}\n\n"

        new_frameworks_section += entry

    with open(readme_path, "w") as f:
        f.write(header + "## Frameworks\n" + new_frameworks_section)


def process_readme(readme_path):
    update_readme_with_metrics(readme_path)
    print("✨ README updated successfully with repository metrics!")


if __name__ == "__main__":
    process_readme("README.md")
