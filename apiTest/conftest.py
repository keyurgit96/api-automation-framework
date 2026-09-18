from pathlib import Path
import json
import pytest
import requests

DATA_FILE = Path(__file__).parent.parent / "data/data.json"
print(DATA_FILE)
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

@pytest.fixture(scope="session")
def read_test_data():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data['Credentials']
    