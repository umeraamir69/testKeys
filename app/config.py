"""Application configuration."""

import os

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

api_key = os.environ["SERVICE_API_KEY"]

SESSION_JWT = os.environ.get("SESSION_JWT", "")

DEBUG = os.environ.get("DEBUG") == "1"
