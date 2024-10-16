import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    req = client.get("http://localhost:8080")
    print(req.text)
    assert req.status_code == 200
    assert req.json() == {"message": "hello World"}

if __name__ == '__main__':
    pytest.main(["-vvs"])
    # test_root()
