import pytest
import requests

@pytest.fixture(scope="session")
def basicurl():
    basiculrl="https://dummyjson.com"
    return basiculrl

@pytest.fixture(scope="session")
def apiBaseUrl():
    return "https://jsonplaceholder.typicode.com"