
[![Test](https://github.com/KnowKit/convmoji/actions/workflows/test.yaml/badge.svg)](https://github.com/KnowKit/convmoji/actions/workflows/test.yaml)
[![codecov](https://codecov.io/gh/KnowKit/convmoji/branch/main/graph/badge.svg?token=84LAM4S1RD)](https://codecov.io/gh/KnowKit/convmoji)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# convmoji

A simple cli tool to commit Conventional Commits.

## usage

````bash
convmoji commit feature "my commit message"
convmoji commit feature devscope "my commit message"
convmoji commit feature devscope "my commit message" \
  --ammend --no-verify
convmoji commit feature devscope "my commit message" --body "my body message" \
  --footer "my body message" \
  --breacking-change "contains a breaking change" \
  --ammend --no-verify

# If you want to see what to does without performing the action, run it with --debug
convmoji commit feature devscope "my commit message" <MoreOptions> --debug
````

## commit types

* `feat`: ✨
* `fix`: 🐛
* `docs`: 📚
* `style`: 💎
* `refactor`: 🔨
* `perf`: 🚀
* `test`: 🚨
* `build`: 📦
* `ci`: 👷
* `chore`: 🔧