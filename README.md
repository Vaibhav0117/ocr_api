# OCR API using FastAPI and Tesseract

This project is a simple Optical Character Recognition (OCR) API built using **FastAPI** and **Tesseract OCR**.

## 🔍 What it does

- Accepts an image file via POST request.
- Extracts text and bounding box data using Tesseract.
- Returns a structured JSON response with the text and its position in the image.

## 🛠 Requirements

- Python 3.8+
- Tesseract OCR installed on your system
- pip packages from `requirements.txt`

## 🚀 How to Run

1. **Install Tesseract OCR**  
   Download from: https://github.com/tesseract-ocr/tesseract  
   Make sure the path to `tesseract.exe` is correctly set in your code.

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run the API**
    uvicorn main:app --reload

4. **Test the endpoint**
    Go to: http://127.0.0.1:8000/docs
    Upload an image and test the /ocr endpoint.