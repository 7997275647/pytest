import Source.service as service
import pytest
import unittest.mock as mock
import requests
@mock.patch("Source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "MockedSandy"
    user_name = service.get_user_from_db(2)

    assert user_name == "MockedSandy"


"""Mocking :
            create a patch mock.patch and give path to actual function to be mocked.
            Then give a return value to the mock.
            call user_name with actual function.
            

"""
@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Sandy Reddy"}
    mock_get.return_value = mock_response
    data = service.get_users()

    assert data == {"id": 1, "name": "Sandy Reddy"}

@mock.patch("requests.get")
def test_get_users_Error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        service.get_users()


