import logging
import time
import uuid

import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
TIMEOUT = 10
SUFFIX = uuid.uuid4().hex[:8]

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def user():
    return {
        "id": int(time.time() * 1000),
        "username": f"bcarvajal_{SUFFIX}",
        "firstName": "Byron",
        "lastName": "Carvajal",
        "email": f"bcarvajal_{SUFFIX}@example.com",
        "password": "Test1234",
        "phone": "0991234567",
        "userStatus": 1,
    }


@pytest.fixture(scope="module")
def updated_fields():
    return {
        "firstName": "Byron Andres",
        "email": f"byron_updated_{SUFFIX}@example.com",
    }


def user_url(user):
    return f"{BASE_URL}/user/{user['username']}"


def send(method, url, payload=None):
    logger.info("Request: %s %s | payload: %s", method, url, payload)
    response = requests.request(method, url, json=payload, timeout=TIMEOUT)
    logger.info("Response: %s | body: %s", response.status_code, response.text)
    return response


def test_create_user(user):
    response = send("POST", f"{BASE_URL}/user", user)

    assert response.status_code == 200
    assert response.json()["message"] == str(user["id"])


def test_get_user(user):
    response = send("GET", user_url(user))

    assert response.status_code == 200
    body = response.json()
    assert body["username"] == user["username"]
    assert body["email"] == user["email"]


def test_update_user(user, updated_fields):
    payload = {**user, **updated_fields}
    response = send("PUT", user_url(user), payload)

    assert response.status_code == 200
    assert response.json()["message"] == str(user["id"])


def test_get_updated_user(user, updated_fields):
    response = send("GET", user_url(user))

    assert response.status_code == 200
    body = response.json()
    assert body["firstName"] == updated_fields["firstName"]
    assert body["email"] == updated_fields["email"]


def test_delete_user(user):
    response = send("DELETE", user_url(user))

    assert response.status_code == 200
    assert response.json()["message"] == user["username"]


def test_get_deleted_user_returns_404(user):
    response = send("GET", user_url(user))

    assert response.status_code == 404
    assert response.json()["message"] == "User not found"
