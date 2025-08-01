from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\choug\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

app = FastAPI()

@app.post("/ocr")
async def perform_ocr(file: UploadFile = File(...)):
    # Read uploaded image
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))

    # Run Tesseract OCR to get text with bounding box data
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    results = []
    for i in range(len(data['text'])):
        text = data['text'][i].strip()
        if text:
            bbox = [
                data['left'][i],
                data['top'][i],
                data['left'][i] + data['width'][i],
                data['top'][i] + data['height'][i]
            ]
            results.append({
                "text": text,
                "bbox": bbox
            })

    return JSONResponse(content=results)
