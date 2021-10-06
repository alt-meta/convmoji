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
