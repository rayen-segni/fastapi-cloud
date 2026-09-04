#!/usr/bin/env bash
# Mask secret in runner logs
echo "::add-mask::$FASTAPI_CLOUD_TOKEN"

# Validate required inputs upfront
if [ -z "$FASTAPI_CLOUD_TOKEN" ]; then
echo "::error::Missing required input: token (or secret FASTAPI_CLOUD_TOKEN)"
exit 1
fi

if [ -z "$FASTAPI_CLOUD_APP_ID" ]; then
echo "::error::Missing required input: app-id"
exit 1
fi

# Ensure fastapi CLI is available
if ! command -v fastapi &> /dev/null; then
echo "Installing FastAPI CLI..."
pipx install "fastapi[standard]"
fi