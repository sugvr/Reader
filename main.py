import PyPDF2
import pyttsx3

path = open('IsaiDel.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(path)

from_page = pdfReader.getPage(0)
text = from_page.extractText()

speak = pyttsx3.init('sapi5')
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[1].id)
speak.say(text)
speak.runAndWait()