from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """
    An abstract base class for ingesting quotes from various file formats.
    """

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determines if the file type can be ingested by this ingestor.

        Args:
            path (str): Path to the file.

        Returns:
            bool: True if the file type can be ingested, False otherwise.
        """
        pass
