# -*- coding: utf-8 -*-

from tkinter import *
from includes.DigitalRoot import DigitalRoot


# GUI program that converts temperatures from Fahrenheit to Celsius.
def digitalRoot_():
    digits = int(entry.get())
    D = DigitalRoot(digits)
    output_label.configure(
        text = 'The digital root of {} is {} '.format(digits,D.digitalRoot()))
    output_label2.configure(
        text = 'The split digits of {} is {} '.format(digits,D.splitNum()))
    output_label3.configure(
        text = 'The add splitted digits of {} is {} '.format(digits,D.addSplit()))
    entry.delete(0,END)


root = Tk()


message_label = Label(text='Enter the number',
                      font=('Verdana', 16, "bold"))
output_label = Label(font=('Verdana', 16))
output_label2 = Label(font=('Verdana', 16))
output_label3 = Label(font=('Verdana', 16))
entry = Entry(font=('Verdana', 16), width=6)
calc_button = Button(text='Get Digital Root', font=('Verdana', 16),bg='red', fg='white',
                     command=digitalRoot_)
entry.bind('<Return>', lambda dummy=0:digitalRoot_())

message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)
output_label2.grid(row=2, column=0, columnspan=3)
output_label3.grid(row=3, column=0, columnspan=3)

mainloop()