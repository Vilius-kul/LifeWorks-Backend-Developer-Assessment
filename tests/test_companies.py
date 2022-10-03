import pytest
from companies import Companies


def test_user_with_company_field_correct_data() -> None:
    mock_company = Companies([{}], [{}])
    user = {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company_id": 555,
    }
    companies = {
        "555": {
            "id": 555,
            "name": "Head Journal",
            "headquarters": "San Francisco",
            "industry": "Tech",
        }
    }
    result = mock_company._user_with_company_field(user, companies)
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


def test_user_without_company_field() -> None:
    mock_company = Companies([{}], [{}])

    user = {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
    }
    companies = {
        "555": {
            "id": 555,
            "name": "Head Journal",
            "headquarters": "San Francisco",
            "industry": "Tech",
        }
    }

    with pytest.raises(Exception) as ex:
        result = mock_company._user_with_company_field(user, companies)

    assert "'company_id'" == str(ex.value)


def test_user_empty_company_field() -> None:
    mock_company = Companies([{}], [{}])
    user = {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company_id": "",
    }
    companies = {
        "555": {
            "id": 555,
            "name": "Head Journal",
            "headquarters": "San Francisco",
            "industry": "Tech",
        }
    }
    result = mock_company._user_with_company_field(user, companies)
    assert result == {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company": {},
    }


def test_user_company_field_without_companies_data() -> None:
    mock_company = Companies([{}], [{}])
    user = {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company_id": "",
    }
    companies = {}
    result = mock_company._user_with_company_field(user, companies)
    assert result == {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company": {},
    }


def test_user_with_company_field_incorrect_company_id() -> None:
    mock_company = Companies([{}], [{}])
    user = {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company_id": 0,
    }
    companies = {
        "555": {
            "id": 555,
            "name": "Head Journal",
            "headquarters": "San Francisco",
            "industry": "Tech",
        }
    }
    result = mock_company._user_with_company_field(user, companies)
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
