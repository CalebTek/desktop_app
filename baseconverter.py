# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:02:42 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import * 

def convert():
    from includes.baseNumber import base10ToLowerBase, base10ToUpperBase
    base10 = int(entry1.get())
    newbase = int(entry2.get())
    if 10 < newbase <= 26: #newbase >10 and newbase <= 26:
        convertBase = base10ToUpperBase(base10, newbase)
    elif 2 <= newbase < 10: #newbase >= 2 and newbase < 10:
        convertBase = base10ToLowerBase(base10, newbase)
    if newbase == 10:
        convertBase = "{} already in Base 10".format(base10)
    if newbase > 26:
        convertBase = "Error, base {} higer than base 26".format(newbase)
    if newbase < 2:
        convertBase = "Error, base {} lower than base 2".format(newbase)
    label4.configure(text="{}".format(convertBase))
    entry1.delete(0,END)
    entry2.delete(0,END)

root= Tk()

#canvas1 = Canvas(root, width = 300, height = 300)
#canvas1.pack()

entry1 = Entry() 
entry1.grid(row=1, column = 1)


entry2 = Entry() 
entry2.grid(row=2, column = 1)

label4 = Label() 
label4.grid(row=4,column=1)

label0 = Label(text='Base Converter')
label0.config(font=('helvetica', 14))
label0.grid(row=0,column=0, columnspan=2)

label1 = Label(text='Number in Base 10  ')
label1.config(font=('helvetica', 10))
label1.grid(row=1,column=0)

label2 = Label(text='New Base Number  ')
label2.config(font=('helvetica', 10))
label2.grid(row=2,column=0)

label3 = Label(text='Result:')
label3.config(font=('helvetica', 10))
label3.grid(row=4,column=0)

button = Button(text='Convert', command=convert, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 7)
button.grid(row=3,column=1)

entry2.bind("<Return>", lambda dummy=0:convert())

root.mainloop()