import unittest

from shortener import URLShortener


class TestURLShortener(unittest.TestCase):
    def setUp(self):
        self.shortener = URLShortener()

    def test_shorten_url(self):
        """Check url transform."""
        original_url = "https://example.com"
        short_url = self.shortener.shorten(original_url)
        self.assertNotEqual(original_url, short_url)

    def test_retrieve_url(self):
        """Check url reading from memory."""
        original_url = "https://example.com"
        short_url = self.shortener.shorten(original_url)
        retrieved_url = self.shortener.retrieve(short_url)
        self.assertEqual(original_url, retrieved_url)


if __name__ == "__main__":
    unittest.main()
