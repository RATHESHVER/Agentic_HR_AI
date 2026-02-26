import PyPDF2
import docx
import re

def parse_resume(file_path):
    print("📄 Parsing resume:", file_path)
    text = ""

    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted

    elif file_path.endswith(".docx"):
        document = docx.Document(file_path)
        for para in document.paragraphs:
            text += para.text + " "

    # Clean text
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", "", text)

    return text
