from flask import Flask, request, render_template, jsonify
import os
import pytesseract
from PIL import Image
import cv2

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update if needed

def preprocess_ct_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read image file.")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    temp_path = os.path.join(UPLOAD_FOLDER, 'processed_ct.png')
    cv2.imwrite(temp_path, binary)
    return temp_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'extracted_text': 'No file uploaded'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'extracted_text': 'No file selected'}), 400
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        if not os.path.exists(filepath):
            return jsonify({'extracted_text': 'File not saved properly'}), 500
        processed_path = preprocess_ct_image(filepath)
        text = pytesseract.image_to_string(Image.open(processed_path), lang='eng')
        if not text.strip():
            return jsonify({'extracted_text': 'No text found in image'}), 200
        return jsonify({'extracted_text': text.strip()})
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({'extracted_text': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
