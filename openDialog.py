# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:13:20 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText

root = Tk()

textbox = ScrolledText()
textbox.grid()
filename=askopenfilename(initialdir='C:\\Users\\LFC SOKOTO STUDIO\\Documents\\',
filetypes=[("Python files", ".py"),('Text files', '.txt'),('All files', '*')])
s = open(filename).read()
textbox.insert(1.0, s)

mainloop()