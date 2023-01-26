# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:44:13 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *
def callback(event):
    print(event.keysym)
root = Tk()
root.bind('<Key>', callback)
mainloop()
