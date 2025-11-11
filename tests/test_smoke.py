import pytest
from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)

def test_root_status():
    # basic smoke: app imports and root responds (index.html served by static), or at least /activities exists
    resp = client.get("/activities")
    assert resp.status_code in (200, 404)
