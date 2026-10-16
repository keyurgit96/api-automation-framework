import pytest


@pytest.mark.getallpost
def test_getAllPost(post_client):
    res = post_client.getAllPosts()
    assert post_client.response.status_code == 200
    assert 'title' in res[0]


@pytest.mark.getsinglepost
def test_getSinglePost(post_client):
    res = post_client.getPost(1)
    assert post_client.response.status_code == 200
    assert 'title' in res


@pytest.mark.nonExistantPost
def test_nonExistantPost(post_client):
    res = post_client.getPost(9833)
    assert post_client.response.status_code == 404
    assert 'title' not in res


@pytest.mark.createPost
def test_createPost(post_client, post_payloads):
    res = post_client.createPost(post_payloads['CreatePost'])
    assert post_client.response.status_code in [200, 201]
    assert 'title' in res


@pytest.mark.updatePost
def test_updatePost(post_client, post_payloads):
    res = post_client.updatePost(1, post_payloads['UpdatePost'])
    assert post_client.response.status_code == 200
    assert 'Title' in res['title']


@pytest.mark.TestDeletePost
@pytest.mark.testthis
def test_deletePost(post_client):
    res = post_client.deletePost(1)
    assert post_client.response.status_code == 200
    assert 'title' not in res


@pytest.mark.test_patch_post
@pytest.mark.testthis
def test_patchPost(post_client, post_payloads):
    res = post_client.patchPost(1, post_payloads['PatchPost'])
    assert post_client.response.status_code == 200
    assert 'Patched' in res['title']