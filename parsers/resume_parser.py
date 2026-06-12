from pypdf import PdfReader
from docx import Document


def extract_resume_text(uploaded_file):
    """
    Extract text from PDF, DOCX, or TXT resume files.
    """

    file_name = uploaded_file.name.lower()

    # PDF
    if file_name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text


    # DOCX
    elif file_name.endswith(".docx"):
        doc = Document(uploaded_file)

        text = "\n".join(
            paragraph.text for paragraph in doc.paragraphs
        )

        return text


    # TXT
    elif file_name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")


    else:
        raise ValueError(
            "Unsupported file type. Upload PDF, DOCX, or TXT."
        )