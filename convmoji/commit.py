#!/usr/bin/env python

import os
import typing
import typer

from convmoji import __version__, __homepage__, __pypi__, commit_types
from convmoji.commit_types import CommitScopes, possible_commit_types


app = typer.Typer()
helpers = {
    "description": "Commit message, as in 'git commit -m \"...\"'",
    "commit_type": f"Either of [{', '.join(commit_types.possible_commit_types.keys())}]",
    "scope": "Scope for commit (any string)",
    "body": "Body message for commit",
    "footer": "Footer message (formatted two blank lines below body)",
    "breaking-changes": "Specially formatted message to show changes might break \
        previous versions",
    "amend": "Execute commit with --amend",
    "no-verify": "Execute commit with --no-verify",
    "co-authored-by": "A string of authors formatted like:\
        --co-authored-by '<User user@no-reply> '\
        --co-authored-by '<User2 user2@no-reply>'",
    "debug": "Debug mode (does not execute commit)",
    "print": "Print the commit message (does not execute commit)",
    "show-scopes": "A helper that shows scopes used with convmoji. "
    "(does not execute commit)",
    "info": "Prompt convmoji info (does not execute commit)",
    "version": "Prompt convmoji version (does not execute commit)",
}
err_messages = {
    "description": "Description for commit is required",
    "commit_type": f"Commit type should be one of: {list(possible_commit_types.keys())}",
}


def validate_description(description_string: str) -> str:
    if len(description_string) < 1:
        typer.echo(err_messages["description"], err=True)
        raise typer.Exit(code=1)
    return description_string


def validate_commit_type(type_string: str) -> str:
    if type_string not in possible_commit_types.keys():
        typer.echo(err_messages["commit_type"], err=True)
        raise typer.Exit(code=1)
    commit_type = commit_types.CommitType(type=type_string)
    return commit_type.emoji


def show_scopes_callback(value: bool):
    if value:
        scopes = CommitScopes()
        typer.echo(repr(scopes))
        raise typer.Exit(code=0)
    return value


def info_callback(value: bool):
    if value:
        typer.echo("convmoji")
        typer.echo(f"version: {__version__}")
        typer.echo(f"homepage: {__homepage__}")
        typer.echo(f"pypi: {__pypi__}")
        raise typer.Exit(code=0)
    return value


def version_callback(value: bool):
    if value:
        typer.echo(f"convmoji {__version__}")
        raise typer.Exit(code=0)
    return value


@app.command()
def commit(
    description: str = typer.Argument(
        ..., callback=validate_description, help=helpers["description"]
    ),
    commit_type: typing.Optional[str] = typer.Argument(
        "feat",
        callback=validate_commit_type,
        help=helpers["commit_type"],
    ),
    scope: typing.Optional[str] = typer.Option(
        "", "--scope/ ", "-s/ ", help=helpers["scope"]
    ),
    body: typing.Optional[str] = typer.Option(
        "", "--body/ ", "-b/ ", help=helpers["body"]
    ),
    footer: typing.Optional[str] = typer.Option(
        "", "--foot/ ", "-f/ ", help=helpers["footer"]
    ),
    breaking_changes: str = typer.Option(
        "",
        "--breaking-changes/ ",
        "--bc/ ",
        help=helpers["breaking-changes"],
    ),
    amend: bool = typer.Option(False, "--amend", help=helpers["amend"]),
    no_verify: bool = typer.Option(False, "--no-verify", help=helpers["no-verify"]),
    co_authored_by: typing.Optional[typing.List[str]] = typer.Option(
        None,
        "--co-authored-by/ ",
        "--co/ ",
        help=helpers["co-authored-by"],
    ),
    debug: bool = typer.Option(False, "--debug", help=helpers["debug"]),
    print_message: bool = typer.Option(False, "--print", help=helpers["print"]),
    show_scopes: typing.Optional[bool] = typer.Option(  # noqa: U100
        None,
        "--show-scopes",
        callback=show_scopes_callback,
        is_eager=True,
        help=helpers["show-scopes"],
    ),
    info: typing.Optional[bool] = typer.Option(  # noqa: U100
        None,
        "--info",
        callback=info_callback,
        is_eager=True,
        help=helpers["info"],
    ),
    version: typing.Optional[bool] = typer.Option(  # noqa: U100
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help=helpers["version"],
    ),
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
    elif print_message:
        typer.echo(cmd.message_formatter())
    else:
        os.system(repr(cmd))  # pragma: no cover


if __name__ == "__main__":
    app()  # pragma: no cover
