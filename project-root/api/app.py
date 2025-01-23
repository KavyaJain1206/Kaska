from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os
from modules.ocr_engine import extract_text_from_image
from modules.exporter import export_text

app = FastAPI()

# Folder paths
raw_folder = "data/raw"
output_folder = "output"

# Ensure the directories exist
os.makedirs(raw_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

@app.post("/process_image/")
async def process_image(image: UploadFile = File(...), format: str = 'md'):
    """
    Process the image file, extract text using OCR, and save results.
    Args:
        image: Image file uploaded by the user
        format: Desired output format (txt, md, pdf)
    Returns:
        JSON with extracted text and output file path
    """
    
    # Save the uploaded image to the raw folder
    image_path = os.path.join(raw_folder, image.filename)
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Extract text from image using OCR
    extracted_text = extract_text_from_image(image_path)

    # Export the extracted text to the desired format
    output_text_path = os.path.join(output_folder, f"{image.filename}_extracted.{format}")
    export_text(extracted_text, format=format, output_path=output_text_path)

    return {
        "message": "Processing completed",
        "extracted_text": extracted_text,
        "output_text_file": output_text_path
    }

@app.get("/get_file/{filename}")
async def get_file(filename: str):
    """
    Return the exported file (txt, md, or pdf) as a file response.
    """
    file_path = os.path.join(output_folder, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}
