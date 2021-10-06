
[![Test](https://github.com/KnowKit/fluffy-waffle/actions/workflows/test.yaml/badge.svg)](https://github.com/KnowKit/fluffy-waffle/actions/workflows/test.yaml)
[![codecov](https://codecov.io/gh/KnowKit/fluffy-waffle/branch/main/graph/badge.svg?token=84LAM4S1RD)](https://codecov.io/gh/KnowKit/fluffy-waffle)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# fluffy-waffle

A simple cli tool to commit Conventional Commits.

## Usage

````bash
fluffy-waffle commit feature "my commit message"
fluffy-waffle commit feature devscope "my commit message"
fluffy-waffle commit feature devscope "my commit message" \
  --ammend --no-verify
fluffy-waffle commit feature devscope "my commit message" --body "my body message" \
  --footer "my body message" \
  --breacking-change "contains a breaking change" \
  --ammend --no-verify

# If you want to see what to does without performing the action, run it with --debug
fluffy-waffle commit feature devscope "my commit message" <MoreOptions> --debug
````
