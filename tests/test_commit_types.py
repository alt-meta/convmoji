import pytest
from pydantic import ValidationError

from convmoji.commit_types import possible_commit_types, CommitType


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
