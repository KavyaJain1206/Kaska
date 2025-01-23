import easyocr

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    """Extract text from an image using EasyOCR."""
    result = reader.readtext(image_path)

    # Combine all detected text into one string
    text = " ".join([res[1] for res in result])
    return text
