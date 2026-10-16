from pathlib import Path
import json
import pytest
import requests
from src.apiClient.authentication import loginAPI
from src.apiClient.postHandling import postAPI
from src.apiClient.userHandling import userAPI

DATA_FILE = Path(__file__).parent.parent / "data/data.json"


@pytest.fixture(scope="session")
def http_client():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()


@pytest.fixture(scope="session")
def raw_test_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def api_urls(raw_test_data):
    return raw_test_data.get("apiURL", {})


@pytest.fixture(scope="session")
def basicurl(api_urls):
    return api_urls.get("DummyJsonURL")


@pytest.fixture(scope="session")
def apiBaseUrl(api_urls):
    return api_urls.get("JsonPlaceholderURL")


@pytest.fixture(scope="session")
def restApiUrl(api_urls):
    return api_urls.get("RestfulApiDevURL")


@pytest.fixture(scope="session")
def read_test_data(raw_test_data):
    return raw_test_data.get("Credentials", raw_test_data.get("CredentialsAPI", {}))


@pytest.fixture(scope="session")
def post_payloads(raw_test_data):
    return raw_test_data.get("PostPayloads", {})


@pytest.fixture(scope="session")
def user_payloads(raw_test_data):
    return raw_test_data.get("UserPayloads", {})


@pytest.fixture(scope="session")
def login_client(basicurl, http_client):
    return loginAPI(baseURL=basicurl, session=http_client)


@pytest.fixture(scope="session")
def post_client(apiBaseUrl, http_client):
    return postAPI(baseURL=apiBaseUrl, session=http_client)


@pytest.fixture(scope="session")
def user_client(restApiUrl, http_client):
    return userAPI(baseURL=restApiUrl, session=http_client)


@pytest.fixture(scope="session")
def token_auth(login_client, read_test_data):
    response = login_client.login(read_test_data['CorrectCreds'])
    assert response.status_code == 200
    return response.json()["accessToken"]