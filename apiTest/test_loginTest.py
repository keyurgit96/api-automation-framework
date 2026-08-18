import pytest

@pytest.mark.correctlogin
@pytest.mark.smoke
def test_login(basicurl,http_client):
    response=http_client.post(basicurl+"/auth/login",json={"username":"emilys","password":"emilyspass"})
    assert response.status_code==200
    

@pytest.mark.incorrectlogin
def test_Incorrect_login(basicurl,http_client):
    response=http_client.post(basicurl+"/auth/login",json={"username":"emilys","password":"Incorrect"})
    assert response.status_code==400
    

@pytest.mark.nousername
def test_nousername(basicurl,http_client):
    response=http_client.post(basicurl+"/auth/login",json={"password":"emilyspass"})
    assert response.status_code==400

@pytest.mark.nopassword
@pytest.mark.smoke
def test_nopassword(basicurl,http_client):
    response=http_client.post(basicurl+"/auth/login",json={"username":"emilys"})
    assert response.status_code==400
    