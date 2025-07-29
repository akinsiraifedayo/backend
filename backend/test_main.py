from fastapi.testclient import TestClient
import pytest
from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bank API Service"}

def test_ping_pass():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"pong": True}

@pytest.mark.skip(reason="This test is temporarily skipped")
def test_ping_fail():
    response = client.get("/ping")
    assert response.status_code == 200
    # Intentionally failing test to verify GitHub Actions Works
    assert response.json() == {"pong": False}
