# Image-to-Text Converter

A web application for extracting visible text (such as annotations, labels, or patient info) from images using image processing and OCR (Tesseract).  
Built with Flask, OpenCV, Pillow, and pytesseract.

---

## Features

- Upload images (PNG, JPG, etc.)
- Automatic image preprocessing for better OCR results
- Extracts and displays text
- Simple, responsive web interface

---

## Installation

### 1. Install Tesseract OCR

**Windows:**  
Download and install from [UB Mannheim’s Tesseract page](https://github.com/UB-Mannheim/tesseract/wiki) (commonly recommended for Windows users).
Default path: `C:\Program Files\Tesseract-OCR`

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

**MacOS:**
```bash
brew install tesseract
```

### 2. Add Tesseract to your System PATH (Windows)

- Open Start Menu → search "Environment Variables" → Edit the system environment variables.
- Click "Environment Variables".
- In "System Variables", select `Path` → Edit → New.
- Add your Tesseract install directory (e.g. `C:\Program Files\Tesseract-OCR`).
- Restart your terminal.

Test installation:
```bash
tesseract -v
```

### 3. Clone and Install Python Dependencies

```bash
git clone https://github.com/shakiliitju/Image-to-Text-Converter
.git
cd Image-to-Text-Converter
pip install flask pillow opencv-python pytesseract
```

---
### 4. Install Python Dependencies

Create a `requirements.txt` file with:
```
flask
pillow
opencv-python
pytesseract
```
Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

1. Make sure Tesseract is installed and the path in `app.py` is correct:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```
2. Start the Flask server:
    ```bash
    python app.py
    ```
3. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)
4. Upload a image and view the extracted text.

---

## Project Structure

```
Image-to-Text-Converter/
│
├── app.py
├── uploads/
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

---

## Notes

- This tool extracts **visible text overlays** from images, not diagnostic scan data.
- For best results, use images with clear, readable text.
- For PDF or DICOM support, convert pages to images before uploading.

---

## License

MIT License

---

## Acknowledgements

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
