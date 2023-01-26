# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:51:41 2020

@author: LFC SOKOTO STUDIO
"""


from time import time
from tkinter import *
def update_timer():
    time_left = int(90 - (time()-start))
    #minutes = time_left // 60
    #seconds = time_left % 60
    minutes, seconds = divmod(time_left,60)
    time_label.configure(text='{}:{:02d}'.format(minutes, seconds))
    root.after(100, update_timer)

root = Tk()
time_label = Label()
time_label.grid(row=0, column=0)

start = time()
update_timer()
mainloop()