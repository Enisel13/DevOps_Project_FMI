from src.app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.data == b"OK"  # nosec B101
