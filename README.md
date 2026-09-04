# FastAPI Cloud Deploy (v1.0.0)

A lightweight, secure GitHub Action to deploy FastAPI applications directly to **FastAPI Cloud** from your CI/CD pipelines.

---

### Features

- **Automated Tooling Setup:** Dynamically verifies and installs `fastapi[standard]` via `pipx` without altering the runner's global Python environment.
- **Secure by Default:** Automatically masks authentication tokens in runner logs using `::add-mask::` and validates required secrets before running.
- **Structured Output:** Parses deployment JSON and prints clean status metrics including App URL, Dashboard link, Deployment ID, and App Slug.
- **Customizable Execution:** Supports custom working directories and asynchronous non-blocking deployments (`no-wait`).

---

### Prerequisites & Setup Guide

#### 1. FastAPI Cloud Configuration

1. Log in to [FastAPI Cloud](https://fastapicloud.com/).
2. Create your application:
   - Click **Create App** → Choose **Empty App** → Enter your app name.
3. Configure Environment Variables:
   - Navigate to the **Environment Variables** section.
   - Click **Add Environment Variable** → Click **Import .env**.
   - Paste your `.env` contents (adjust production-specific values accordingly).
4. Generate an API Token:
   - Navigate to the **Tokens** section.
   - Click **Create Token**, select name and expiration.
   - Copy the token immediately (it will only be displayed once).
5. Copy your **App ID** located to the right of your application name at the top of the dashboard.

#### 2. GitHub Secrets Setup

1. In your GitHub repository, open **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret** and add:
   - `FASTAPI_CLOUD_APP_ID`: Your copied App ID.
   - `FASTAPI_CLOUD_TOKEN`: Your copied API token.

---

### Usage Example

```yaml
name: Deploy Application

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Deploy to FastAPI Cloud
        uses: rayensegni/fastapi-cloud-deploy@v1
        with:
          app-id: ${{ secrets.FASTAPI_CLOUD_APP_ID }}
          token: ${{ secrets.FASTAPI_CLOUD_TOKEN }}
          working-directory: "./"
          no-wait: "false"
```

## License

This project is licensed under the MIT License.
