import re
import subprocess
import typing

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

    def message_formatter(self):
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
        if self.breaking_changes:
            self.type = f"{self.type}‼️"

        if self.scope == "":
            return f"{self.type}: {message}"

        return f"{self.type}({self.scope}): {message}"

    def __repr__(self):
        optional_args = ""
        optional_args += "--amend " if self.amend else ""
        optional_args += "--no-verify " if self.no_verify else ""

        message = self.message_formatter()
        return f'{commit_cmd_base} "{message}" {optional_args}'


class CommitScopes(BaseModel):
    scopes: typing.Optional[typing.List[str]] = None

    @validator("scopes", pre=True, always=True)
    def find_commits(cls, v: typing.Any) -> typing.List[str]:  # noqa: U100
        emojis = "".join(possible_commit_types.values())
        scopes_pattern = re.compile(fr"[{emojis}]\(([\w_\-\d]*)\)")
        messages = subprocess.check_output(["git", "log", '--pretty="%s"'])
        scopes = []
        if messages == 0:
            return scopes  # pragma: no cover
        else:
            messages = messages.decode("utf-8").split("\n")
            messages = list(
                filter(
                    lambda msg: (
                        len(msg) > 0 and msg[1] in possible_commit_types.values()
                    ),
                    messages,
                )
            )
            scopes = list(
                set(
                    map(
                        lambda msg_pattern: msg_pattern.group(1),
                        filter(
                            lambda pattern: pattern is not None,
                            map(lambda msg: scopes_pattern.search(msg), messages),
                        ),
                    )
                )
            )
        return sorted(scopes)

    def __repr__(self):
        return "\n".join(self.scopes).strip()
