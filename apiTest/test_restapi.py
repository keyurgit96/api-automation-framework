import pytest


@pytest.mark.getuser
def test_GetAllUser(user_client):
    res = user_client.getAllUsers()
    res = res.json()
    assert res.status_code == 200
    assert isinstance(res, list)


@pytest.mark.create_delete_user
def test_createUser(user_client, user_payloads):
    # Create user/object using payload from data.json
    res = user_client.createUser(user_payloads['CreateUser'])
    assert res.status_code == 200
    res = res.json()
    assert 'id' in res
    assert res['name'] == 'New User'
    user_id = res['id']

    # Patch user/object using payload from data.json
    patch_res = user_client.patchUser(user_id, user_payloads['PatchUser'])
    assert patch_res.status_code == 200
    assert 'name' in patch_res
    assert patch_res['name'] == 'Patched User'

    # Delete user/object
    del_res = user_client.deleteUser(user_id)
    assert user_client.response.status_code == 200