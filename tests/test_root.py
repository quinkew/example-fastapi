def test_root(client):
    res = client.get('/')
    print(res.json().get('message'))
    assert res.json().get('message') == 'some changes for you'
    assert res.status_code == 200