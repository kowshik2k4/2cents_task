from docx import Document
from io import BytesIO

def parse_docx(file):
    doc = Document(BytesIO(file.read()))
    text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    return text
