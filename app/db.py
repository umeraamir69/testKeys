"""Database connection."""

import os

DATABASE_URL = os.environ["DATABASE_URL"]


def connect():
    return DATABASE_URL
