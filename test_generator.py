import unittest

from generator import ShortURLGenerator


class TestShortURLGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ShortURLGenerator()

    def test_generate_url(self):
        """Check of right short url generation."""
        original_url = "https://example.com"
        short_url = self.generator.generate(original_url)
        self.assertEqual(len(short_url), 2)  # when use 2 in generate method


if __name__ == "__main__":
    unittest.main()
