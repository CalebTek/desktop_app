# -*- coding: utf-8 -*-

from tkinter import *

menu = ["File", "Home", "Insert", "Paye Layout", "Formula", "Data"]
Format = ["Format "]*10
for i in range(10):
    Format[i] = Format[i]+ str(i+1)

workArea = ["Navigation", "Work Area", "Properties"]
workAreaButton = [0]*3
workAreaColSpan = [1,4,1]
workAreaCol = [0,1,5]
    
menuButton = [0]*6
FormatButton = [0]*6
FormatButton2 = [0]*4
FormatColSpan = [2,1,1,2]
FormatCol = [0,2,3,4]

frame = [0]*4


root = Tk()

canvas = Canvas(root)
canvas.pack()

for i in range(4):
    frame[i] = Frame(canvas,bg = "green")
    frame[i].pack(side = "top")


for i in range(6):
    menuButton[i] = Button(frame[0],text=menu[i], width = 8)
    menuButton[i].pack(side = "left")
    FormatButton[i] = Button(frame[1], text=Format[i], width = 8)
    FormatButton[i].pack(side = "left")

for i in range(4):
    if FormatColSpan[i] == 2:
        Width = 8*2
    else:
        Width = 8
    FormatButton2[i] = Button(frame[3], text=Format[i+6], width = Width)
    FormatButton2[i].pack(side = "left")
    
for i in range(3):
    if workAreaColSpan[i] == 4:
        Width = 8*4
    else:
        Width = 8
    workAreaButton[i] = Button(frame[2], text=workArea[i], width = Width, height = 8)
    workAreaButton[i].pack(side = "left")

mainloop()