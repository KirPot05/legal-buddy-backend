from google.api_core.client_options import ClientOptions
from google.cloud import documentai  # type: ignore


def extract_text_from_document(file_path: str, mime_type: str = "application/pdf") -> str:
    project_id = "centering-force-431907-n6"
    location = "us"
    processor_id = "b57c0b82b05c45d3"

    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    with open(file_path, "rb") as image:
        image_content = image.read()

    # Load binary data
    raw_document = documentai.RawDocument(
        content=image_content,
        mime_type=mime_type,
    )

    processor_name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    request = documentai.ProcessRequest(
        name=processor_name, raw_document=raw_document)

    result = client.process_document(request=request)

    document = result.document

    return document.text
