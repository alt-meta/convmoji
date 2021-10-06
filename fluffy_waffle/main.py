#!/usr/bin/env python

import typer

from fluffy_waffle import commit

app = typer.Typer()
app.add_typer(commit.app)

# TODO: app.add_typer(wizard, name="wizard")


if __name__ == "__main__":
    app()
