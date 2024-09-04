
# PDF to Audio Converter

This is a web-based application that allows users to upload a PDF file, convert its text to speech, and download an MP3 file. The application is built using Flask, pdfplumber for PDF text extraction, and gTTS (Google Text-to-Speech) for converting text to audio.

## Features
- Upload any PDF file.
- Convert the text within the PDF to an MP3 audio file.
- Play and download the audio directly from the web interface.
- Supports multiple pages of PDFs.
- Clean and responsive user interface.

## Requirements

- Python 3.x
- Flask
- pdfplumber
- gTTS

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repository-url
   ```

2. Navigate to the project directory:

   ```bash
   cd pdf_to_audio
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Upload a PDF file, and the application will convert it to audio. Once the conversion is done, you can play or download the MP3 file.

## Configuration

By default, the application supports PDFs up to 16 MB. You can modify the size limit by changing the `MAX_CONTENT_LENGTH` in the `app.py` file:

```python
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB
```

## Folder Structure

```
pdf_to_audio/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # HTML file for the web interface
├── static/
│   └── uploads/         # Folder where PDFs and MP3s are saved
└── README.md            # This file
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
