import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = " ".join(page.get_text() for page in doc)
    return text
