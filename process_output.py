#!/usr/bin/env python3
"""
Process JSON output from `fastapi cloud deploy --json`.
Exposes outputs for GitHub Actions ($GITHUB_OUTPUT) and creates a Markdown Job Summary ($GITHUB_STEP_SUMMARY).
"""

import json
import os
import sys


def get_input_json() -> str:
    """Retrieve JSON string from CLI arguments or stdin."""
    # 1. First check command-line argument: python3 process_output.py '<json>'
    if len(sys.argv) > 1 and sys.argv[1].strip():
        return sys.argv[1].strip()

    # 2. Check piped input: echo '<json>' | python3 process_output.py
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()

    return ""


def main():
    raw = get_input_json()
    if not raw:
        print("::warning::No JSON input provided to process_output.py", file=sys.stderr)
        sys.exit(0)

    try:
        parsed = json.loads(raw)
        data = parsed.get("data", {})
    except Exception as e:
        print(f"::warning::Failed to parse deployment JSON output: {e}", file=sys.stderr)
        sys.exit(0)

    url = data.get("url", "")
    dashboard_url = data.get("dashboard_url", "")
    deployment_id = data.get("deployment_id", "")
    slug = data.get("slug", "")

    # 1. Print formatted console output
    print("\n" + "=" * 50)
    print("🚀 FastAPI Cloud Deployment Succeeded!")
    if url:
        print(f" • App URL:        {url}")
    if dashboard_url:
        print(f" • Dashboard:      {dashboard_url}")
    if deployment_id:
        print(f" • Deployment ID: {deployment_id}")
    if slug:
        print(f" • App Slug:      {slug}")
    print("=" * 50 + "\n")

    # 2. Write GitHub Actions step outputs
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output and os.path.exists(github_output):
        with open(github_output, "a", encoding="utf-8") as f:
            if url:
                f.write(f"url={url}\n")
            if dashboard_url:
                f.write(f"dashboard-url={dashboard_url}\n")
            if deployment_id:
                f.write(f"deployment-id={deployment_id}\n")
            if slug:
                f.write(f"slug={slug}\n")

    # 3. Write rich GitHub Actions Job Summary
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary and os.path.exists(step_summary):
        with open(step_summary, "a", encoding="utf-8") as f:
            f.write("### 🚀 FastAPI Cloud Deployment\n\n")
            f.write("| Key | Details |\n")
            f.write("| :--- | :--- |\n")
            if url:
                f.write(f"| **App URL** | [{url}]({url}) |\n")
            if dashboard_url:
                f.write(f"| **Dashboard** | [View Deployment]({dashboard_url}) |\n")
            if slug:
                f.write(f"| **App Slug** | `{slug}` |\n")
            if deployment_id:
                f.write(f"| **Deployment ID** | `{deployment_id}` |\n\n")


if __name__ == "__main__":
    main()
