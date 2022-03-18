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
