import os
import random
import argparse
from MemeEngine.meme_generator import MemeEngine
from QuoteEngine import Ingestor, QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote"""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./tmp")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # Use ArgumentParser to parse CLI arguments
    parser = argparse.ArgumentParser(description="Generate a meme image.")

    # Define the arguments that can be passed from the command line
    parser.add_argument("--path", type=str, help="path to an image file")
    parser.add_argument("--body", type=str, help="quote body to add to the image")
    parser.add_argument("--author", type=str, help="quote author to add to the image")

    # Parse the arguments
    args = parser.parse_args()

    # Call the generate_meme function with the parsed arguments
    print(generate_meme(args.path, args.body, args.author))
