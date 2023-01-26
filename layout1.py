# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:21:47 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *

root = Tk()

canvas = Canvas(root, bg = "green")
canvas.pack()

label = Label(canvas, text = "Test Place x argument")
#label.place(relx= 0.1, rely = 0.1, relheight = 0.1, relwidth = 0.8)
label.pack(side = "left")

label = Label(canvas, text = "Test Place x argument")
#label.place(relx= 0.1, rely = 0.22, relheight = 0.1, relwidth = 0.8)
label.pack(side = "left")

label = Label(canvas, text = "Test Place x argument")
#label.place(relx= 0.1, rely = 0.34, relheight = 0.1, relwidth = 0.8)
label.pack(side = "left")

root.mainloop()