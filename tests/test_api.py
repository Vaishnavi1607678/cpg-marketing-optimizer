from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_recommendations():

    response = client.get("/recommendations")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert "roi" in data[0]