import pytest
import requests

@pytest.fixture(scope="session")
def basicurl():
    basiculrl="https://jsonplaceholder.typicode.com"
    return basiculrl