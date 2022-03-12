from unittest.mock import MagicMock, patch

import pytest
from pydantic import typing, ValidationError

from convmoji.commit_types import CommitScopes, possible_commit_types, CommitType


def test_commit_types_emoji_selection_pass():
    for commit_type, emoji in possible_commit_types.items():
        commit_type_model = CommitType(type=commit_type)
        assert commit_type_model.emoji == possible_commit_types[commit_type]


def test_commit_types_emoji_selection_fail():
    with pytest.raises(ValidationError) as exeception:
        commit_type_model = CommitType(type="testing")

    with pytest.raises(ValidationError) as exeception:
        commit_type_model = CommitType(type="None")

    with pytest.raises(ValidationError) as exeception:
        commit_type_model = CommitType(type="performance")

    with pytest.raises(ValidationError) as exeception:
        commit_type_model = CommitType(type="feature")


@patch("convmoji.commit_types.subprocess.run")
def test_commit_scopes_pass(
    mock_run, default_stdout_return_value, expected_scopes: typing.List[str]
):
    mock_stdout = MagicMock()
    mock_stdout.configure_mock(
        **{"stdout.decode.return_value": default_stdout_return_value}
    )
    commit_scopes = CommitScopes()
    assert commit_scopes.scopes is not None
    assert all(map(lambda scope: scope in expected_scopes, commit_scopes.scopes))
