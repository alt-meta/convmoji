#!/usr/bin/env python

import os
import typing
import typer

from convmoji.commit_types import CommitType, CommitCmd


app = typer.Typer()


def validate_commit_type(type: str) -> str:
    commit_type = CommitType(type=type)
    return commit_type.emoji


@app.command()
def commit(
    description: str = typer.Argument(...),
    commit_type: typing.Optional[str] = typer.Argument(
        "feat", callback=validate_commit_type
    ),
    scope: typing.Optional[str] = typer.Argument(""),
    body: typing.Optional[str] = typer.Argument(""),
    footer: typing.Optional[str] = typer.Argument(""),
    breaking_changes: str = typer.Option(default=""),
    amend: bool = typer.Option(default=False, metavar="--amend"),
    no_verify: bool = typer.Option(default=False, metavar="--no-verify"),
    co_authored_by: typing.Optional[typing.List[str]] = typer.Option(None),
    debug: bool = typer.Option(default=False, metavar="--debug"),
):
    cmd = CommitCmd(
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
