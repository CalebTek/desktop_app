# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:39:52 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *

WIDTH = 250
HEIGHT = 150

MINWIDTH = WIDTH - 50
MINHEIGHT = HEIGHT - 50

app = Tk()

app.maxsize(width = WIDTH, height = HEIGHT)
app.minsize(width = MINWIDTH, height = MINHEIGHT)

canvas = Canvas(app, width = WIDTH, height = HEIGHT)
canvas.pack()

frame1 = Frame(canvas)
frame1.pack(side = "top")
label1 = Label(frame1,text = "Input Number 1: ")
label1.pack(side = "left")
entry1 = Entry(frame1)
entry1.pack(side = "left")



frame2 = Frame(canvas)
frame2.pack(side = "top")
label2 = Label(frame2, text = "Input Number 2: ")
label2.pack(side = "left")
entry2 = Entry(frame2)
entry2.pack(side = "left")

frame3 = Frame(canvas)
frame3.pack(side = "top")

buttons_name = ["+", "-", "*", "/"]
buttons = [0]*4

for i in range(4):
    buttons[i] = Button(frame3, text = buttons_name[i], width = 6)
    buttons[i].pack(side = "left")
    
frame3 = Frame(canvas)
frame3.pack(side = "top")
label3 = Label(frame3, text = "Result: ")
label3.pack(side = "left")
entry3 = Entry(frame3)
entry3.pack(side = "left")





app.mainloop()