import pytest
from users import Users


def test_add_full_name_with_correct_data(users_correct_data):

    result = users_correct_data.add_full_name()
    assert isinstance(result, list)
    assert len(result) == 2
    assert "full_name" in result[0].keys()
    assert result[0]["full_name"] == "Jane Smith"


def test_add_full_name_with_faulty_data(users_faulty_data):

    result = users_faulty_data.add_full_name()
    assert result[0]["full_name"] == "Jane "
    assert result[1]["full_name"] == " Johnson"
    assert result[2]["full_name"] == "Jane Doe"
    assert result[3]["full_name"] == " "


def test_age_with_correct_data(users_correct_data):

    result = users_correct_data._age({"date_of_birth": "2001/10/12"})
    assert result == 20
