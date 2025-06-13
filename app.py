from flask import Flask, render_template, request, jsonify
import pytesseract
import cv2
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract-text', methods=['POST'])
def extract_text():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400

        image_file = request.files['image']
        image_bytes = image_file.read()

        # Convert image bytes to numpy array
        np_img = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({'error': 'Could not decode image'}), 400

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Convert to PIL Image
        pil_img = Image.fromarray(gray)

        # OCR
        extracted_text = pytesseract.image_to_string(pil_img)

        return jsonify({'text': extracted_text})

    except Exception as e:
        print("❌ Error:", e)  # <-- Print the actual error
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
