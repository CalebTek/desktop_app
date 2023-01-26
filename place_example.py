# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:08:34 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *
from tkinter import ttk

WIDTH = 250
HEIGHT = 150

MINWIDTH = WIDTH - 50
MINHEIGHT = HEIGHT - 50

app = Tk()
app.title("Calculator")

app.maxsize(width = WIDTH, height = HEIGHT)
app.minsize(width = MINWIDTH, height = MINHEIGHT)

canvas = Canvas(app, width = WIDTH, height = HEIGHT)
canvas.pack()

frame1 = Frame(canvas)
frame1.place(relheight = 0.2,relwidth = 0.9, relx = 0.05, rely = 0.05)
label1 = ttk.Label(frame1,text = "Input Number 1: ")
label1.place(relwidth = 0.41)
entry1 = ttk.Entry(frame1)
entry1.place(relx = 0.43)



frame2 = Frame(canvas)
frame2.place(rely = 0.22,relheight = 0.2, relwidth = 0.9, relx = 0.05)
label2 = ttk.Label(frame2, text = "Input Number 2: ")
label2.place(relwidth = 0.41)
entry2 = ttk.Entry(frame2)
entry2.place(relx = 0.43)


frame3 = Frame(canvas)
frame3.place(rely = 0.44, relheight = 0.2, relwidth = 0.9, relx = 0.05)

buttons_name = ["+", "-", "x", "/"]
buttons = [0]*4

for i in range(4):
    buttons[i] = Button(frame3, text = buttons_name[i], width = 6)
    Relx = [0,0.25,0.5,0.75]
    buttons[i].place(relx = Relx[i], relwidth = 0.24)
    

frame4 = Frame(canvas)
frame4.place(rely = 0.66, relwidth = 0.9, relheight = 0.2, relx = 0.05)
label3 = ttk.Label(frame4, text = "Result: ")
label3.place(relwidth = 0.2)
entry3 = ttk.Entry(frame4)
entry3.place(relx = 0.25, relwidth = 0.75)


app.mainloop()