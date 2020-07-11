import pyttsx3 as pt
import PyPDF2 as pdf

book = open('D:/Python Code/Best-on-Python/Data/abc.pdf', 'rb')
pdfReader = pdf.PdfFileReader(book)
pages = pdfReader.numPages
print('Total Pages', pages)

speaker = pt.init()
for n in range(1, pages):
    single_page = pdfReader.getPage(n)
    text = single_page.extractText()
    speaker.say(text)
    speaker.runAndWait()
