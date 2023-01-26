# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 08:17:57 2020

@author: LFC SOKOTO STUDIO
"""


import os
import urllib.request

day = ["01d.png","02d.png","03d.png",
       "04d.png","09d.png","10d.png",
       "11d.png","13d.png","50d.png"]

night = ["01n.png","02n.png","03n.png",
       "04n.png","09n.png","10n.png",
       "11n.png","13n.png","50n.png"]

base_url = "http://openweathermap.org/img/w/"
img_dir = "./images/"

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# Get the day weather icon
for name in day:
    file_name = img_dir+name
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(base_url+name, file_name)
        
# Get the night weather icon
for name in night:
    file_name = img_dir+name
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(base_url+name, file_name)
