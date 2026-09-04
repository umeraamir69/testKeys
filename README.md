# testKeys

Deliberately vulnerable repo used to test [SecSentry](https://github.com/umeraamir69/secsentry).

**Every credential in this repository is fake.** They are structurally valid (right prefix, right length, so scanners fire) but they were never issued by any provider and authenticate to nothing.

## Why this exists

A developer deletes a key from a file and assumes the leak is fixed. Git history disagrees.

This repo reproduces that exact situation:

| Commit | What happens |
|---|---|
| 1 | Fake credentials are hardcoded in `app/`, `deploy/`, and a committed `.env` |
| 2 | "Remove hardcoded credentials" — the files are cleaned up and read from the environment |

After commit 2 the working tree is clean. The secrets are still in history.

## The demo

```bash
git clone https://github.com/umeraamir69/testKeys.git
cd testKeys

secsentry scan .              # clean — nothing in the working tree
secsentry scan . --history    # still finds every planted key, with the commit and author
```

The history scan reports `still_in_head=false`, which is the whole point: the leak is invisible to a normal scan but fully recoverable from `git log`.

## What is planted

Positives (should be detected):

- AWS access key ID
- GitHub personal access token
- OpenAI API key
- Slack bot token
- PostgreSQL connection string with an inline password
- RSA private key
- Generic `api_key = "..."` assignment
- JWT

Negatives (should **not** be reported — these are the false-positive traps):

- A UUID
- A git commit SHA
- A `sha512-` lockfile integrity hash
- `password = "password"`
- `AKIAIOSFODNN7EXAMPLE`, the key from AWS's own documentation

## Note on GitHub secret scanning

GitHub may flag these or block the push, since it pattern-matches the same prefixes. That is a reasonable thing for it to do. Nothing here is live, so it is safe to mark as a false positive and allow the push.

Do not add a real credential to this repository for any reason.
