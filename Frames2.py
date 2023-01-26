# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:48:47 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *
from string import ascii_uppercase
#alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = ascii_uppercase

def color_convert(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(int(r*2.55),int(g*2.55),
                                        int(b*2.55))
root = Tk()

button_frame = Frame(borderwidth = 10, bg = "#a1ff45")
buttons = [0]*26

for i in range(26):
    buttons[i] = Button(button_frame, text=alphabet[i])
    buttons[i].grid(row=0, column=i)

ok_button = Button(text='Ok', font=('Verdana', 24), bg = color_convert(68,100,52))

button_frame.grid(row=0, column=0)
ok_button.grid(row=1, column=0)

mainloop()