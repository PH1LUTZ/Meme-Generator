from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeEngine:
    """
    A class dedicated to generating meme images by superimposing text on original images.
    It allows customization of text color, shadow effects, and font choices.
    """

    # Default styling constants
    DEFAULT_TEXT_COLOR = "white"
    DEFAULT_SHADOW_COLOR = "black"
    DEFAULT_SHADOW_OFFSET = (3, 3)  # Shadow offset in pixels for visual depth
    DEFAULT_QUOTE_FONT = "./_data/fonts/impact.ttf"  # Path to font for quotes
    DEFAULT_AUTHOR_FONT = "./_data/fonts/comic.ttf"  # Path to font for author

    def __init__(self, output_dir):
        """
        Initialize the Generator with an output directory.

        Parameters:
            output_dir (str): Directory where the generated memes will be saved.
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Generates a meme image with text and an author signature.

        Parameters:
            img_path (str): Path to the input image.
            text (str): Quote text to add to the image.
            author (str): Author of the quote.
            width (int): Desired width of the output image while maintaining aspect ratio.

        Returns:
            str: Path to the saved image or None if an error occurs.
        """
        try:
            # Load and conditionally resize the image
            img = Image.open(img_path)
            img_width, img_height = img.size
            if img_width > width:
                # Scale down the image to the specified width while maintaining aspect ratio
                height = img_height * width // img_width
                img = img.resize((width, height), Image.Resampling.LANCZOS)
                img_width, img_height = img.size

            draw = ImageDraw.Draw(img)

            # Dynamically set font sizes based on image width
            QUOTE_FONT_SIZE = img_width // 16
            AUTHOR_FONT_SIZE = img_width // 20

            quote_font = ImageFont.truetype(self.DEFAULT_QUOTE_FONT, QUOTE_FONT_SIZE)
            author_font = ImageFont.truetype(self.DEFAULT_AUTHOR_FONT, AUTHOR_FONT_SIZE)

            # Calculate text positioning
            quote_line, author_line = f'"{text}"', f"- {author}"
            quote_bbox = draw.textbbox((0, 0), quote_line, font=quote_font)
            author_bbox = draw.textbbox((0, 0), author_line, font=author_font)
            quote_hight = quote_bbox[3] - quote_bbox[1]
            author_hight = author_bbox[3] - author_bbox[1]
            text_height = quote_hight + author_hight

            # Randomize vertical position for the text
            text_y = random.randint(20, img_height - text_height - 20)

            # Draw the quote text with shadow
            self.draw_text(
                draw,
                quote_line,
                quote_font,
                img_width,
                text_y,
                self.DEFAULT_TEXT_COLOR,
                self.DEFAULT_SHADOW_COLOR,
            )

            # Adjust position for author text
            text_y += quote_hight

            # Draw the author text with shadow
            self.draw_text(
                draw,
                author_line,
                author_font,
                img_width,
                text_y,
                self.DEFAULT_TEXT_COLOR,
                self.DEFAULT_SHADOW_COLOR,
            )

            # Ensure the output directory exists
            os.makedirs(self.output_dir, exist_ok=True)

            # Prepare to save the generated meme
            img_name = f"meme_{os.path.basename(img_path)}"

            # Save the newly created meme to the output directory
            output_path = os.path.join(self.output_dir, img_name)
            img.save(output_path)

            return output_path
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def draw_text(self, draw, text, font, img_width, text_y, text_color, shadow_color):
        """
        Helper method to draw text with a shadow effect.

        Parameters:
            draw (ImageDraw.Draw): The drawing context.
            text (str): Text to draw.
            font (ImageFont): Font for the text.
            img_width (int): Width of the image to center the text horizontally.
            text_y (int): Vertical position for the text.
            text_color (str): Color for the text.
            shadow_color (str): Color for the text shadow.
        """
        # Compute text positioning for centered alignment
        bbox = draw.textbbox((0, 0), text, font=font)
        text_x = (img_width - bbox[2]) // 2
        shadow_x = text_x + self.DEFAULT_SHADOW_OFFSET[0]
        shadow_y = text_y + self.DEFAULT_SHADOW_OFFSET[1]

        # Draw shadow first, then the text for a clear, readable appearance
        draw.text((shadow_x, shadow_y), text, fill=shadow_color, font=font)
        draw.text((text_x, text_y), text, fill=text_color, font=font)
