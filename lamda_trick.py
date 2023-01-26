# -*- coding: utf-8 -*-

from tkinter import *
from string import *
#alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alphabet = ascii_uppercase

def callback(x):
    label.configure(text='Button {} clicked'.format(alphabet[x]))

root = Tk()

label = Label()

label.grid(row=1, column=0, columnspan=26)

buttons = [0]*26 # create a list to hold 26 buttons

for i in range(26):
    buttons[i] = Button(text=alphabet[i],
                        command = lambda y=i: callback(y))
    buttons[i].grid(row=0, column=i)

mainloop()