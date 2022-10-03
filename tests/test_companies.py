import pytest


def test_user_with_company_field_correct_data(companies_correct_data):

    user = {"company_id": 555}
    companies = {
        "555": {
            "id": 555,
            "name": "Head Journal",
            "headquarters": "San Francisco",
            "industry": "Tech",
        }
    }
    result = companies_correct_data._user_with_company_field(user, companies)
    assert result == {
        "company": {
            "headquarters": "San Francisco",
            "id": 555,
            "industry": "Tech",
            "name": "Head Journal",
        }
    }


# def test_user_with_company_field_faulty_data():
#     pass


def test_add_company_field_correct_data(companies_correct_data):
    result = companies_correct_data.add_company_field()
    assert result[0]["company"]["id"] == 3
    assert result[1]["company"]["id"] == 1


# def test_add_company_field_faulty_data():
#     pass
