import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine.meme_generator import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources"""

    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    quotes = []

    # Iterate over the quote files and process each one
    for f in quote_files:
        if os.path.exists(f):
            # Add quotes from the current file to the quotes list
            quotes.extend(Ingestor.parse(f))
        else:
            print(f"File not found: {f}")

    images_path = "./_data/photos/dog/"

    imgs = [os.path.join(images_path, image) for image in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user-defined meme"""

    image_url = request.form.get("image_url")
    if not image_url:
        abort(400, description="Image URL is required")

    temp_image_path = "./temp_image.jpg"
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(temp_image_path, "wb") as f:
            f.write(response.content)
    else:
        abort(400, description="Failed to download image from provided URL")

    body = request.form.get("body")
    author = request.form.get("author")
    if not body or not author:
        abort(400, description="Body and Author are required")

    path = meme.make_meme(temp_image_path, body, author)

    os.remove(temp_image_path)

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
