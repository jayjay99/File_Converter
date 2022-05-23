import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from pdf2docx import Converter,parse

filenames=""
file_path=""
convertfilename="convertfile.docx"
def choose1_event():
    global file_path
    filetypes=(("PDF Files","*.pdf"),)
    filenames=fd.askopenfile(filetypes=filetypes)
    if filenames:
        file_path=os.path.abspath(filenames.name)
    file1Label.config(text=file_path)
    

def tran2Word():
    global file_path
    parse(file_path,convertfilename,start=0,end=None)

window = tk.Tk()
window.title('File Converter')
window.geometry('500x300')
file1Button=tk.Button(window,text='選擇PDF檔案',command=choose1_event)
file1Button.place(x=100,y=50)
file1Label=tk.Label(window,text='請選擇檔案')
file1Label.place(x=100,y=30)
fileTransfer=tk.Button(window,text="轉成WORD",command=tran2Word)
fileTransfer.place(x=100,y=80)
window.mainloop()