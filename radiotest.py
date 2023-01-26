# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:31:14 2020

@author: LFC SOKOTO STUDIO
"""
from tkinter import *

root = Tk()

def createRadios(radText = None,frame = None, font = None,
                 radVar = None, radValue = None):
    ## create buttons
    if radText != None and radValue != None:
        radLen = len(radText)
        radios = [0]*radLen
        for i in range(radLen):
            radios[i] = Radiobutton(frame,text = radText[i], font = font,
                                    var = radVar, value = radValue[i])
    else:
        errorMSG = "Radio text or value cannot be empty"
        
    return(radios)

var = IntVar()
text = ["Phone Book", "Member Cards", "Member List", "Houseolds"]
radios = createRadios(radText = text, radValue = text, radVar = var)
for i in range(len(radios)):
    radios[i].pack()

root.mainloop()