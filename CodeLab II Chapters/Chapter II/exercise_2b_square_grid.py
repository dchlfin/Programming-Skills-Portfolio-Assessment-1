import tkinter
from tkinter import *

main = Tk()
main.title('Square Grid')
main.resizable(True, True)

# frames
f1 = Frame(main, relief = 'sunken', bd = 5)
f2 = Frame(main, relief = 'sunken', bd = 5)

# labels
a_label = Label(f1, text = 'A', bg = '#22263D', fg = 'white')
b_label = Label(f1, text = 'B', bg = 'white')
c_label = Label(f2, text = 'C', bg = 'white')
d_label = Label(f2, text = 'D', bg = '#22263D', fg = 'white')

# pack
f1.pack(side = LEFT, expand = True, fill = BOTH)
f2.pack(side = LEFT, expand = True, fill = BOTH)
a_label.pack(side = TOP, expand = True, fill = BOTH)
c_label.pack(side = TOP, expand = True, fill = BOTH)
b_label.pack(side = BOTTOM, expand = True, fill = BOTH)
d_label.pack(side = BOTTOM, expand = True, fill = BOTH)

main.mainloop()