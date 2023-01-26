# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:47:14 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *


root = Tk()
canvas = Canvas(width=200, height=200, bg='#a47500')
canvas.create_rectangle(20,100,30,150, fill='#1c6494')
canvas.create_rectangle(20,100,70,180)
canvas.create_oval(20,100,70,180, fill='#1c6494')
canvas.create_line(20,100,70,180, fill='green')
canvas.grid(row=0,column=0)

mainloop()