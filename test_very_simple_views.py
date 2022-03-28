from django.http import HttpResponse


def test_one_plus_one_is_two():
    x = 1 + 1
    assert x == 2


def test_one_plus_one_is_three():
    x = 1 + 1
    assert x == 3


def test_home(client):
    r: HttpResponse = client.get("")
    assert r.status_code == 200
    assert r.content.decode() == 'Hello <b>world</b>!!!'



