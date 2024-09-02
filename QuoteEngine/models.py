class QuoteModel:
    """
    A class that represents a quote with an author.

    Attributes:
        body (str): The content of the quote.
        author (str): The author of the quote.
    """

    def __init__(self, body: str, author: str) -> None:
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        return f'"{self.body}"- {self.author}'
