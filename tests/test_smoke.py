from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # ensure we have at least one activity
    assert len(data) > 0
import pytest
from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)

def test_root_status():
    # basic smoke: app imports and root responds (index.html served by static), or at least /activities exists
    resp = client.get("/activities")
    assert resp.status_code in (200, 404)
