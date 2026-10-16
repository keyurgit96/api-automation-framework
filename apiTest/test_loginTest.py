import pytest


@pytest.mark.correctlogin
@pytest.mark.smoke
def test_login(login_client, read_test_data):
    response = login_client.login(read_test_data['CorrectCreds'])
    assert response.status_code == 200


@pytest.mark.incorrectlogin
def test_Incorrect_login(login_client, read_test_data):
    response = login_client.login(read_test_data['IncorrectCreds'])
    assert response.status_code == 400


@pytest.mark.nousername
def test_nousername(login_client, read_test_data):
    response = login_client.login(read_test_data['NoUserName'])
    assert response.status_code == 400


@pytest.mark.nopassword
@pytest.mark.smoke
def test_nopassword(login_client, read_test_data):
    response = login_client.login(read_test_data['NoPassword'])
    assert response.status_code == 400


@pytest.mark.correcttoken
def test_correcttoken(login_client, token_auth):
    response = login_client.getProfile(token=token_auth)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "username" in data
    assert data["username"] == "emilys"


@pytest.mark.incorrecttoken
def test_incorrecttoken(login_client):
    response = login_client.getProfile(token="")
    assert response.status_code == 401
    data = response.json()
    assert "Invalid/Expired" in data["message"]