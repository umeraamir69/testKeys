"""Database connection."""

DATABASE_URL = "postgres://appuser:s3cr3tP4ssw0rd@db.internal:5432/appdb"


def connect():
    return DATABASE_URL
