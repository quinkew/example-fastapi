import pytest
from server import schemas
from jose import jwt
from server.core.config import settings


def test_create_user(client):
    res = client.post('/users/', json={'email':'testclient@gmail.com', 'password':'test'})
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'testclient@gmail.com'
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post('/login', data={'username':test_user['email'], 'password':test_user['password']})
    print(res.json())
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get('user_id')
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200


@pytest.mark.parametrize('username, password, status_code', [
    ('wrongemail@gmail.com', 'test', 403),
    ('testclient', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'test', 403),
    (None, 'test', 422),
    ('testclient@gmail.com', None, 422)
])
def test_incorrect_login(client, username, password, status_code):
    res = client.post('/login', data={'username': username,
                                       'password': password})
    assert res.status_code == status_code
