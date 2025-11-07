import tkinter 
from tkinter import *

main = Tk()
main.geometry("200x200")
main.resizable(False, False)
main.configure(bg="#B4E5FA")

welcome = Label(main, text = "Welcome!", font = ("Arial", 25, "bold")).pack()

main.mainloop()
