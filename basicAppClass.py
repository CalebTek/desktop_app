# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:52:10 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *


WIDTH, HEIGHT = 540, 400

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Tkinter GUI using Class")
        self.maxsize(WIDTH, HEIGHT)
        self.minsize(440,300)
        self.wm_iconbitmap("./images/sun_icon.ico")
        self.configure(bg = "#4d4d4d")
        
        self.createWidget()
        
    # GUI program that converts temperatures from Fahrenheit to Celsius.
    def calculate(self):
        self.temp = int(self.entry.get())
        temp = (self.temp-32)*(5/9)
        kelvin = temp + 273.15
        self.output_label.configure(
            text = 'Conversion: \n{} \u2109 = {:.2f} \u2103 \n{} \u2109 = {:.2f} K'
            .format(self.temp,temp, self.temp, kelvin))
        self.entry.delete(0,END)
        
    def createWidget(self):
        self.canvas = Canvas(self, width = WIDTH, height = HEIGHT)
        self.canvas.pack(side = "left")
        
        self.upper_frame = Frame(self.canvas, bd = 5, bg = "red")
        self.upper_frame.place(relx=0.1, rely = 0.1,relheight = 0.3, relwidth = 0.8)
        self.message_label = Label(self.upper_frame, text='Enter Temperature in \u2109',
                      font=('Verdana', 16, "bold"), fg = "red")
        self.message_label.place(relheight = 0.4, relwidth = 1)
        
        self.entry = Entry(self.upper_frame, font=('Verdana', 16))
        self.entry.place(relheight = 0.5, relwidth = 0.7, rely = 0.5)
        self.calc_button = Button(self.upper_frame, text='Convert', font=('Verdana', 16,"bold"), fg='red',
                             command=self.calculate)
        self.calc_button.place(relheight = 0.5, relwidth = 0.3, rely = 0.5, relx = 0.7)
        
        self.lower_frame = Frame(self.canvas, bd = 5, bg = "red")
        self.lower_frame.place(relx = 0.1, rely = 0.45, relheight = 0.5, relwidth = 0.8)
        self.output_label = Label(self.lower_frame, font=('Verdana', 16), justify = "left", anchor = "nw")
        self.output_label.place(relheight = 1, relwidth = 1)
       
        self.entry.bind('<Return>', lambda dummy=0:self.calculate())
        
        #message_label.grid(row=0, column=0)
        #entry.grid(row=0, column=1)
        #calc_button.grid(row=0, column=2)
        #output_label.grid(row=1, column=0, columnspan=3)
                
        
app = Root()


'''
app = Tk()
app.title("Tkinter GUI using Class")
app.minsize(540,400)
app.wm_iconbitmap("./images/sun_icon.ico")
app.configure(bg = "#4d4d4d")
'''

app.mainloop()