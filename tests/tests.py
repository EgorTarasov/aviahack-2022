from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()