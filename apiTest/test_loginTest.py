import pytest

@pytest.mark.login
def test_login(basicurl,http_client):
    response=http_client.post(basicurl,json={"username":"k","password":"k"})
    print( response.status_code)
    print(response.json())