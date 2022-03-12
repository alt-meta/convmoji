import typing
from typer.testing import CliRunner

from convmoji import __name__, __version__, __homepage__, __pypi__
from convmoji.commit import app, err_messages

runner = CliRunner()


def invoke_app_commit(*args):
    invoke_values = []
    invoke_values.extend(list(args))
    return runner.invoke(app, invoke_values)


def test_app_commit_fail_001():
    result = invoke_app_commit("")
    assert result.exit_code == 1
    assert err_messages["description"] in result.stdout


def test_app_commit_fail_002(default_description: str):
    result = invoke_app_commit(default_description, "testing")
    assert result.exit_code == 1
    assert err_messages["commit_type"] in result.stdout


def test_app_commit_001_fix(default_description: str):
    result = invoke_app_commit(default_description, "fix", "--debug")
    assert result.exit_code == 0
    assert f"🐛: {default_description}" in result.stdout


def test_app_commit_001_docs(default_description: str):
    result = invoke_app_commit(default_description, "docs", "--debug")
    assert result.exit_code == 0
    assert f"📚: {default_description}" in result.stdout


def test_app_commit_001_style(default_description: str):
    result = invoke_app_commit(default_description, "style", "--debug")
    assert result.exit_code == 0
    assert f"💎: {default_description}" in result.stdout


def test_app_commit_001_refactor(default_description: str):
    result = invoke_app_commit(default_description, "refactor", "--debug")
    assert result.exit_code == 0
    assert f"🔨: {default_description}" in result.stdout


def test_app_commit_001_perf(default_description: str):
    result = invoke_app_commit(default_description, "perf", "--debug")
    assert result.exit_code == 0
    assert f"🚀: {default_description}" in result.stdout


def test_app_commit_001_test(default_description: str):
    result = invoke_app_commit(default_description, "test", "--debug")
    assert result.exit_code == 0
    assert f"🚨: {default_description}" in result.stdout


def test_app_commit_001_build(default_description: str):
    result = invoke_app_commit(default_description, "build", "--debug")
    assert result.exit_code == 0
    assert f"📦: {default_description}" in result.stdout


def test_app_commit_001_ci(default_description: str):
    result = invoke_app_commit(default_description, "ci", "--debug")
    assert result.exit_code == 0
    assert f"👷: {default_description}" in result.stdout


def test_app_commit_001_chore(default_description: str):
    result = invoke_app_commit(default_description, "chore", "--debug")
    assert result.exit_code == 0
    assert f"🔧: {default_description}" in result.stdout


def test_app_commit_001_feat(default_description: str, default_commit_type: str):
    result = invoke_app_commit(default_description, "--debug")
    assert result.exit_code == 0
    assert "git commit -m " in result.stdout
    assert "✨" in result.stdout
    assert default_description in result.stdout
    assert f"✨: {default_description}" in result.stdout


def test_app_commit_002(
    default_description: str, default_commit_type: str, default_scope: str
):
    result = invoke_app_commit(
        default_description, default_commit_type, "--scope", default_scope, "--debug"
    )
    assert result.exit_code == 0
    assert "git commit -m " in result.stdout
    assert "✨" in result.stdout
    assert f"({default_scope})" in result.stdout
    assert default_description in result.stdout
    assert f"✨({default_scope}): {default_description}" in result.stdout


def test_app_commit_003(
    default_description: str,
    default_commit_type: str,
    default_scope: str,
    default_body: str,
):
    result = invoke_app_commit(
        default_description,
        default_commit_type,
        "-s",
        default_scope,
        "--body",
        default_body,
        "--debug",
    )
    assert result.exit_code == 0
    assert "git commit -m " in result.stdout
    assert "✨" in result.stdout
    assert f"({default_scope})" in result.stdout
    assert default_description in result.stdout
    assert f"✨({default_scope}): {default_description}" in result.stdout
    assert default_body in result.stdout


def test_app_commit_004(
    default_description: str,
    default_commit_type: str,
    default_scope: str,
    default_body: str,
    default_footer: str,
):
    result = invoke_app_commit(
        default_description,
        default_commit_type,
        "-s",
        default_scope,
        "-b",
        default_body,
        "--foot",
        default_footer,
        "--debug",
    )
    assert result.exit_code == 0
    assert "git commit -m " in result.stdout
    assert "✨" in result.stdout
    assert f"({default_scope})" in result.stdout
    assert default_description in result.stdout
    assert f"✨({default_scope}): {default_description}" in result.stdout
    assert default_body in result.stdout
    assert default_footer in result.stdout


def test_app_commit_005(
    default_description: str,
    default_commit_type: str,
    default_scope: str,
    default_body: str,
    default_footer: str,
    default_breaking_changes: str,
):
    result = invoke_app_commit(
        default_description,
        default_commit_type,
        "-s",
        default_scope,
        "-b",
        default_body,
        "-f",
        default_footer,
        "--breaking-changes",
        default_breaking_changes,
        "--no-verify",
        "--debug",
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


def test_app_commit_006(
    default_description: str,
    default_commit_type: str,
    default_scope: str,
    default_body: str,
    default_footer: str,
    default_breaking_changes: str,
):
    result = invoke_app_commit(
        default_description,
        default_commit_type,
        "-s",
        default_scope,
        "-b",
        default_body,
        "-f",
        default_footer,
        "--bc",
        default_breaking_changes,
        "--amend",
        "--no-verify",
        "--debug",
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
    assert "--amend" in result.stdout
    assert "--no-verify" in result.stdout


def test_app_commit_info_007():
    result = invoke_app_commit("--info")
    stdout_lines = result.stdout.split("\n")
    assert __name__ in stdout_lines[0]
    assert __version__ in stdout_lines[1]
    assert __homepage__ in stdout_lines[2]
    assert __pypi__ in stdout_lines[3]


def test_app_commit_version_008():
    result = invoke_app_commit("--version")
    assert f"{__name__} {__version__}" in result.stdout


def test_print_message(default_description: str):
    result = invoke_app_commit(default_description, "--print")
    assert f"✨: {default_description}\n\n" == result.stdout


def test_show_scopes(expected_scopes: typing.List[str]):
    result = invoke_app_commit("--show-scopes")
    output = list(filter(lambda res: len(res) > 0, result.stdout.split("\n")))
    assert len(output) >= 0
    assert all(map(lambda scope: scope in expected_scopes, output))
