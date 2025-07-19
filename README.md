# Image-to-Text Converter

A modern web application for extracting visible text from images using advanced OCR (Optical Character Recognition) technology. Built with Flask, OpenCV, Pillow, and Tesseract OCR for accurate text extraction from various image formats.

---

## Features

- Upload images in multiple formats (PNG, JPG, JPEG, GIF, BMP, TIFF)
- Automatic image preprocessing with OpenCV for enhanced OCR accuracy
- Advanced text extraction using Tesseract OCR
- Real-time text extraction and display
- Clean, responsive web interface
- Cross-platform compatibility (Windows, Linux, macOS)

---

## Installation

### 1. Install Tesseract OCR

**Windows:**  
Download and install from [UB Mannheim’s Tesseract page](https://github.com/UB-Mannheim/tesseract/wiki) (commonly recommended for Windows users).<br>
Default path: `C:\Program Files\Tesseract-OCR`

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install tesseract-ocr
```

**macOS:**
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

### 3. Clone the Repository and Install Python Dependencies

```bash
git clone https://github.com/shakiliitju/Image-to-Text-Converter.git
cd Image-to-Text-Converter
```

### 4. Install Python Dependencies

Install dependencies using the included requirements.txt file:
```bash
pip install -r requirements.txt
```

The requirements.txt includes:
```
Flask
opencv-python
pytesseract
Pillow
numpy
requests
```

---

## Usage

1. **Configure Tesseract Path**: Make sure Tesseract is installed and the path in `app.py` is correct:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```
    
2. **Start the Flask Application**:
    ```bash
    python app.py
    ```
    
3. **Access the Application**: Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)

4. **Upload and Process**: Select an image file and click upload to extract text from the image.

---

## Project Structure

```
Image-to-Text-Converter/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── LICENSE               # MIT License file
├── README.md            # Project documentation
├── uploads/             # Directory for uploaded images
├── templates/           # HTML templates
│   └── index.html      # Main web interface
└── static/             # Static files (CSS, JS)
    ├── style.css       # Stylesheet
    └── script.js       # JavaScript functionality
```

---

## Troubleshooting

### Common Issues

1. **Tesseract not found error**:
   - Ensure Tesseract is properly installed
   - Verify the path in `app.py` matches your installation
   - Add Tesseract to your system PATH

2. **Poor OCR results**:
   - Use high-resolution images with clear text
   - Ensure good contrast between text and background
   - Try preprocessing the image manually if needed

3. **Flask server not starting**:
   - Check if port 5000 is available
   - Ensure all dependencies are installed
   - Run `pip install -r requirements.txt` again

---

## Notes

- This tool extracts **visible text overlays** from images, not diagnostic scan data
- For optimal results, use high-resolution images with clear, readable text
- Supported image formats: PNG, JPG, JPEG, GIF, BMP, TIFF
- For PDF or DICOM support, convert pages/files to image format before uploading
- The application automatically preprocesses images using OpenCV for better OCR accuracy

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

MIT License

---

## Acknowledgements

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
