from google.cloud import vision


vision_client = vision.ImageAnnotatorClient()


def extract_text_from_image(file_path):
    with open(file_path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = vision_client.document_text_detection(image=image)
    if response.error.message:
        raise Exception(response.error.message)
    return response.full_text_annotation.text
