import pytest

@pytest.fixture(scope="session")
def basicurl():
    basiculrl="https://dummyjson.com"
    return basiculrl

@pytest.fixture(scope="session")
def apiBaseUrl():
    apiBaseUrl= "https://jsonplaceholder.typicode.com"
    return apiBaseUrl

@pytest.fixture(scope='session')
def restApiUrl():
    return "https://api.restful-api.dev/"