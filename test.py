import unittest

from lightspeed_x import LightspeedX


class LightspeedXTest(unittest.TestCase):

    def setUp(self):
        self.domain_prefix = "test-store"
        self.personal_token = "12345"
        self.client = LightspeedX(self.personal_token, self.domain_prefix)

    def test_init(self):
        # Test correct initialization
        self.assertEqual(self.client.domain_prefix, self.domain_prefix)
        self.assertEqual(
            self.client._client.headers["Authorization"], f"Bearer {self.personal_token}"
        )

    def test_personal_token_setter(self):
        # Test setting a new personal token
        new_token = "98765"
        self.client.personal_token = new_token

        self.assertEqual(self.client.personal_token, new_token)
        self.assertEqual(
            self.client._client.headers["Authorization"], f"Bearer {new_token}"
        )


if __name__ == "__main__":
    unittest.main()
