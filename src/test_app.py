import unittest
from src.app import app


# def test_health():
#     client = app.test_client()
#     response = client.get("/health")
#     assert response.data == b"OK"  # nosec B101


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"OK Super", response.data)

if __name__ == "__main__":
    unittest.main()
