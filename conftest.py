import pytest

@pytest.fixture(scope="session")
def basicurl():
    basiculrl="https://dummyjson.com"
    return basiculrl

@pytest.fixture(scope="session")
def apiBaseUrl():
    apiBaseUrl= "https://jsonplaceholder.typicode.com"
    return apiBaseUrl