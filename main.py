import cv2
import os
import PyPDF2
from pdf2image import convert_from_path
from pyzbar import pyzbar


def save_image(image, image_path):
    try:
        image.save(image_path, "JPEG")
    except cv2.error as e:
        print(f"Error during saving image - {image_path}: {e}")


def convert_pdf_to_jpg(pdf_file_path, dirname):
    images = convert_from_path(pdf_file_path)
    image_path = os.path.join(dirname, "image.jpg")
    save_image(images[0], image_path)
    return image_path


def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text


def extract_barcodes_from_image(image):
    barcodes_data = []
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        bdata = barcode.data.decode("utf-8")
        barcodes_data.append(bdata)
    return barcodes_data


def extract_barcodes_from_pdf(pdf_file_path, dirname):
    image_path = convert_pdf_to_jpg(pdf_file_path, dirname)
    image = cv2.imread(image_path)
    barcodes_data = extract_barcodes_from_image(image)
    try:
        os.remove(image_path)
    except OSError as e:
        print(f"Error during deleting image - {image_path}: {e}")
    return barcodes_data


def extract_data_from_pdf(pdf_file_path, dirname):
    text = extract_text_from_pdf(pdf_file_path)
    barcodes = extract_barcodes_from_pdf(pdf_file_path, dirname)
    data = {"text": text, "barcodes": barcodes}
    return data


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    pdf_file_path = "test_task.pdf"
    extracted_data = extract_data_from_pdf(pdf_file_path, dirname)
    print(extracted_data)
