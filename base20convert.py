# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:50:33 2020

@author: LFC SOKOTO STUDIO
"""


# -*- coding: utf-8 -*-

from tkinter import *
from includes.base20 import base20
from tkinter.messagebox import *


# GUI program that converts temperatures from Fahrenheit to Celsius.
def convert():
    base10 = entry.get()
    if base10 == "":
        showwarning(title='Warning', message='Oops, Enter a number')
    else:
        base20Convert = base20(int(base10))
    output_label.configure(text = '{} in Base 20 is {} '.format(base10,base20Convert))
    entry.delete(0,END)


root = Tk()
message_label = Label(text='Enter number in base 10',
                      font=('Verdana', 16, "bold"))
output_label = Label(font=('Verdana', 16))
entry = Entry(font=('Verdana', 16), width=6)
calc_button = Button(text='Convert', font=('Verdana', 16),bg='red', fg='white',
                     command=convert, width=10)
entry.bind('<Return>', lambda dummy=0:convert())

message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)

mainloop()