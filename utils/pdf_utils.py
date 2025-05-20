import base64
import io

import pdf2image
from PIL import Image


def pdf_to_base64_images(uploaded_file):
    """
    Convert the first page of a PDF file to a base64-encoded JPEG image.
    Returns a list of dicts with keys 'mime_type' and 'data'.
    """
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded") 