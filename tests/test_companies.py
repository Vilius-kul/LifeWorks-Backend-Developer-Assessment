from typing import Any, Dict

import pytest
from companies import Companies


@pytest.fixture(autouse=True)
def base_user() -> Dict[str, Any]:
    return {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
    }


@pytest.fixture(autouse=True)
def base_company() -> Dict[str, Any]:
    return {
        "555": {
            "id": 555,
            "name": "Head Journal",
            "headquarters": "San Francisco",
            "industry": "Tech",
        }
    }


def test_user_with_company_field_correct_data(base_user, base_company) -> None:
    mock_company = Companies([{}], [{}])
    base_user.update(
        {
            "company_id": 555,
        }
    )
    result = mock_company._user_with_company_field(base_user, base_company)
    assert result == {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company": {
            "headquarters": "San Francisco",
            "id": 555,
            "industry": "Tech",
            "name": "Head Journal",
        },
    }


def test_user_without_company_field(base_user, base_company) -> None:
    mock_company = Companies([{}], [{}])
    print(base_user)
    with pytest.raises(KeyError) as ex:

        result = mock_company._user_with_company_field(base_user, base_company)

    assert "'company_id'" == str(ex.value)


def test_user_empty_company_field(base_user, base_company) -> None:
    mock_company = Companies([{}], [{}])
    base_user.update({"company_id": ""})

    result = mock_company._user_with_company_field(base_user, base_company)
    assert result == {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company": {},
    }


def test_user_company_field_without_companies_data(base_user) -> None:
    mock_company = Companies([{}], [{}])
    base_user.update(
        {
            "company_id": 555,
        }
    )
    companies = {}
    result = mock_company._user_with_company_field(base_user, companies)
    assert result == {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company": {},
    }


def test_user_with_company_field_incorrect_company_id(
    base_user, base_company
) -> None:
    mock_company = Companies([{}], [{}])
    base_user.update(
        {
            "company_id": 0,
        }
    )

    result = mock_company._user_with_company_field(base_user, base_company)
    assert result == {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company": {},
    }


def test_add_company_field_correct_data(companies_correct_data) -> None:
    result = companies_correct_data.add_company_field()
    assert result[0]["company"]["id"] == 3
    assert result[1]["company"]["id"] == 1
