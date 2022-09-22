import pytest
from users import Users


def test_add_full_name_with_correct_data(dummy_users):
    users = Users(dummy_users)
    result = users.add_full_name()
    assert isinstance(result, list)
    assert len(result) == 2
    assert "full_name" in result[0].keys()
    assert result[0]["full_name"] == "Jane Smith"
