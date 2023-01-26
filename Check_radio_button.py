# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:44:47 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *
from tkinter.scrolledtext import ScrolledText

color = ["red", "green", "blue"]
root = Tk()

def getvalue():
    getcheck = show_totals.get()
    if getcheck == 1:
        show_label.configure(text="Box Checked, value is {}".format(getcheck))
    else:
        show_label.configure(text="Box not Checked value is {}".format(getcheck))
    getselect = colorVar.get()
    if getselect == 1:
        c = color[0].title()
    elif getselect == 2:
        c = color[1].title()
    else:
        c = color[2].title()
    show_label2.configure(text="{} Radio Selected, value is {}".format(c,getselect))

def getradio():
    getselect = colorVar.get()
    if getselect == 1:
        c = color[0]
    elif getselect == 2:
        c = color[1]
    else:
        c = color[2]
    show_label2.configure(text="{} Radio Selected, value is {}".format(c,getselect))

submit = Button(text="Submit", command=getvalue)
show_label = Label()
show_label2 = Label()
show_label2.grid(row=3, column=0, columnspan =2)

show_totals = IntVar()
#show_totals.get()
#show_totals.set(0)

check = Checkbutton(text='Show totals', var=show_totals)
check.grid(row=0,column=0)
#show_totals.grid(row=1, column=0)

show_label.grid(row=2, column=0, columnspan = 2)
submit.grid(row=0, column=1)

colorVar = IntVar()

buttons = [0]*3

textbox = ScrolledText(font=('Verdana', 12), height=6, width=40)
textbox.grid(row=4,column=0, columnspan = 3)


for i in range(3):
    buttons[i] = Radiobutton(text=color[i], var=colorVar, value = (i+1))#, command = getradio)
    buttons[i].grid(row=(1), column=i)

mainloop()