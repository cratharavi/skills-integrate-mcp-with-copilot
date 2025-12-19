import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from src.app import app
from src.db import DB_FILE

client = TestClient(app)


def test_seed_and_signup_persists(tmp_path):
    # Ensure DB file exists after app startup
    assert DB_FILE.exists()

    # pick an activity and sign up a new student
    activity = "Chess Club"
    email = "tester@example.com"

    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert "Signed up" in resp.json().get("message", "")

    # Verify participant appears in activity listing
    resp2 = client.get("/activities")
    assert resp2.status_code == 200
    data = resp2.json()
    assert email in data[activity]["participants"]

    # Unregister and ensure removed
    resp3 = client.delete(f"/activities/{activity}/unregister", params={"email": email})
    assert resp3.status_code == 200
    resp4 = client.get("/activities")
    data2 = resp4.json()
    assert email not in data2[activity]["participants"]
