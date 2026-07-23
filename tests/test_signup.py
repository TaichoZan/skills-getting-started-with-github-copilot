from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    register_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    assert register_response.status_code == 200

    unregister_response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    assert unregister_response.status_code == 200

    payload = unregister_response.json()
    assert "Unregistered" in payload["message"]

    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]
