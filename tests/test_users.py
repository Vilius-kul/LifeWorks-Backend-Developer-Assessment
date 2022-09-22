import pytest
from users import Users


def test_add_full_name_with_correct_data(dummy_users):
    users = Users(dummy_users)
    result = users.add_full_name()
    assert isinstance(result, list)
    assert len(result) == 2
    assert "full_name" in result[0].keys()
    assert result[0]["full_name"] == "Jane Smith"


def test_add_full_name_with_faulty_data(dummy_users_faulty_data):
    users = Users(dummy_users_faulty_data)
    result = users.add_full_name()
    assert result[0]["full_name"] == "Jane "
    assert result[1]["full_name"] == " Johnson"
    assert result[2]["full_name"] == "Jane Doe"
    assert result[3]["full_name"] == " "
