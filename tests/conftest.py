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


@pytest.fixture(scope="module")
def default_stdout_return_value() -> str:
    return """
📦: v0.1.5
Merge pull request #3 from KnowKit/feature/print-command
✨: add new option print
📦(readme): Actions update
Merge branch 'main' of github.com:KnowKit/convmoji
🚨: removed linter warnings
✨(error-handling): 0.1.3
📚(readme): Updated docs
📚: merged README
🔨(cli-options): v0.1.2
📚(readme): Update to README.md
🚨(coverage): Update .coveragerc
Create LICENSE
Update README.md
📚(documentation): v0.1.1
🚨: removed linter warnings
📚(documentation): Docs, short options, helper strings
📦(pipy): convmoji 0.1.0 Co-authored-by: defel <defel@no-reply>
📚(README): Updated to docs
✨: badges are fun
🐛(action): fixed lint action
🐛(trynerror): action fix
🐛(trynerror): Small changes
🚨: Updated --no-verify test
🐛(actions): fixed install command in gh_actions
✨‼️(project): initial commit
✨: meine commit message
"""