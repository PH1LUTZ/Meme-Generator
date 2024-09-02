
# Meme Generation Application

## Overview

This project is a meme generation application that combines quotes with images to create engaging memes. It features modules for extracting quotes from various document formats and a meme generation component that overlays text onto images. The application provides a web interface that allows users to generate custom memes or view randomly created ones.

## Project Structure

### Python Modules and Packages:
- **`app.py`**: Main Flask application script for running the web server and handling routes.
- **`meme.py`**: Script for generating memes either randomly or based on user input via command line.
- **`MemeEngine` Module**:
  - **`meme_generator.py`**: Core logic for generating memes by overlaying text on images.
- **`QuoteEngine` Module**:
  - **`ingestor.py`**: Manages the ingestion of quotes from different file formats.
  - **`models.py`**: Defines the Quote data models.
  - **`ingestors` Submodule**:
    - **`csv_ingestor.py`, `docx_ingestor.py`, `pdf_ingestor.py`, `txt_ingestor.py`**: Specialized ingestors for reading quotes from respective file types.

### Web Interface:
- **`templates`**: Folder containing HTML templates for the web interface, including forms for meme creation and pages for displaying memes.

### Resources:
- **`_data`**: Contains quote files in various formats and directories of images used for meme generation.

## Setting Up and Running the Program

1. **Clone the Repository**:
   The initial project was started from a meme generator starter code available at: [Starter Code Download](https://video.udacity-data.com/topher/2020/February/5e595ebf_meme-generator-starter-code/meme-generator-starter-code.zip). Download and unzip it, or clone directly from the updated repository:
   ```bash
   git clone https://github.com/PH1LUTZ/Meme-Generator
   cd Meme-Generator
   ```

2. **Install Dependencies**:
   Install Python if not already installed and then install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the application using the following command:
   ```bash
   python app.py
   ```
   Navigate to `http://localhost:5000` in your web browser to interact with the application. Additionally, you can generate memes via command line using:
   ```bash
   python meme.py --path "<image_path>" --body "Quote text" --author "Author Name"
   ```

## Module Descriptions and Examples

- **`MemeEngine`**: Creates memes by placing quotes on images.
  - *Example*:
    ```python
    from MemeEngine.meme_generator import MemeEngine
    meme = MemeEngine("./static")
    path = meme.make_meme('path/to/image.jpg', "Sample quote", "Author Name")
    ```

- **`QuoteEngine`**: Extracts and manages quotes from a variety of document types.
  - *Example*:
    ```python
    from QuoteEngine import Ingestor
    quotes = Ingestor.parse('path/to/quotes.docx')
    ```

## Dependencies

- **Python 3.x**: Main programming language used.
- **Flask**: Web framework for creating the web interface.
- **Pillow**: Library for image processing.
- **Requests**: Library for making HTTP requests (used for downloading images).
- **Pandas**: Utilized for handling CSV files in some ingestors.
- **python-docx**: For reading DOCX files.
- **PDFMiner**: For extracting text from PDF files.
