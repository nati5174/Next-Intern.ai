from pypdf import PdfReader

def extract_pdf_info(pdf):

    reader = PdfReader(pdf)
    pages = len(reader.pages)

    if pages > 1:
        text = []
        for i in range(len(pages)):
            page = reader.pages[i]
            text.append(page.extract_text())
        return " ".join(text) 

    else:
        return reader.pages.extract_text()  



    