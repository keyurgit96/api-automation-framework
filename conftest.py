import pytest
import requests

@pytest.fixture(scope="session")
def basicurl(self):
    basiculrl="https://jsonplaceholder.typicode.com"
    return basiculrl