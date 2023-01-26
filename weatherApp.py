from tkinter import *
from tkinter.messagebox import *
import requests

WIDTH = 600
HEIGHT = 500

def quit_func():
    answer = askquestion(title='Quit?', message='Do you want to Quit?')
    if answer=='yes':
        root.destroy()
        

def get_weather():
    wx = entry.get()
    #label.configure(text="{}".format(wx))
    label["text"] = wx
    entry.delete(0,END)


'''
def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]
        
        final_str = "City: %s \nConditions: %s \nTemperature: %s" % (name,desc,temp)
    except:
        final_str = "Problem retrieving that information"
    return(final_str)
        

def get_weather():
    weather_key = "3c6d376bab2eb677c125eae404a840e3"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"APPID":weather_key, "q":city, "units":"metric"}
    response = requests.get(url, params = params)
    weather = response.json()
'''
    
root = Tk()

root.title("Weather Application")
root.maxsize(WIDTH, HEIGHT)

canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#image_frame = Frame(root, bg="#1f4b66")
#image_frame.place(relwidth=1, relheight=1)

#image_frame = Frame(root)
#image_frame.place(relheight = 1, relwidth = 1)

bg_image = PhotoImage(file = "images/wp1.png")
bg_label = Label(root, image = bg_image)
bg_label.place(relwidth=1, relheight=1)

upper_frame = Frame(root,bg="#1f4b66",bd=5)
upper_frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

entry = Entry(upper_frame, font = "Courier 14 bold")
entry.place(relwidth = 0.65,relheight = 1)
entry.bind("<Return>", lambda dummy=0:get_weather())

# command = lambda:get_weather(entry.get()))#

button = Button(upper_frame, text = "Get Weather", 
                font = "Courier 14 bold", bg = "#923429", fg = "#1f4b66", command=get_weather)
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

lower_frame = Frame(root, bg = "#1f4b66", bd = 5)
lower_frame.place(relx=0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

label = Label(lower_frame, font = "Courier 14 bold", justify = "left", anchor = "nw")
label.place(relwidth=1,relheight=1)

root.protocol('WM_DELETE_WINDOW', quit_func)

root.mainloop()