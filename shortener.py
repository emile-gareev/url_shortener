from generator import ShortURLGenerator
from storage import URLStorage, InMemoryStorage


class URLShortener:
    """Class main input/output logic."""
    def __init__(self, storage: URLStorage = InMemoryStorage(), generator: ShortURLGenerator = ShortURLGenerator()):
        self.storage = storage
        self.generator = generator

    def shorten(self, original_url: str) -> str:
        """Short url and save it to memory."""
        short_url = self.generator.generate(original_url)
        self.storage.save(short_url, original_url)
        return short_url

    def retrieve(self, short_url: str) -> str:
        """Return original url from short url."""
        return self.storage.retrieve(short_url)


def main():
    """Example using."""
    url_shortener = URLShortener()

    example_urls = ['https://google.com', 'https://example.com', 'https://example.org', 'https://example.com']

    for example_url in example_urls:
        short_url = url_shortener.shorten(example_url)
        print(f'Short url for {example_url} = {short_url}')
        original_url = url_shortener.retrieve(short_url)
        print(f'Original url for {short_url} = {original_url}')

    nothing = url_shortener.retrieve('99')
    print(nothing)  # None, if limit = 2 into the storage.py


if __name__ == "__main__":
    main()