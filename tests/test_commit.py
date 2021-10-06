from typer.testing import CliRunner

from fluffy_waffle.commit import app

runner = CliRunner()


# feat
# fix
# docs
# style
# refactor
# perf
# test
# build
# ci
# chore


def test_app_001(default_description: str):
    result = runner.invoke(app, [default_description, "--debug"])
    assert result.exit_code == 0
    assert "git commit -m " in result.stdout
    assert "✨" in result.stdout
    assert default_description in result.stdout
    assert f"✨: {default_description}" in result.stdout


def test_app_002(default_description: str, default_commit_type: str):
    result = runner.invoke(app, [default_description, default_commit_type, "--debug"])
    assert result.exit_code == 0
    assert "git commit -m " in result.stdout
    assert "✨" in result.stdout
    assert default_description in result.stdout
    assert f"✨: {default_description}" in result.stdout


def test_app_003(
    default_description: str, default_commit_type: str, default_scope: str
):
    result = runner.invoke(
        app, [default_description, default_commit_type, default_scope, "--debug"]
    )
    assert result.exit_code == 0
    assert "git commit -m " in result.stdout
    assert "✨" in result.stdout
    assert f"({default_scope})" in result.stdout
    assert default_description in result.stdout
    assert f"✨({default_scope}): {default_description}" in result.stdout


def test_app_004(
    default_description: str,
    default_commit_type: str,
    default_scope: str,
    default_body: str,
):
    result = runner.invoke(
        app,
        [
            default_description,
            default_commit_type,
            default_scope,
            default_body,
            "--debug",
        ],
    )
    assert result.exit_code == 0
    assert "git commit -m " in result.stdout
    assert "✨" in result.stdout
    assert f"({default_scope})" in result.stdout
    assert default_description in result.stdout
    assert f"✨({default_scope}): {default_description}" in result.stdout
    assert default_body in result.stdout


def test_app_005(
    default_description: str,
    default_commit_type: str,
    default_scope: str,
    default_body: str,
    default_footer: str,
):
    result = runner.invoke(
        app,
        [
            default_description,
            default_commit_type,
            default_scope,
            default_body,
            default_footer,
            "--debug",
        ],
    )
    assert result.exit_code == 0
    assert "git commit -m " in result.stdout
    assert "✨" in result.stdout
    assert f"({default_scope})" in result.stdout
    assert default_description in result.stdout
    assert f"✨({default_scope}): {default_description}" in result.stdout
    assert default_body in result.stdout
    assert default_footer in result.stdout


def test_app_006(
    default_description: str,
    default_commit_type: str,
    default_scope: str,
    default_body: str,
    default_footer: str,
    default_breaking_changes: str,
):
    result = runner.invoke(
        app,
        [
            default_description,
            default_commit_type,
            default_scope,
            default_body,
            default_footer,
            "--breaking-changes",
            default_breaking_changes,
            "--no-verify",
            "--debug",
        ],
    )
    assert result.exit_code == 0
    assert "git commit -m " in result.stdout
    assert "✨" in result.stdout
    assert f"({default_scope})" in result.stdout
    assert default_description in result.stdout
    assert f"✨‼️({default_scope}): {default_description}" in result.stdout
    assert default_body in result.stdout
    assert default_footer in result.stdout
    assert f"BREAKING CHANGE: {default_breaking_changes}" in result.stdout
    assert "--no-verify" in result.stdout
