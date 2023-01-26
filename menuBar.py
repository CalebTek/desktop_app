# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:44:44 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *
from tkinter.filedialog import *

def open_callback():
    filename = askopenfilename()
    # add code here to do something with filename
def saveas_callback():
    filename = asksaveasfilename()
    # add code here to do something with filename
root = Tk()

menu = Menu()
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Open', command=open_callback)
file_menu.add_command(label='Save as', command=saveas_callback)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
menu.add_cascade(label='File', menu=file_menu)


mainloop()