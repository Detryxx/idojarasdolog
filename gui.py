from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont

textVar = {
    "title": "idojarasos app",

}


#setup
root = Tk()
root.title("idojaras app")
root.geometry("300x500")
frm = ttk.Frame(root, padding=30)
frm.grid()

title_font = tkfont.Font(size=25)

#UI
ttk.Label(frm,
        name="title",
        text=textVar["Title"], 
        font=title_font
        ).grid(column=0, row=0)

ttk.Label(frm, 
          text="Enter city name: "
        ).grid(column=0, row=2)

city_entry = ttk.Entry(frm,
        
        ).grid(column=0, row=3)

ttk.Button(frm, 
        text="Quit", 
        command=root.destroy
        ).grid(column=0, row=10)

def launch():
    root.mainloop()

if __name__ == "__main__": #testing UI
    launch()