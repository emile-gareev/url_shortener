from abc import ABC, abstractmethod
from collections import OrderedDict
from typing import Optional


class URLStorage(ABC):
    @abstractmethod
    def save(self, short_url: str, original_url: str):
        ...

    @abstractmethod
    def retrieve(self, short_url: str) -> str:
        ...


class InMemoryStorage(URLStorage):
    """Class for data store into memory."""
    def __init__(self):
        self.storage = OrderedDict()  # Use OrderedDict for ordering of input
        self.limit = 100  # Limit of URLs

    def save(self, short_url: str, original_url: str):
        """Save into the memory."""
        if short_url not in self.storage:
            if len(self.storage) >= self.limit:
                self.storage.popitem(last=False)  # del the oldest element
        self.storage[short_url] = original_url

    def retrieve(self, short_url: str) -> Optional[str]:
        """Reading original url from memory."""
        return self.storage.get(short_url)
