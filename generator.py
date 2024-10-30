"""
16^2 = 256
16^3 = 4096
16^4 = 65,536
16^5 = 1,048,576
16^6 = 16,777,216
16^7 = 268,435,456
16^8 = 4,294,967,296
16^9 = 68,719,476,736
"""

import hashlib
import string


class ShortURLGenerator:
    """Class for short url generation (16 symbols include digits and a-f)."""

    # Basic symbols for Base62
    BASE62_ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits

    def encode_base62(self, num):
        """Transformation to base62."""
        if num == 0:
            return self.BASE62_ALPHABET[0]

        base62 = []
        while num > 0:
            num, rem = divmod(num, 62)
            base62.append(self.BASE62_ALPHABET[rem])

        return ''.join(reversed(base62))

    def string_to_base16(self, input_string):
        """Transformation to base16."""
        # transform string to bytes
        byte_array = input_string.encode('utf-8')
        # transform bytes to hex
        base16_string = byte_array.hex()
        return base16_string

    def generate(self, original_url: str) -> str:
        """Short url generation."""
        return hashlib.md5(original_url.encode()).hexdigest()[:2]

        # # Example for base62 + DB
        # input_id = id("https://example.org")  # Random digit id (better from DB)
        # base62_result = self.encode_base62(input_id)
        # return base62_result

        # # Example for base16
        # input_str = "https://example.org"
        # return base16_string[:2]

