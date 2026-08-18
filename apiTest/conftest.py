import requests
import pytest

@pytest.fixture(scope="session")
def http_client():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()

@pytest.fixture(scope='session')
def token_auth(http_client,basicurl):
    response=http_client.post(basicurl+"/auth/login",json={"username":"emilys","password":"emilyspass"})
    assert response.status_code==200
    return response.json()["accessToken"]