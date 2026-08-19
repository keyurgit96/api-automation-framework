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

@pytest.mark.createPost
def test_createPost(http_client,apiBaseUrl):
    payload={
        "title": "Test Post",
        "body": "Test Body",
        "userId": 1
    }
    response=http_client.post(f"{apiBaseUrl}/posts",json=payload)
    res=response.json()
    assert 'title' in res
    assert response.status_code==200

@pytest.mark.updatePost
def tests_updatePost(http_client,apiBaseUrl):
    payload={
        "title": "New Title",
        "body": "New Body",
        "userId": 1
    }
    response=http_client.put(f"{apiBaseUrl}/posts/1",json=payload)
    res=response.json()
    assert 'Title' in res['title']
    assert response.status_code==200