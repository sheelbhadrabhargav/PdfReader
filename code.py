!pip install pyttsx3
!pip install PyPDF2
!sudo apt-get install libespeak-dev
from tkinter import *
import pyttsx3
from tkinter import filedialog
import PyPDF2

engine = pyttsx3.init()
engine.setProperty('rate', 130)  # Adjust this value to control the speed

win = Tk()
win.title("Text to speech converter")
win.configure(bg="pink")
win.geometry("500x300")

def speak_text(input_text):
    engine.say(input_text)
    engine.runAndWait()

def convert_pdf_to_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page_num].extract_text()
        return text
    except Exception as e:
        return str(e)

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_text = convert_pdf_to_text(file_path)
        text.set(pdf_text)

def speak():
    input_text = text.get()
    if input_text:
        speak_text(input_text)

# label frame
pbl = LabelFrame(win, text="TEXT TO SPEECH CONVERTER", font=30, bd=10, bg="white")
pbl.pack(fill="both", expand="yes", padx=10, pady=50)
Label(pbl, text="Text", font="30", padx=15).pack(side=LEFT)

# entry
text = StringVar()
Entry(pbl, width=25, bd=5, font="20", textvariable=text).pack(side=LEFT, padx=10)

# buttons
Button(pbl, text="Speak", font=15, command=speak).pack(side=LEFT)
Button(pbl, text="Open PDF", font=15, command=open_file_dialog).pack(side=LEFT)

mainloop()
