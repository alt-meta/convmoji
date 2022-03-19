import typing

from prompt_toolkit.application import AppSession, create_app_session
from prompt_toolkit.input import create_pipe_input
from prompt_toolkit.input.base import PipeInput
from prompt_toolkit.output import DummyOutput


class Interactions(typing.TypedDict):
    msg: str
    type: str
    scope: str
    body: str
    footer: str
    breaking_changes: str
    co_authors: str
    execute: str


class KeyInputs:
    DOWN = "\x1b[B"
    UP = "\x1b[A"
    LEFT = "\x1b[D"
    RIGHT = "\x1b[C"
    ENTER = "\r"
    ESCAPE = "\x1b"
    CONTROLC = "\x03"
    BACK = "\x7f"
    SPACE = " "
    TAB = "\x09"
    ONE = "1"
    TWO = "2"
    THREE = "3"


def get_pipe_for_interaction(
    interactions: Interactions,
) -> typing.Tuple[typing.Generator[AppSession, None, None], PipeInput]:
    input_pipe = create_pipe_input()
    for action in interactions.values():
        input_pipe.send_text(action)
    return create_app_session(input=input_pipe, output=DummyOutput()), input_pipe


interactions_expectations: typing.List[typing.Tuple[Interactions, str]] = [
    (
        Interactions(
            msg="My commit message\n",
            type="\n",
            scope="\n",
            body="\n",
            footer="\n",
            breaking_changes="\n",
            co_authors="\n",
            execute="n\n",
        ),
        "✨: My commit message",
    ),
    (
        Interactions(
            msg="Updated docs\n",
            type=(KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.ENTER),
            scope="web-docs\n",
            body="\n",
            footer="\n",
            breaking_changes="\n",
            co_authors="defel, arrrrrmin\n",
            execute="n\n",
        ),
        "📚(web-docs): Updated docs\nCo-authored-by: defel\nCo-authored-by: arrrrrmin",
    ),
    (
        Interactions(
            msg="Hello, I cancel this process soon",
            type=KeyInputs.CONTROLC,
            scope="\n",
            body="\n",
            footer="\n",
            breaking_changes="\n",
            co_authors="\n",
            execute="n\n",
        ),
        "Aborted, convmoji stopped.",
    ),
]
