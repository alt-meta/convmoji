import typing
import pytest


@pytest.fixture(scope="module")
def default_description() -> str:
    return "meine commit message"


@pytest.fixture(scope="module")
def default_commit_type() -> str:
    return "feat"


@pytest.fixture(scope="module")
def default_scope() -> str:
    return "devScope"


@pytest.fixture(scope="module")
def default_body() -> str:
    return "awesome stuff, believe me"


@pytest.fixture(scope="module")
def default_footer() -> str:
    return "i'm your footer"


@pytest.fixture(scope="module")
def default_breaking_changes() -> str:
    return "Something"


@pytest.fixture(scope="module")
def expected_scopes() -> typing.List[str]:
    return [
        "action",
        "documentation",
        "actions",
        "readme",
        "error-handling",
        "pipy",
        "README",
        "coverage",
        "trynerror",
        "cli-options",
    ]
