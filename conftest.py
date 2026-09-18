import pytest
import json

with open(file="data/data.json",mode="r") as f:
    file_data=json.load(f)

@pytest.fixture(scope="session")
def data():
    return file_data["apiURL"]

@pytest.fixture(scope="session")
def basicurl(data):
    basicurl=data["DummyJsonURL"]
    return basicurl

@pytest.fixture(scope="session")
def apiBaseUrl(data):
    apiBaseUrl=data["JsonPlaceholderURL"]
    return apiBaseUrl

@pytest.fixture(scope='session')
def restApiUrl(data):
    restApiUrl=data["RestfulApiDevURL"]
    return restApiUrl