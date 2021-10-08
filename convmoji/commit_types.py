import typing

import typer
from pydantic import BaseModel, validator, root_validator


# See: https://gist.github.com/parmentf/359667bf23e08a1bd8241fbf47ecdef0
possible_commit_types = {
    "feat": "✨",
    "fix": "🐛",
    "docs": "📚",
    "style": "💎",
    "refactor": "🔨",
    "perf": "🚀",
    "test": "🚨",
    "build": "📦",
    "ci": "👷",
    "chore": "🔧",
}
commit_cmd_base = "git commit -m"


class CommitType(BaseModel):
    type: str
    emoji: typing.Optional[str]

    @validator("type", allow_reuse=True)
    def validate_commit_type(cls, v: str):  # noqa: U100
        if v not in possible_commit_types.keys():
            raise ValueError(f"Commit type not in {possible_commit_types.keys()}")
        return v

    @root_validator
    def find_emoji(cls, values: typing.Dict):
        cls.validate_commit_type(values.get("type"))
        values["emoji"] = possible_commit_types[values.get("type")]
        return values


class CommitCmd(BaseModel):
    type: str
    scope: typing.Optional[str]
    description: str
    body: typing.Optional[str]
    footer: typing.Optional[str]
    breaking_changes: typing.Optional[str]
    amend: typing.Optional[bool]
    no_verify: typing.Optional[bool]
    co_authored_by: typing.Optional[typing.List[str]]

    def _message_formatter(self):
        message = self.description
        if self.body:
            message += f"\n\n{self.body}"
        if self.breaking_changes:
            self.footer = f"BREAKING CHANGE: {self.breaking_changes}\n{self.footer}"
        if self.footer:
            message += f"\n\n{self.footer}"
        if self.co_authored_by is not None:
            message = "{0}\n{1}".format(
                message,
                "\n".join(
                    [f"Co-authored-by: {author}" for author in self.co_authored_by]
                ),
            )
        return message

    def __repr__(self):
        optional_args = ""
        optional_args += "--amend " if self.amend else ""
        optional_args += "--no-verify " if self.no_verify else ""
        if self.breaking_changes:
            self.type = f"{self.type}‼️"
        message = self._message_formatter()
        if self.scope == "":
            return f'{commit_cmd_base} "{self.type}: {message}" {optional_args}'
        return f'{commit_cmd_base} "{self.type}({self.scope}): {message}" {optional_args}'
