
[![Test](https://github.com/KnowKit/convmoji/actions/workflows/test.yaml/badge.svg)](https://github.com/KnowKit/convmoji/actions/workflows/test.yaml)
[![Codecov](https://codecov.io/gh/KnowKit/convmoji/branch/main/graph/badge.svg?token=84LAM4S1RD)](https://codecov.io/gh/KnowKit/convmoji)
![PyPI](https://img.shields.io/pypi/v/convmoji?label=convmoji)

# convmoji

A simple cli tool to commit Conventional Commits.

### Requirements

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/convmoji)

### Install

```bash
pip install convmoji
convmoji --help
```

## Commit types

For details on commit types see [conventional commits spec](https://www.conventionalcommits.org/en/v1.0.0/#specification).

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

With options
````bash
convmoji "epic feature added" feat --scope somescope --amend --no-verify
# ✨(somescope): epic feature added --amend --no-verify
````

With more informative text
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

Lost track of what scope string to use? Run the following to view all scopes used in 
the mentioned **conventional commits spec** format.
````bash
convmoji --show-scopes
# README
# action
# actions
# cli-options
# coverage
# documentation
# error-handling
# pipy
# readme
# trynerror
````

> If you want to see what to does without performing the action, run it with `--debug`.
> This will prompt the commit command.

> If you want to work with some sort of paste tool or other workflow, for example to pipe results 
> back to ide and commit stuff there, run command with `--print`. 
> This will only prompt the commit message.

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
* `--co-authored_by, --co TEXT`: A string of authors formatted like: _`--co-authored-by '<User user@no-reply> '        --co-authored-by '<User2 user2@no-reply>'`_
* `--debug`: Debug mode (does not execute commit)  [default: False]
* `--show-scopes`: A helper that shows scopes used with convmoji. (does not execute commit)
* `--info`: Prompt convmoji info (does not execute commit)
* `--version`: Prompt convmoji version (does not execute commit)
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.
