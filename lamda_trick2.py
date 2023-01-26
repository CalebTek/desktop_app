# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from tkinter import *
from string import *
#alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alphabet = ascii_uppercase

menu = ["File","Edit","Search", "Source","Run","Debug", "Consoles","Projects",
        "Tools", "View", "Help"]

def callback(x):
    label.configure(text='Button {} clicked'.format(menu[x]))

root = Tk()

label = Label()

label.grid(row=1, column=0, columnspan=11)

buttons = [0]*11 # create a list to hold 26 buttons

for i in range(11):
    buttons[i] = Button(text=menu[i],
                        command = lambda y=i: callback(y), bg = "white")
    buttons[i].grid(row=0, column=i)

mainloop()