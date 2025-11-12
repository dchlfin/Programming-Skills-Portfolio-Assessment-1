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

        # widgets
        self.input_frame = InputFrame(self)
        self.input_frame.grid(row = 0, sticky = EW, pady = (0,5))

        # run
        self.mainloop()

class InputFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, height = 100, highlightthickness = 1, highlightbackground = 'gray')
        
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
        self.name = ttk.Entry(self)
        self.name.grid(row = 1, column = 1, padx = 5, pady = (0, 5), sticky = EW)

        # color
        Label(self, text = "Select a Color:", background = 'white').grid(row = 2, column = 0, padx = 5, pady = (0, 5),sticky = E)

        # combobox
        self.colors_info = [
            {'name': 'red', 'hex_bg': '#FF9E97', 'hex_fg': '#DC3E4D'},
            {'name': 'orange', 'hex_bg': '#FFDBA7', 'hex_fg': '#E8A25C'},
            {'name': 'yellow', 'hex_bg': '#FFF6BF', 'hex_fg': '#F4CC0A'},
            {'name': 'green', 'hex_bg': '#E9FFDB', 'hex_fg': '#80CA9F'},
            {'name': 'blue', 'hex_bg': '#CBECFF', 'hex_fg': '#03B1EE'},
            {'name': 'purple', 'hex_bg': '#EBCFFF', 'hex_fg': '#7544B4'}
        ]

        colors = [color['name'] for color in self.colors_info]

        self.color = ttk.Combobox(self, values = colors)
        self.color.grid(row = 2, column = 1, padx = 5, pady = (0, 5), sticky = EW)

        # update greeting
        Button(self, text = "Update Greeting", font = ('Helvetica', 9,  'bold'), background = '#03B1EE', foreground = '#CBECFF', relief = FLAT, command = self.update_greeting).grid(row = 4, column = 0, columnspan = 3, pady = 10, ipadx = 5, ipady = 5)

        # call
        self.display_frame = DisplayFrame(self)
        self.display_frame.grid(row = 3, column = 0, columnspan = 3, padx = 5, pady = (10, 0), sticky = EW)

    def update_greeting(self):
        n = self.name.get().strip()
        c = self.color.get()

        if not n: 
            n = "User"

        for color in self.colors_info:
            if color['name'] == c:
                self.display_frame.display.config(text = f"Hello, {n.capitalize()}!", background = color['hex_bg'], foreground = color['hex_fg'])
                break
        else:
            self.display_frame.display.config(text = f"Hello {n.capitalize()}!", background = '#f0f0f0', foreground = 'black')

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
