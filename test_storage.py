import unittest

from storage import InMemoryStorage


class TestInMemoryStorage(unittest.TestCase):

    def setUp(self):
        self.storage = InMemoryStorage()

    def test_save_and_retrieve(self):
        """Check saving and reading url."""
        short_url = "abc12345"
        original_url = "https://example.com"
        self.storage.save(short_url, original_url)
        retrieved_url = self.storage.retrieve(short_url)
        self.assertEqual(original_url, retrieved_url)

    def test_retrieve_nonexistent(self):
        """Check url exists."""
        retrieved_url = self.storage.retrieve("nonexistent")
        self.assertIsNone(retrieved_url)

    def test_limit_of_urls(self):
        """Check overflow of storage."""
        # Add 101 URL
        for i in range(101):
            short_url = f"short{i:03d}"
            original_url = f"https://example.com/page{i}"
            self.storage.save(short_url, original_url)

        retrieved_url = self.storage.retrieve("short000")
        self.assertIsNone(retrieved_url)
        retrieved_url = self.storage.retrieve("short100")
        self.assertEqual(retrieved_url, "https://example.com/page100")


if __name__ == "__main__":
    unittest.main()
