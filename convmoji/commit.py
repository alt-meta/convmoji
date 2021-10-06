#!/usr/bin/env python

import os
import typing
import typer

from convmoji import commit_types


app = typer.Typer()
helpers = {
    "description": "Commit message, as in 'git commit -m \"...\"'",
    "commit_type": f"Either of [{','.join(commit_types.possible_commit_types.keys())}]",
    "scope": "Scope for commit (any string)",
    "body": "Body message for commit",
    "footer": "Footer message (formatted two blank lines below body)",
    "breaking-changes": "Specially formatted message to show changes might break previous versions",  # noqa
    "amend": "Execute commit with --amend",
    "no-verify": "Execute commit with --no-verify",
    "co-authored-by": "A string of authors formatted like:\
        --co-authored-by '<User user@no-reply> '\
        --co-authored-by '<User2 user2@no-reply>'",
}


def validate_commit_type(type: str) -> str:
    commit_type = commit_types.CommitType(type=type)
    return commit_type.emoji


@app.command()
def commit(
    description: str = typer.Argument(..., help=helpers["description"]),
    commit_type: typing.Optional[str] = typer.Argument(
        ...,
        callback=validate_commit_type,
        help=helpers["commit_type"],
    ),
    scope: typing.Optional[str] = typer.Argument(default="", help=helpers["scope"]),
    body: typing.Optional[str] = typer.Argument(default="", help=helpers["body"]),
    footer: typing.Optional[str] = typer.Argument(default="", help=helpers["footer"]),
    breaking_changes: str = typer.Option(
        default="",
        help=helpers["breaking-changes"],
    ),
    amend: bool = typer.Option(False, "--amend/ ", "-a/ ", help=helpers["amend"]),
    no_verify: bool = typer.Option(
        False, "--no-verify/ ", "--nv/ ", help=helpers["no-verify"]
    ),
    co_authored_by: typing.Optional[typing.List[str]] = typer.Option(
        None,
        "--co-authored_by/ ",
        "--co/ ",
        help=helpers["co-authored-by"],
    ),
    debug: bool = typer.Option(default=False, metavar="--debug"),
):
    cmd = commit_types.CommitCmd(
        type=commit_type,
        scope=scope,
        description=description,
        body=body,
        footer=footer,
        breaking_changes=breaking_changes,
        amend=amend,
        no_verify=no_verify,
        co_authored_by=co_authored_by,
    )
    if debug:
        typer.echo(repr(cmd))
    else:
        os.system(repr(cmd))


if __name__ == "__main__":
    app()  # pragma: no cover
