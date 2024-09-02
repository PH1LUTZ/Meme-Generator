from typing import List
from ..ingestor import IngestorInterface
from ..models import QuoteModel
import subprocess
import re


class PDFIngestor(IngestorInterface):
    """
    Ingestor for PDF files using the pdftotext command line tool.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".pdf")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with path: {path}")

        quotes = []
        try:
            result = subprocess.run(
                ["pdftotext", path, "-"], capture_output=True, text=True, check=True
            )
            text = result.stdout

            pattern = r'"(.*?)" - (.*?)\s*(?="|$)'
            matches = re.findall(pattern, text)

            for body, author in matches:
                body, author = body.strip(), author.strip()
                if body and author:
                    quotes.append(QuoteModel(body=body, author=author))

            if not matches:
                print("No valid quotes found in the text.")
        except subprocess.CalledProcessError as e:
            print(f"Error calling pdftotext: {e}")
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return quotes
