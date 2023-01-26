# -*- coding: utf-8 -*-

from tkinter import *


# GUI program that converts temperatures from Fahrenheit to Celsius.
def calculate():
    temp = int(entry.get())
    temp = (temp-32)*(5/9)
    output_label.configure(text = 'Converted: {:.1f} \u2103'.format(temp))
    entry.delete(0,END)


root = Tk()
root.title("Temperature Converter")
message_label = Label(text='Enter temperature in Fahrenheit',
                      font=('Verdana', 16, "bold"))
output_label = Label(font=('Verdana', 16))
entry = Entry(font=('Verdana', 16), width=6)
calc_button = Button(text='Calculate', font=('Verdana', 16),bg='red', fg='white',
                     command=calculate, width=10)
entry.bind('<Return>', lambda dummy=0:calculate())

message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)

mainloop()