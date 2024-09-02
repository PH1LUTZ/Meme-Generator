from typing import List
from ..ingestor import IngestorInterface
from ..models import QuoteModel
from docx import Document


class DOCXIngestor(IngestorInterface):
    """
    Ingestor for DOCX files.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".docx")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with path: {path}")

        quotes = []
        try:
            doc = Document(path)
            for para in doc.paragraphs:
                text = para.text.strip()
                if "-" in text:
                    body, author = (
                        part.strip().strip('"').strip("'")
                        for part in text.rsplit("-", 1)
                    )
                    quotes.append(QuoteModel(body=body, author=author))
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return quotes
