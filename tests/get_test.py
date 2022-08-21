from unittest import TestCase, result
from fastapi.testclient import TestClient
from fast_api_sample.main import app

client = TestClient(app)

class SuccessTests(TestCase):
    def test_create_item(self) -> None:
        expected_body = {"message": "Hello World"}
        response = client.get("/items/")
        assert response.status_code == 200
        result = response.json()
        assert result == expected_body