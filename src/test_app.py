from src.app import app


# def test_health():
#     client = app.test_client()
#     response = client.get("/health")
#     assert response.data == b"OK"  # nosec B101

def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert b"OK Super" in response.data
