from typing import List
from ..ingestor import IngestorInterface
from ..models import QuoteModel
import pandas as pd


class CSVIngestor(IngestorInterface):
    """
    Ingestor for CSV files using pandas.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".csv")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with path: {path}")

        try:
            df = pd.read_csv(path)
            quotes = [
                QuoteModel(body=row["body"], author=row["author"])
                for index, row in df.iterrows()
            ]
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except KeyError as e:
            print(f"Missing expected column: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            quotes = []

        return quotes
