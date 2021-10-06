import typing
import pytest


@pytest.fixture(scope="module")
def default_description() -> typing.Generator:
    yield "meine commit message"


@pytest.fixture(scope="module")
def default_commit_type() -> typing.Generator:
    yield "feat"


@pytest.fixture(scope="module")
def default_scope() -> typing.Generator:
    yield "devScope"


@pytest.fixture(scope="module")
def default_body() -> typing.Generator:
    yield "awesome stuff, believe me"


@pytest.fixture(scope="module")
def default_footer() -> typing.Generator:
    yield "i'm your footer"


@pytest.fixture(scope="module")
def default_breaking_changes() -> typing.Generator:
    yield "Something"


# description
# commit_type
# scope
# body
# footer
# breaking_changes
# ammend
# no_verify
# co_authored_by
