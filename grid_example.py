# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:08:47 2020

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
frame1.grid(row = 0, column = 0)
label1 = Label(frame1,text = "Input Number 1: ")
label1.grid(row = 0, column = 0)
entry1 = Entry(frame1)
entry1.grid(row = 0 , column = 1)



frame2 = Frame(canvas)
frame2.grid(row = 1, column = 0)
label2 = Label(frame2, text = "Input Number 2: ")
label2.grid(row = 0, column = 0)
entry2 = Entry(frame2)
entry2.grid(row = 0, column = 1)


frame3 = Frame(canvas)
frame3.grid(row = 2, column = 0)

buttons_name = ["+", "-", "*", "/"]
buttons = [0]*4

for i in range(4):
    buttons[i] = Button(frame3, text = buttons_name[i], width = 6)
    buttons[i].grid(row = 0, column = i)
    
frame3 = Frame(canvas)
frame3.grid(row = 3, column = 0)
label3 = Label(frame3, text = "Result: ")
label3.grid(row = 0, column = 0)
entry3 = Entry(frame3, width = 25)
entry3.grid(row = 0, column = 1)





app.mainloop()