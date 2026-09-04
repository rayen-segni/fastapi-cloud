# FastAPI Cloud Deploy

A GitHub Action for deploying FastAPI applications to [FastAPI Cloud](https://fastapicloud.com/).

## Status

Work in progress.

## Usage

```yaml
name: Deploy to FastAPI Cloud

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Deploy to FastAPI Cloud
        uses: rayensegni/fastapi-cloud-deploy@v1
        env:
          FASTAPI_CLOUD_TOKEN: ${{ secrets.FASTAPI_CLOUD_TOKEN }}
          FASTAPI_CLOUD_APP_ID: ${{ secrets.FASTAPI_CLOUD_APP_ID }}
```

> Replace `rayensegni/fastapi-cloud-deploy` with the repository owner and name of your action.

## Requirements

The action requires:

- `FASTAPI_CLOUD_TOKEN` — FastAPI Cloud deployment token.
- `FASTAPI_CLOUD_APP_ID` — FastAPI Cloud application ID.

Store these values as GitHub repository or environment secrets.

## Features

Planned features include:

- Deploy FastAPI applications from GitHub Actions.
- Simple configuration.
- Support for common FastAPI Cloud deployment options.
- Clear deployment status and error messages.

## License

This project is licensed under the MIT License.