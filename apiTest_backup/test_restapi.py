import pytest

@pytest.mark.getuser
def test_GetAllUser(http_client, restApiUrl):
    response = http_client.get(f"{restApiUrl}objects")
    assert response.status_code==200

@pytest.mark.create_delete_user
def test_createUser(http_client,restApiUrl):
    payload={
        "name": "New User",
        "salary": "12300",
        "age": "30"
    }
    response=http_client.post(f"{restApiUrl}objects",json=payload)
    assert response.status_code==200
    res=response.json()
    id=res['id']
    assert 'id' in res
    assert res['name']=='New User'

    payload={
        "name": "Patched User"
    }
    
    response=http_client.patch(f"{restApiUrl}objects/{id}", json=payload)
    assert response.status_code==200
    res=response.json()
    assert 'name' in res
    assert res['name']=='Patched User'
    print(res['name'])
    delresponse=http_client.delete(f"{restApiUrl}objects/{id}")
    assert delresponse.status_code==200
