# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:00:58 2020

@author: LFC SOKOTO STUDIO
"""


# -*- coding: utf-8 -*-

from tkinter import *

menu = ["File", "Home", "Insert", "Page Layout", "Formula", "Data"]
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
RELY = [0.02,0.14,0.26,0.88]
HEIGHT = [0.1,0.1,0.6,0.1]

def spaceWidthMaker(n):
    width, space = divmod(100,n)
    total = (width + space)
    width = total*0.8
    space = total*0.2
    relSpace = (space/(n+1))/100
    relWidth = width/100
    width_space = [relWidth,relSpace]
    return(width_space)

root = Tk()

canvas = Canvas(root, bg = "gray", width = 500, height = 300)
canvas.pack()

for i in range(4):
    frame[i] = Frame(canvas, bg = "white")
    frame[i].place(relx = 0.02, rely = RELY[i], 
                   relwidth = 0.96, relheight = HEIGHT[i])


for i in range(6):
    menuButton[i] = Button(frame[0],text=menu[i])
    #RELX = [0.0067,0.1734,0.3401,0.5068,0.6735,0.8402]
    #RELSPACE = 0.0057
    #RELWIDTH = 0.16
    RELSPACE = spaceWidthMaker(6)[1]
    RELWIDTH = spaceWidthMaker(6)[0]
    
    RELX = [(RELSPACE*(i+1) + RELWIDTH*i) for i in range(6)]
    menuButton[i].place(relx = RELX[i], relheight = 1, relwidth = RELWIDTH)
    FormatButton[i] = Button(frame[1], text=Format[i], width = 8)
    FormatButton[i].place(relx = RELX[i], relheight = 1, relwidth = RELWIDTH)




for i in range(4):
    #RELSPACE = 0.005
    #RELWIDTH = 0.244
    RELSPACE = spaceWidthMaker(4)[1]
    RELWIDTH = spaceWidthMaker(4)[0]+0.039
    
    RELX = [(RELSPACE*(i+1) + RELWIDTH*i) for i in range(4)]
    FormatButton2[i] = Button(frame[3], text=Format[i+6])
    FormatButton2[i].place(relx = RELX[i], relheight = 1, relwidth = RELWIDTH)

for i in range(3):
    workAreaButton[i] = Button(frame[2], text=workArea[i])
    RELWIDTH = [0.15,0.68,0.15]
    RELSPACE = 0.025
    RELX = [0.005, 0.160, 0.845]
    workAreaButton[i].place(relx = RELX[i], relheight = 1, relwidth = RELWIDTH[i])

root.mainloop()
