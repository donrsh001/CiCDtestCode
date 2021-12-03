import pytest
# from werkzeug.wrappers import response
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_contact_page(client):
    response = client.get("/contact")
    assert response.status_code == 200
