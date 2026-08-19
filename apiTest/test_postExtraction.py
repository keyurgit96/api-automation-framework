import requests
import pytest

@pytest.mark.getallpost
def test_getAllPost(http_client,apiBaseUrl):
    response=http_client.get(apiBaseUrl+'/posts')
    res=response.json()
    assert 'title' in res[0]
    assert response.status_code==200

@pytest.mark.getsinglepost
def test_getSinglePost(http_client,apiBaseUrl):
    response=http_client.get(apiBaseUrl+'/posts/1')
    res=response.json()
    assert 'title' in res
    assert response.status_code==200

@pytest.mark.nonExistantPost
def test_nonExistantPost(http_client,apiBaseUrl):
    response=http_client.get(apiBaseUrl+'/posts/9833')
    res=response.json()
    assert 'title' not in res
    assert response.status_code==404