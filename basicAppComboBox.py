# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:52:10 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *
from tkinter import ttk


WIDTH, HEIGHT = 540, 400

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Tkinter GUI using Class")
        self.maxsize(WIDTH, HEIGHT)
        self.minsize(440,300)
        #self.wm_iconbitmap("./images/sun_icon.ico")
        self.configure(bg = "#4d4d4d")
        
        self.createWidget()
        
    # GUI program that converts temperatures from Fahrenheit to Celsius.
    def calculate(self):
        self.unit1 = self.selectUnit1.get()
        self.unit2 = self.selectUnit2.get()
        self.temp = int(self.entry.get())
        
        if self.unit1 == self.unitName[0] and self.unit2 == self.unitName[1]:
            # fahrenheit to celcius
            degC = (self.temp - 32) * (5/9)
            self.output_label.configure(
                text = 'Conversion: \n{} \u2109 = {:.2f} \u2103'
                .format(self.temp, degC))
        elif self.unit1 == self.unitName[0] and self.unit2 == self.unitName[2]:
            # fahrenheit to Kelvin
            kelvin = (self.temp - 32) * (5/9) + 273.15
            self.output_label.configure(
                text = 'Conversion: \n{} \u2109 = {:.2f} K'
                .format(self.temp, kelvin))
        elif self.unit1 == self.unitName[1] and self.unit2 == self.unitName[0]:
            # celsius to fahrenheit
            degF = ((9/5) * self.temp) + 32
            self.output_label.configure(
                text = 'Conversion: \n{} \u2103 = {:.2f} \u2109'
                .format(self.temp, degF))
        elif self.unit1 == self.unitName[1] and self.unit2 == self.unitName[2]:
            # celsuis to Kelvin
            kelvin = self.temp + 273.15
            self.output_label.configure(
                text = 'Conversion: \n{} \u2103 = {:.2f} K'
                .format(self.temp, kelvin))
        elif self.unit1 == self.unitName[2] and self.unit2 == self.unitName[0]:
            # Kelvin to fahrenheit
            degF = ((9/5) * (self.temp - 273.15)) + 32
            self.output_label.configure(
                text = 'Conversion: \n{} K = {:.2f} \u2109'
                .format(self.temp, degF))
        elif self.unit1 == self.unitName[2] and self.unit2 == self.unitName[1]:
            # Kelving to Celsius
            degC = self.temp - 273.15
            self.output_label.configure(
                text = 'Conversion: \n{} K = {:.2f} \u2103'
                .format(self.temp, degC))
        else:
            self.output_label.configure(
                text = "Can't convert, temperature units are the same")
            self.output_label.configure(font=('Verdana', 12))
        #self.output_label.configure(text = 'Conversion: \n{} \u2109 = {:.2f} \u2103 \n{} \u2109 = {:.2f} K'.format(self.temp,temp, self.temp, kelvin))
        self.entry.delete(0,END)
        
    def createWidget(self):
        self.canvas = Canvas(self, width = WIDTH, height = HEIGHT)
        self.canvas.pack(side = "left")
        
        #upper frame
        self.upper_frame = Frame(self.canvas, bd = 5, bg = "red")
        self.upper_frame.place(relx=0.1, rely = 0.1,relheight = 0.2, relwidth = 0.8)
        self.message_label = Label(self.upper_frame, text='Temperature Conversion',
                      font=('Verdana', 16, "bold"), fg = "red", bg = "white")
        self.message_label.place(relheight = 0.45, relwidth = 1)
        
        self.input_label = Label(self.upper_frame, text='Enter Temperature',
                      font=('Verdana', 16, "bold"), fg = "white", bg = "red",
                      justify = "left", anchor = "nw")
        self.input_label.place(rely = 0.5, relheight = 0.5, relwidth = 0.65)
        self.entry = Entry(self.upper_frame, font=('Verdana', 16), fg = "red")
        self.entry.place(relheight = 0.5, relwidth = 0.35, rely = 0.5, relx= 0.65)
        
        #middle Frame
        self.middle_frame = Frame(self.canvas, bd = 5)
        self.middle_frame.place(relx=0.1, rely = 0.31, relheight = 0.31, relwidth = 0.8)
        
        self.from_label = Label(self.middle_frame, text = "Convert temperature from ",
                      font=('Verdana', 12, "bold"), fg = "red", justify = "right", anchor = "ne")
        self.from_label.place(relheight = 0.3, relwidth = 0.7)
        
        self.selectUnit1 = StringVar()
        self.unitName = ("Fahrenheit", "Celsius", "Kelvin")
        self.combo1 = ttk.Combobox(self.middle_frame, textvariable = self.selectUnit1,
                                   font=('Verdana', 12), foreground = "red")
        self.combo1["values"] = self.unitName
        self.combo1.place(relx = 0.71, relheight = 0.3, relwidth = 0.3)
        
        self.to_label = Label(self.middle_frame, text = "Convert temperature to ",
                      font=('Verdana', 12, "bold"), fg = "red", justify = "right", anchor = "ne")
        self.to_label.place(rely = 0.32,relheight = 0.3, relwidth = 0.7)
        
        self.selectUnit2 = StringVar()
        self.combo2 = ttk.Combobox(self.middle_frame, textvariable = self.selectUnit2,
                                   font=('Verdana', 12), foreground = "red")
        self.combo2["values"] = self.unitName
        self.combo2.place(rely = 0.32, relx = 0.71, relheight = 0.3, relwidth = 0.3)
        
        
        self.calc_button = Button(self.middle_frame, text='Convert', font=('Verdana', 16,"bold"), fg='red',
                             command=self.calculate)
        self.calc_button.place(relheight = 0.3, relwidth = 0.3, rely = 0.65, relx = 0.71)
        
        #lower frame
        self.lower_frame = Frame(self.canvas, bd = 5, bg = "red")
        self.lower_frame.place(relx = 0.1, rely = 0.62, relheight = 0.28, relwidth = 0.8)
        self.output_label = Label(self.lower_frame, font=('Verdana', 16), justify = "left",
                                  anchor = "nw", fg = "red")
        self.output_label.place(relheight = 1, relwidth = 1)
       
        self.combo2.bind('<Return>', lambda dummy=0:self.calculate())
        self.calc_button.bind('<Return>', lambda dummy=0:self.calculate())
        
        #message_label.grid(row=0, column=0)
        #entry.grid(row=0, column=1)
        #calc_button.grid(row=0, column=2)
        #output_label.grid(row=1, column=0, columnspan=3)
                
        
#app = Root()


'''
app = Tk()
app.title("Tkinter GUI using Class")
app.minsize(540,400)
app.wm_iconbitmap("./images/sun_icon.ico")
app.configure(bg = "#4d4d4d")
'''

#app.mainloop()

if __name__ == '__main__':
    app = Root()
    app.mainloop()