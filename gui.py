from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont

import app

#setup
root = Tk()
root.title("idojaras app")
root.geometry("300x500")
frm = ttk.Frame(root, padding=30)
frm.grid()

title_font = tkfont.Font(size=25)

#UI\
elements = {
"title": ttk.Label(frm,
        text="idojarasos app", 
        font=title_font
        ).grid(column=0, row=0),

"city_entry_text": ttk.Label(frm,
          text="Enter city name: "
        ).grid(column=0, row=2),

"city_entry": ttk.Entry(frm
        ),

"warning": ttk.Label(frm, 
        text="error",
        foreground="red"
        ),

"exit": ttk.Button(frm, 
        text="Quit", 
        command=root.destroy
        ).grid(column=0, row=10),
}

#logic

def launch():
    root.mainloop()

def warning(message:str):
    elements["warning"].text = message
    elements["warning"].grid(column=0, row=4)
    print(message)

def refresh_info():
    city_input = elements["city_entry"].get()
    info = app.get_weather(city_input)
    if info is not str:
        pass
    else:
        warning(f"error: {type(info)}")
    

elements["city_entry"].bind("<Return>", lambda event: refresh_info())
elements["city_entry"].grid(column=0, row=3)
elements["warning"].grid(column=0, row=4)

if __name__ == "__main__": #testing UI
    launch()