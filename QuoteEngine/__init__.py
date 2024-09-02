from typing import List
from .models import QuoteModel
from .ingestors import CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor


class Ingestor:
    """
    Ingestor class to manage the ingestion of quotes from various file types.
    """

    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Determines the appropriate ingestor and parses the file.

        Args:
            path (str): Path to the file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f"No suitable ingestor found for file: {path}")
