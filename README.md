# Legal Document Summarizer

The **Legal Document Summarizer** is a Python-based application that allows users to upload documents (PDFs or images) in English or Kannada. The application uses OCR technology to extract text from the documents, generates summaries using advanced AI models, and translates the summaries into English and Kannada. The application stores the results in a MongoDB database and a Pinecone vector store for future retrieval and similarity-based queries.

---

## Features

- **Document Upload**: Supports PDF and image file formats (JPEG, PNG).
- **OCR Processing**: Extracts text using Google Cloud Vision API or Document AI.
- **Summarization**: Generates concise summaries using Gemini 1.5 Pro.
- **Translation**: Translates summaries into English and Kannada using Google Cloud Translate API.
- **Data Storage**:
  - Stores extracted text and summaries in MongoDB.
  - Stores summary vectors and metadata in Pinecone for efficient similarity-based searches.
- **API Endpoints**: Exposes RESTful endpoints for document upload and summary retrieval.

---

## Tech Stack

- **Programming Language**: Python
- **Framework**: FastAPI
- **APIs**:
  - Google Cloud Vision API / Document AI for OCR
  - Google Cloud Translate API for translation
- **Database**: MongoDB
- **Vector Store**: Pinecone
- **AI Models**: SentenceTransformer for embeddings
- **Containerization**: Docker (optional)

---

## Prerequisites

- Python 3.8 or later
- MongoDB instance (local or hosted)
- Google Cloud account with Vision, Translate, and Document AI APIs enabled
- Pinecone account with API key and environment details
- `pip` for package management
- Poppler (for PDF processing with `pdf2image`)

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-repo/legal-document-summarizer.git
cd legal-document-summarizer
```

### Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory with the following variables:

```plaintext
MONGO_URI=mongodb://localhost:27017
GCP_VISION_CREDENTIALS=/path/to/your/gcp/credentials.json
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENVIRONMENT=your-pinecone-environment
```

---

## Usage

### Start the Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### API Endpoints

#### **Upload Document**

- **POST /upload**
- Request:
  - Form data with file upload (PDF or image)
- Response:
  ```json
  {
    "summary_english": "Summary in English...",
    "summary_kannada": "Summary in Kannada...",
    "timestamp": "unique-timestamp"
  }
  ```

#### **Retrieve Summary**

- **GET /summaries/{timestamp}**
- Request:
  - `timestamp`: Unique identifier for the document.
- Response:
  ```json
  {
    "summary_english": "Summary in English...",
    "summary_kannada": "Summary in Kannada..."
  }
  ```

#### **List Summaries**

- **GET /summaries**
- Response:
  ```json
  [
      {
          "file_name": "document1.pdf",
          "timestamp": "unique-timestamp"
      },
      ...
  ]
  ```

---

## Deployment

### Docker Setup (Optional)

1. Create a `Dockerfile`:

   ```dockerfile
   FROM python:3.8-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   EXPOSE 8000

   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. Build and Run the Docker Container:
   ```bash
   docker build -t legal-document-summarizer .
   docker run -p 8000:8000 legal-document-summarizer
   ```

### Cloud Deployment

Refer to [Google Cloud Run](https://cloud.google.com/run), [AWS EC2](https://aws.amazon.com/ec2/), or [Heroku](https://www.heroku.com/) for cloud deployment steps.

---

## Testing

- Use tools like **Postman** or **cURL** to test the API endpoints.
- Example cURL command for document upload:
  ```bash
  curl -X POST "http://127.0.0.1:8000/upload" -F "file=@path/to/your/document.pdf"
  ```

---

## Future Enhancements

- Add support for additional languages.
- Improve summarization using more advanced AI models.
- Integrate a frontend for user-friendly document uploads and summary viewing.
- Implement authentication and user management.

---

## License

This project is licensed under the MIT License.

---

## Contributors

- Your Name ([KirPot05](https://github.com/KirPot05))
- Contributions are welcome! Open a pull request or file an issue to get started.

---

For further details, feel free to contact [raypot53@gmail.com].
