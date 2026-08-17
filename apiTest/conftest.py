import requests
import pytest

@pytest.fixture(scope="session")
def http_client():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()