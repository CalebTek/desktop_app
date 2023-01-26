# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:58:32 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *

def callback(event):
    global move#, move_
    if event.keysym=='Right':
        move += 1
        canvas.coords(rect,50+move,50,100+move,100)
    elif event.keysym=='Left':
        move -=1
        canvas.coords(rect,50+move,50,100+move,100)
    if event.keysym == "Down":
        move += 1
        canvas.coords(rect,50,50+move,100,100+move)
    elif event.keysym == "Up":
        move -=1
        canvas.coords(rect,50,50+move,100,100+move)

root = Tk()
root.bind('<Key>', callback)

canvas = Canvas(width=200,height=200)
canvas.grid(row=0,column=0)
rect = canvas.create_rectangle(50,50,100,100,fill='blue')

move= 0#, move_ = 0,0

mainloop()