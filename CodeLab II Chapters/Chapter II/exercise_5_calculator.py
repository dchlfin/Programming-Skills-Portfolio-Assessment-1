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
        def enter(num):
            current = entry.get()
            entry.delete(0, END)
            entry.insert(0, str(current) + str(num))

        # columns
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)

        # widgets
        entry = ttk.Entry(self, style = 'calc.TEntry', **entry_font).grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = (0, 5), sticky = EW)

        # row 1
        ttk.Button(self, text = "÷").grid(row = 1, column = 3)
        ttk.Button(self, text = "9", command = lambda: enter(9)).grid(row = 1, column = 2)
        ttk.Button(self, text = "8", command = lambda: enter(8)).grid(row = 1, column = 1)
        ttk.Button(self, text = "7", command = lambda: enter(7)).grid(row = 1, column = 0)
        
        # row 2
        ttk.Button(self, text = "×").grid(row = 2, column = 3)
        ttk.Button(self, text = "6", command = lambda: enter(6)).grid(row = 2, column = 2)
        ttk.Button(self, text = "5", command = lambda: enter(5)).grid(row = 2, column = 1)
        ttk.Button(self, text = "4", command = lambda: enter(4)).grid(row = 2, column = 0)
        
        # row 3
        ttk.Button(self, text = "-").grid(row = 3, column = 3)
        ttk.Button(self, text = "3", command = lambda: enter(3)).grid(row = 3, column = 2)
        ttk.Button(self, text = "2", command = lambda: enter(2)).grid(row = 3, column = 1)
        ttk.Button(self, text = "1", command = lambda: enter(1)).grid(row = 3, column = 0)
        
        # row 4
        ttk.Button(self, text = "+").grid(row = 4, column = 3)
        ttk.Button(self, text = "=").grid(row = 4, column = 2)
        ttk.Button(self, text = "0", command = lambda: enter(0)).grid(row = 4, column = 1, sticky = EW)
        ttk.Button(self, text = "c").grid(row = 4, column = 0, sticky = EW)

        # row 5
        ttk.Button(self, text = "%").grid(row = 5, column = 3, sticky = EW)

if __name__ == "__main__":
    Calculator()
