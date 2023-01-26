# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:43:05 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import * 
from tkinter.messagebox import *

def quitter_function():
    answer = askquestion(title='Quit?', message='Do you want to Quit?')
    if answer=='yes':
        root.destroy()
'''
def tab():
    if keysym=='Return':
        keysym = "Tab"
    return(keysym)
'''

def convert():
    from includes.baseNumberClass import BaseNumber
    base10 = entry1.get()
    newbase = entry2.get()
    if base10 == "" or newbase == "":
        showwarning(title='Warning', message='Oops, Filled the box')
    else:
        base10 = int(base10)
        newbase = int(newbase)
    if 10 < newbase <= 26: #newbase >10 and newbase <= 26:
        convertBase = BaseNumber(base10, newbase).base10ToUpperBase()
    elif 2 <= newbase < 10: #newbase >= 2 and newbase < 10:
        convertBase = BaseNumber(base10, newbase).base10ToLowerBase()
    if newbase == 10:
        convertBase = "{} already in Base 10".format(base10)
    if newbase > 26:
        convertBase = "Error, base {} higer than base 26".format(newbase)
    if newbase < 2:
        convertBase = "Error, base {} lower than base 2".format(newbase)
    label3.configure(text="{}".format(convertBase))
    entry1.delete(0,END)
    entry2.delete(0,END)

root= Tk()
root.title("Base Converter")
root.wm_iconbitmap("./images/converter.ico")

canvas = Canvas(root, width = 300, height = 300, bg = "#e3f2e7")
canvas.pack()

entry1 = Entry(canvas,font=('helvetica', 12)) 
entry1.place(relx = 0.45, rely = 0.2, relheight = 0.1, relwidth = 0.50)


entry2 = Entry(canvas, font=('helvetica', 12)) 
entry2.place(relx = 0.45, rely = 0.32, relheight = 0.1, relwidth = 0.50)


label0 = Label(canvas, text='Base Converter')
label0.config(font=('helvetica', 16, "bold"), bg = "green", fg = "white")
label0.place(relx = 0.05, rely = 0.05, relheight = 0.1, relwidth = 0.9)


label1 = Label(canvas, text='Number in Base 10:')
label1.config(font=('helvetica', 10), anchor = "nw", justify = "left", bg ="#e3f2e7")
label1.place(relx = 0.05, rely = 0.2, relheight = 0.1, relwidth = 0.4)

label2 = Label(canvas, text='New Base Number:')
label2.config(font=('helvetica', 10), anchor = "nw", justify = "left", bg ="#e3f2e7")
label2.place(relx = 0.05, rely = 0.32, relheight = 0.1, relwidth = 0.4)


label_frame = Frame(canvas, bg = "green")
label_frame.place(relx = 0.05, rely = 0.56, relheight = 0.4, relwidth = 0.9)
label3 = Label(label_frame)
label3.config(font=('helvetica', 16), anchor = "nw", justify = "left", bg ="#e3f2e7")
label3.place(relx = 0.025, rely = 0.025, relwidth = 0.95, relheight = 0.95)



button = Button(canvas, text='Convert', command=convert, 
                bg='green', fg='white', font=('helvetica', 9, 'bold'), 
                width = 7)
button.place(relx = 0.7, relheight = 0.1, rely = 0.44, relwidth = 0.25)


#entry1.bind("<Return>", lambda dummy=0:tab())

entry2.bind("<Return>", lambda dummy=0:convert())


root.protocol('WM_DELETE_WINDOW', quitter_function)

root.mainloop()