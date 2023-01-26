# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:23:14 2020

@author: LFC SOKOTO STUDIO
"""


width , space = divmod(100, 10)
total = (width + space)
width = total*0.8
space = total*0.2

'''
if space == 0:
    width = width - 2
    space = space + 2
elif space == 1:
    width = width - 1
    space = space + 1
'''

relSpace = space/7




def spaceWidthMaker(n):
    width, space = divmod(100,n)
    total = (width + space)
    width = total*0.8
    space = total*0.2
    relSpace = (space/(n+1))/100
    relWidth = width/100
    width_space = [relWidth,relSpace]
    return(width_space)


