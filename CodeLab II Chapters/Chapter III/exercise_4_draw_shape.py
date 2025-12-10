from tkinter import *
from tkinter import ttk
import random

class DrawShape(Tk):
    def __init__(self):
        super().__init__()
        self.title("Draw Shape")
        self.resizable(False, False)

        # 3x3 layout
        # rows
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 0)
        self.rowconfigure(2, weight = 1)

        # columns
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 0)
        self.columnconfigure(2, weight = 1)
        
        Label(self, text = "Shape Generator", font = ('Helvetica', 15, 'bold')).grid(row = 0, column = 1, sticky = EW, pady = 10)
        self.canvas = Canvas(self, width = 400, height = 300, bg = 'white', highlightthickness = 2, highlightbackground = 'black')
        self.canvas.grid(row = 1, column = 1, padx = 20)
        self.shape_options = ShapeOptions(self, self.canvas)
        self.shape_options.grid(row = 2, column = 1, sticky = EW, padx = 20, pady = 20)

        self.mainloop()

class ShapeOptions(Frame):
    def __init__(self, parent, canvas):
        super().__init__(parent)

        # initialize
        self.canvas = canvas

        # 2x4 layout
        # rows 
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 1)

        # columns 
        for i in range(4):
            self.columnconfigure(i, weight = 1)

        Label(self, text = "Select a Shape to Draw on the Canvas", font = ('Helvetica', 10, 'bold')).grid(row = 0, column = 0, columnspan = 4, pady = (0, 10))
        
        self.oval = Button(self, text = "Oval", relief = "flat", bg = 'white', command = self.draw_oval)
        self.rect = Button(self, text = "Rectangle", relief = "flat", bg = 'white', command = self.draw_rect)
        self.square = Button(self, text = "Square", relief = "flat", bg = 'white', command = self.draw_square)
        self.triangle = Button(self, text = "Triangle", relief = "flat", bg = 'white',  highlightthickness = 2, highlightbackground = 'black', command = self.draw_triangle)

        self.oval.grid(row = 1, column = 0, ipadx = 10, ipady = 10)
        self.rect.grid(row = 1, column = 1, ipadx = 10, ipady = 10)
        self.square.grid(row = 1, column = 2, ipadx = 10, ipady = 10)
        self.triangle.grid(row = 1, column = 3, ipadx = 10, ipady = 10)

    def draw_oval(self):
        x = random.randint(10, 330)
        y = random.randint(10, 330)

        self.canvas.create_oval(x, y, x + 60, y + 40, fill = 'yellow', outline = 'black')

    def draw_rect(self):
        x = random.randint(10, 330)
        y = random.randint(10, 330)

        self.canvas.create_rectangle(x, y, x + 60, y + 40, fill = 'blue', outline = 'black')

    def draw_square(self):
        x = random.randint(10, 330)
        y = random.randint(10, 330)

        self.canvas.create_rectangle(x, y, x + 40, y + 40, fill = 'red', outline = 'black')

    def draw_triangle(self):
        x = random.randint(10, 330)
        y = random.randint(10, 330)

        self.canvas.create_polygon(x, y, x + 40, y - 60, x + 80, y, fill = 'green', outline = 'black')


if __name__ == "__main__":
    DrawShape()