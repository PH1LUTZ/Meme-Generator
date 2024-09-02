from typing import List
from ..ingestor import IngestorInterface
from ..models import QuoteModel


class TXTIngestor(IngestorInterface):
    """
    Ingestor for TXT files.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".txt")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with path: {path}")

        quotes = []
        try:
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    if "-" in line:
                        body, author = line.rsplit("-", 1)
                        body, author = body.strip().strip('"'), author.strip()
                        quotes.append(QuoteModel(body=body, author=author))
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return quotes
