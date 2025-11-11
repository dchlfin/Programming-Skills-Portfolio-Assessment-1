import tkinter
from tkinter import *
from tkinter import ttk

class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Calculator")
        self.propagate(False)

        # styles
        self.s = ttk.Style()
        self.s.configure('calc.TButton', font = ('Helvetica', 15))
        self.entry_font = {'font': ('Helvetica', 15)}

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)

        # widgets
        self.numbers = Numbers(self, self.entry_font)
        self.numbers.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5, sticky = EW)
    
        # calculation methods

        # call
        self.mainloop()

class Numbers(ttk.Frame):
    def __init__(self, parent, entry_font):
        super().__init__(parent)
        self.entry_font = entry_font

        # add num
        def add_num(num):
            entry.insert(0, num)

        # columns
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)

        # widgets
        entry = ttk.Entry(self, style = 'calc.TEntry', **entry_font).grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = (0, 5), sticky = EW)
        
        ttk.Button(self, text = "÷").grid(row = 0, column = 3)
        ttk.Button(self, text = "9").grid(row = 0, column = 2)
        ttk.Button(self, text = "8").grid(row = 0, column = 1)
        ttk.Button(self, text = "7").grid(row = 0, column = 0)
        ttk.Button(self, text = "x").grid(row = 1, column = 3)
        ttk.Button(self, text = "6").grid(row = 1, column = 2)
        ttk.Button(self, text = "5").grid(row = 1, column = 1)
        ttk.Button(self, text = "4").grid(row = 1, column = 0)
        ttk.Button(self, text = "-").grid(row = 2, column = 3)
        ttk.Button(self, text = "3").grid(row = 2, column = 2)
        ttk.Button(self, text = "2").grid(row = 2, column = 1)
        ttk.Button(self, text = "1").grid(row = 2, column = 0)
        ttk.Button(self, text = "+").grid(row = 3, column = 3)
        ttk.Button(self, text = "=").grid(row = 3, column = 2)
        ttk.Button(self, text = "0").grid(row = 3, column = 0, columnspan = 2, sticky = EW)

if __name__ == "__main__":
    Calculator()
