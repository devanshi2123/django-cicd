from django.test import Client

def test_home_page():
    client = Client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, this is my first Django app!" in response.content
