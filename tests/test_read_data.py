from unittest import mock

import pytest
from read_data import DataReader


@mock.patch("read_data.json.load")
@mock.patch("read_data.open")
def test_read_users_correct_data(mock_open, mock_json_load):
    mock_data_reader = DataReader("", "")
    mock_json_load.return_value = dict({"the_data": "This is real data"})
    result = mock_data_reader.read_users()

    assert result == {"the_data": "This is real data"}


@mock.patch("read_data.json.load")
@mock.patch("read_data.open")
def test_read_companies_correct_data(mock_open, mock_json_load):
    mock_data_reader = DataReader("", "")
    mock_json_load.return_value = dict({"the_data": "This is real data"})
    result = mock_data_reader.read_companies()

    assert result == {"the_data": "This is real data"}
