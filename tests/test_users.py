import pytest
from users import Users


def test_add_full_name_with_correct_data(users_correct_data) -> None:
    result = users_correct_data.add_full_name()

    assert isinstance(result, list)
    assert len(result) == 2
    assert "full_name" in result[0].keys()
    assert result[0]["full_name"] == "Jane Smith"


def test_add_full_name_with_faulty_data(users_faulty_data) -> None:
    result = users_faulty_data.add_full_name()

    assert result[0]["full_name"] == "Jane "
    assert result[1]["full_name"] == " Johnson"
    assert result[2]["full_name"] == "Jane Doe"
    assert result[3]["full_name"] == " "


def test_age_with_correct_data() -> None:
    correct_dob = {"date_of_birth": "2001/10/12"}
    result = Users._age(correct_dob)
    assert result == 20


def test_age_with_faulty_data() -> None:
    incorrect_data = {"date_of_birth": ""}
    with pytest.raises(ValueError) as ve:
        Users._age(incorrect_data)
    assert "time data '' does not match format '%Y/%m/%d'" in str(ve.value)


def test_thirty_and_over_with_correct_data(users_correct_data) -> None:
    result = users_correct_data.thirty_and_over()
    for user in result:
        assert Users._age(user) >= 30


def test_thirty_and_over_with_incorrect_data(users_faulty_data) -> None:
    result = users_faulty_data.thirty_and_over()
    assert result == []
