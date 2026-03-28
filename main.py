import PyPDF2

PDF_PATH = "/input/book.pdf"

pdfreader = PyPDF2.PdfReader(PDF_PATH)
pages = len(pdfreader.pages)

print(PDF_PATH, pages)
# for num in range(0, pages):
#     page = pdfreader.pages[num]
#     text = page.extract_text()
#     player.say(text)
#     player.runAndWait()
    