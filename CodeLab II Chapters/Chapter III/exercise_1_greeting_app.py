import tkinter
from tkinter import *
from tkinter import ttk

class Greeting(Tk):
    def __init__(self):
        super().__init__()

        self.title("Greeting App")
        self.resizable(False, False)

        # layout configuration 
        for i in range(2):
            self.rowconfigure(i, weight = 1)

        # style
        self.s = ttk.Style()
        self.s.configure('Greeting.TFrame', background = 'white')

        # widgets
        self.input_frame = InputFrame(self, self.s)
        self.input_frame.grid(row = 0, sticky = EW, pady = (0,5))

        # run
        self.mainloop()

class InputFrame(ttk.Frame):
    def __init__(self, parent, s):
        super().__init__(parent) 
        self.s = s
        self.configure(style = 'Greeting.TFrame')   

        # layout configuration
        # columns
        for i in range(2):
            self.columnconfigure(i, weight = 1)

        # rows 
        for i in range(5):
            self.rowconfigure(i, weight = 1)
        
        Label(self, text = "Greeting App", font = ('Helvetica', 15, 'bold'), background = "#CBECFF", foreground = "#03B1EE").grid(row = 0, column = 0, columnspan = 3, pady = (0,5), sticky = EW)

        # name
        Label(self, text = "Enter your Name:", background = 'white').grid(row = 1, column = 0, ipadx = 5, pady = (10, 5), sticky = E)
        name = ttk.Entry(self)
        name.grid(row = 1, column = 1, padx = 5, pady = (0, 5), sticky = EW)

        # color
        Label(self, text = "Select a Color:", background = 'white').grid(row = 2, column = 0, padx = 5, pady = (0, 5),sticky = E)

        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
        color = ttk.Combobox(self, values = colors)
        color.grid(row = 2, column = 1, padx = 5, pady = (0, 5), sticky = EW)

        # update greeting
        Button(self, text = "Update Greeting", font = ('Helvetica', 9,  'bold'), background = '#03B1EE', foreground = '#CBECFF', relief = FLAT).grid(row = 4, column = 0, columnspan = 3, pady = 10, ipadx = 5, ipady = 5)

        # call
        self.display_frame = DisplayFrame(self)
        self.display_frame.grid(row = 3, column = 0, columnspan = 3, padx = 5, pady = (10, 0), sticky = EW)

class DisplayFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, height = 100, highlightthickness = 1, highlightbackground = 'gray')

        # layout configuration
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.grid_propagate(False)

        display = Label(self, text = "", font = ('Helvetica', 12))
        display.grid(row = 0, rowspan = 2, column = 0, columnspan = 2, sticky = NSEW)

if __name__ == "__main__":
    Greeting()
