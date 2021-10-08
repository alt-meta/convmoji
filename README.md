
[![Build](https://github.com/KnowKit/convmoji/actions/workflows/build.yaml/badge.svg)](https://github.com/KnowKit/convmoji/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/KnowKit/convmoji/branch/main/graph/badge.svg?token=84LAM4S1RD)](https://codecov.io/gh/KnowKit/convmoji)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI version](https://badge.fury.io/py/convmoji.svg)](https://badge.fury.io/py/convmoji)

# convmoji

A simple cli tool to commit Conventional Commits.

### Install

```bash
pip install convmoji
convmoji --help
```

## Examples

A conventianal commit
````bash
convmoji "epic feature added" feat
````

One with a scope
````bash
convmoji "epic feature added" feat --scope somescope
# ✨: epic feature added
````

With some options
````bash
convmoji "epic feature added" feat --scope somescope --amend --no-verify
# ✨(somescope): epic feature added --amend --no-verify
````

With more textual information
````bash
convmoji "epic feature added" feat --scope somescope \
  --body "more body information" --foot "more footer information"
# ✨(somescope): epic feature added
# 
# more body information
# 
# more footer information
````

Inform people about breaking changes
````bash
convmoji "epic feature added" feat --scope somescope \
  --body "more body information" --footer "more footer information" \
  --breaking-changes "breaks somthing"
# ✨‼️(somescope): epic feature added
# 
# more body information
# 
# BREAKING CHANGE: breaks somthing
# more footer information
````

> If you want to see what to does without performing the action, run it with `--debug`

## Commit types

For details on commit types see [conventional commits specification](https://www.conventionalcommits.org/en/v1.0.0/#specification).

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

## convmoji --help

**Usage**:

```console
$ convmoji [OPTIONS] DESCRIPTION [COMMIT_TYPE]
```

**Arguments**:

* `DESCRIPTION`: Commit message, as in 'git commit -m "..."'  [required]
* `[COMMIT_TYPE]`: Either of [feat, fix, docs, style, refactor, perf, test, build, ci, chore]  [default: feat]

**Options**:

* `-s, --scope TEXT`: Scope for commit (any string)  [default: ]
* `-b, --body TEXT`: Body message for commit  [default: ]
* `-f, --foot TEXT`: Footer message (formatted two blank lines below body)  [default: ]
* `--breaking-changes, --bc TEXT`: Specially formatted message to show changes might break         previous versions  [default: ]
* `--amend`: Execute commit with --amend  [default: False]
* `--no-verify`: Execute commit with --no-verify  [default: False]
* `--co-authored_by, --co TEXT`: A string of authors formatted like:        --co-authored-by '<User user@no-reply> '        --co-authored-by '<User2 user2@no-reply>'
* `--debug`: Debug mode (does not execute commit)  [default: False]
* `--info`: Prompt convmoji info (does not execute commit)
* `--version`: Prompt convmoji version (does not execute commit)
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.
