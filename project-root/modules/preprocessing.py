import easyocr
import cv2
import numpy as np

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def preprocess_image(image_path):
    """
    Preprocess the image for OCR (Grayscale conversion, resizing, etc.)
    """
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding or noise removal if needed
    _, threshold_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
    
    # Return preprocessed image
    return threshold_image

def extract_text_from_image(image_path):
    """
    Extract text from an image using EasyOCR
    """
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    
    # Use EasyOCR to extract text
    result = reader.readtext(preprocessed_image)
    
    # Combine all the text detected by EasyOCR
    text = " ".join([res[1] for res in result])
    return text
