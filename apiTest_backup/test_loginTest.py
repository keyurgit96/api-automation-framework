import pytest

@pytest.mark.correctlogin
@pytest.mark.smoke
def test_login(basicurl,http_client,read_test_data):
    response=http_client.post(basicurl+"/auth/login",json=read_test_data['CorrectCreds'])
    assert response.status_code==200
    

@pytest.mark.incorrectlogin
def test_Incorrect_login(basicurl,http_client,read_test_data):
    response=http_client.post(basicurl+"/auth/login",json=read_test_data['IncorrectCreds'])
    assert response.status_code==400
    

@pytest.mark.nousername
def test_nousername(basicurl,http_client,read_test_data):
    response=http_client.post(basicurl+"/auth/login",json=read_test_data['NoUserName'])
    assert response.status_code==400

@pytest.mark.nopassword
@pytest.mark.smoke
def test_nopassword(basicurl,http_client,read_test_data):
    response=http_client.post(basicurl+"/auth/login",json=read_test_data['NoPassword'])
    assert response.status_code==400
    
@pytest.mark.correcttoken
def test_correcttoken(http_client,token_auth,basicurl):
    response=http_client.get(basicurl+"/auth/me",headers={"Authorization":f"Bearer {token_auth}"})
    assert response.status_code==200
    data=response.json()
    assert "id" in data
    assert "username" in data
    assert data["username"]=="emilys"

@pytest.mark.incorrecttoken
def test_incorrecttoken(http_client,token_auth,basicurl):
    response=http_client.get(basicurl+"/auth/me",headers={"Authorization":f"Bearer "})
    assert response.status_code==401
    data=response.json()
    assert "Invalid/Expired" in data["message"]
