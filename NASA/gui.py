from cgitb import text
from script import *
from tkinter import *
import time 

window = Tk()
window.title("Space Weather Notifier")
window['bg']='#2C2F33'
window.geometry("300x300")

bg = PhotoImage(file="Infographic2.png")


def popup():
   top= Toplevel(window)
   top.geometry("500x700")
   top.title("Infographic")
   Label(top, image=bg).pack()

Label(window, text="Show Infographic", font=('Helvetica 18 bold'), bg = '#2C2F33', fg = 'white', height = 1).pack(pady=20)
Button(window, text= "Open", command= popup).pack()

Label(window, text="Start Notifications",font=('Helvetica 18 bold'), bg = '#2C2F33', fg = 'white').pack(pady=20)
b = Button(window, text= "Start", command= lambda: weather(window))
b.pack()

Label(text="You get space weather updates via notifications\n every 30 minutes!", height = 4, bg='#2C2F33', fg = 'white').pack()
Label(text="This application will close automatically after\n 24 hours.", bg='#2C2F33', fg = 'white').pack()

window.mainloop()



