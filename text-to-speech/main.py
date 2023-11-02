import pyttsx3, PyPDF2

# Another PDF can be converted by changing the name
pdfreader = PyPDF2.PdfReader('book.pdf') 
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num]
    clean_text = text.extract_text().replace('\n', ' ')
    print(clean_text)

# Name of the mp3 file can be changed as per the choice
speaker.save_to_file(clean_text, 'book.mp3')
speaker.runAndWait()

speaker.stop()

