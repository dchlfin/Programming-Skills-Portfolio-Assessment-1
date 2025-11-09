import tkinter 
from tkinter import * 

main = Tk()
main.title("Login Page")

# widgets
user = Label(main, text = "Username:")
password = Label(main, text = "Password:")
user_entry = Entry(main)
pw_entry = Entry(main)
login = Button(main, text = "Login")

user.grid(row = 0, column = 0, padx = 5, pady = 5)
password.grid(row = 1, column = 0, padx = 5, pady = 5)
user_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
pw_entry.grid(row = 1, column = 1, padx = 5, pady = 5)
login.grid(row = 2, column = 1, sticky = E, padx = 5, pady = 5)

main.mainloop()