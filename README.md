# 🧾 OCR Text Extractor

A simple web app that extracts text from images using Python, Flask, Tesseract OCR, and OpenCV. Just upload an image and extract text with one click.

🚀 Features

📤 Upload image via web interface

🌈 Automatic grayscale conversion for better accuracy

🧠 Text extraction using Tesseract OCR

⚡ Fast and minimal Flask backend

🎨 Clean UI with HTML, CSS, and JS

📁 Project Structure

ocr-text-extractor/
├── app.py
├── static/
│   ├── styles.css
│   └── script.js
├── templates/
│   └── index.html
└── README.md

⚙️ Installation & Setup

✅ 1. Clone the Repository

git clone https://github.com/your-username/ocr-text-extractor.git
cd ocr-text-extractor

✅ 2. Install Python Dependencies

Make sure you have Python 3.8+ installed.

pip install flask opencv-python pillow pytesseract

✅ 3. Install Tesseract OCR Engine

🔗 Download for Windows:
https://github.com/UB-Mannheim/tesseract/wiki

Install it to: C:\Program Files\Tesseract-OCR

Then add it to your System Environment Variables (PATH).
OR explicitly set the path in app.py:

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

To verify installation:

tesseract --version

▶️ Run the App

python app.py

Open your browser and visit:

http://127.0.0.1:5000

Upload an image and click "Extract Text" to see the results!

📷 Sample Usage

Upload an image containing printed or handwritten text.
The app converts it to grayscale (for better OCR).
Extracted text is shown instantly on the same page.
