"""False-positive traps. A good scanner reports none of these."""

# A UUID, not a secret
REQUEST_ID = "550e8400-e29b-41d4-a716-446655440000"

# A git commit SHA, not a secret
BASE_COMMIT = "6d0b145a9f3c21e8b7d40f5c2a1e9b8d7c6f5e4a"

# A lockfile integrity hash, not a secret
INTEGRITY = "sha512-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

# A placeholder, not a secret
password = "password"

# The key from AWS's own documentation
DOCS_EXAMPLE_KEY = "AKIAIOSFODNN7EXAMPLE"
