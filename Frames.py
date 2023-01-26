# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:41:53 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *
from string import ascii_uppercase

root = Tk()
alphabet = ascii_uppercase
buttons = [0]*26

for i in range(26):
    buttons[i] = Button(text=alphabet[i])
    buttons[i].grid(row=0, column=i)

ok_button = Button(text='Ok', font=('Verdana', 24))
ok_button.grid(row=1, column=0, columnspan = 26)

mainloop()