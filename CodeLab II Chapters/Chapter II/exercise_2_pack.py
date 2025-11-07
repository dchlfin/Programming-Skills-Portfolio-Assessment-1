import tkinter
from tkinter import *

main = Tk()
main.title("GUI Pack Example")
main.geometry("400x200")
# main.resizable(False, False)

# widgets
label_a = Button(main, text = "A", bg = "red", relief = "groove", bd = 5)
label_b = Label(main, text = "B", bg = "yellow", relief = "raised", padx = 40)
label_c = Label(main, text = "C", bg = "blue", padx = 40)
label_d = Label(main, text = "D", bg = "white", padx = 40)

# pack
label_a.pack(side = TOP, expand = True, fill = X)
label_b.pack(side = BOTTOM)
label_d.pack(side = RIGHT, anchor = S)
label_c.pack(side = RIGHT, anchor = S, expand = True)

main.mainloop()