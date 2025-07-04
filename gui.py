from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import PhotoImage

import app

#setup
root = Tk()
root.title("idojaras app")
root.geometry("350x500")
frm = ttk.Frame(root, padding=30)
frm.grid()

title_font = tkfont.Font(size=25)
#UI\
elements = {
"logo": ttk.Label(frm,
        text="⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆ ",
        font=title_font
        ).grid(column=0, row=0),
        
"title": ttk.Label(frm,
        text="idojarasos app", 
        font=title_font
        ).grid(column=0, row=1),

"city_entry_text": ttk.Label(frm,
          text="Enter city name: "
        ).grid(column=0, row=2),

"city_entry": ttk.Entry(frm
        ),

"warning": ttk.Label(frm, 
        text="",
        foreground="red"
        ),

"submit": ttk.Button(frm, 
        text="submit",
        ),

"city": ttk.Label(frm, 
        text="",
        ),

"temp": ttk.Label(frm, 
        text="",
        ),

"contition": ttk.Label(frm, 
        text="",
        ),
}

#logic

def launch():
    root.mainloop()

def warning(message:str):
    elements["warning"].config(text=message)
    print(message)

def refresh_info():
    city_input = elements["city_entry"].get()
    info = app.get_weather(city_input)
    if type(info) is int:
        warning(app.api_errors.get(info) or f"Error code: {info}")
    else:
        warning('')
        elements["city"].config(text=f"city: {info[0]}")
        elements["temp"].config(text=f"tempeture: {info[1]}c")
        elements["contition"].config(text=f"condition: {info[2]}")
    
#manual grid setup for non-statis elements
elements["city_entry"].bind("<Return>", lambda event: refresh_info())
elements["city_entry"].grid(column=0, row=3)
elements["warning"].grid(column=0, row=4)
elements["submit"].config(command=refresh_info)
elements["submit"].grid(column=0, row=5)
elements["city"].grid(column=0, row=6)
elements["temp"].grid(column=0, row=7)
elements["contition"].grid(column=0, row=8)
