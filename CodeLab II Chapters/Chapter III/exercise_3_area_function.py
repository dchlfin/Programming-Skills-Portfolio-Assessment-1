from tkinter import *
from tkinter import ttk
import math

class AreaFunc(Tk):
    def __init__(self):
        super().__init__()
        self.title("Area Calculator")
        self.resizable(False, False)

        self.tabs = ttk.Notebook(self)
        self.tabs.grid(row = 0, column = 0, padx = 5, pady = 10)

        # initialize tabs
        self.circle = CircleArea(self.tabs)
        self.rectangle = RectangleArea(self.tabs)
        self.square = SquareArea(self.tabs)

        # add tabs
        self.tabs.add(self.circle, text = "Circle Area")
        self.tabs.add(self.rectangle, text = "Rectangle Area")
        self.tabs.add(self.square, text = "Square Area")
    
        self.mainloop()

class CircleArea(Frame):
    def __init__(self, parent):
        super().__init__(parent, width = 250, height = 250, bg = 'white')

        # 3x2 layout
        for i in range(4):
            self.rowconfigure(i, weight = 1)

        for i in range(2):
            self.columnconfigure(i, weight = 1)

        self.grid_propagate(False)

        Label(self, text = "Area of a Circle", font = ('Helvetica', 11, 'bold'), bg = 'white').grid(row = 0, column = 0, columnspan = 2, pady = 5)

        # entries
        Label(self, text = "Radius (r)", bg = 'white').grid(row = 1, column = 0, sticky = E)
        self.radius = ttk.Entry(self)
        self.radius.grid(row = 1, column = 1, sticky = EW, padx = 5)

        Label(self, text = "Area (a)", bg = 'white').grid(row = 2, column = 0, sticky = E)
        self.c_area = Label(self, text = "")
        self.c_area.grid(row = 2, column = 1, sticky = EW, padx = 5)

        # calc button
        self.calc_c_area = ttk.Button(self, text = "Calculate Area", command = self.calculate_circle_area)
        self.calc_c_area.grid(row = 3, column = 1, sticky = NE, padx = 5)

    def calculate_circle_area(self):
        try:
            radius = int(self.radius.get())
            self.c_area.config(text = f"{round(math.pi * (radius * radius), 2)}", anchor = "w")
        except ValueError:
            self.c_area.config(text = "Invalid radius", anchor = "w")

class RectangleArea(Frame):
    def __init__(self, parent):
        super().__init__(parent, width = 250, height = 250, bg = 'white')

        # 4x2 layout
        for i in range(5):
            self.rowconfigure(i, weight = 1)

        for i in range(2):
            self.columnconfigure(i, weight = 1)

        self.grid_propagate(False)

        Label(self, text = "Area of a Rectangle", font = ('Helvetica', 11, 'bold'), bg = 'white').grid(row = 0, column = 0, columnspan = 2, pady = 5)

        # entries
        Label(self, text = "Length (a)", bg = 'white').grid(row = 1, column = 0, sticky = E)
        self.length = ttk.Entry(self)
        self.length.grid(row = 1, column = 1, sticky = EW, padx = 5)

        Label(self, text = "Width (b)", bg = 'white').grid(row = 2, column = 0, sticky = E)
        self.width = ttk.Entry(self)
        self.width.grid(row = 2, column = 1, sticky = EW, padx = 5)

        Label(self, text = "Area (a)", bg = 'white').grid(row = 3, column = 0, sticky = E)
        self.r_area = Label(self, text = "")
        self.r_area.grid(row = 3, column = 1, sticky = EW, padx = 5)

        # calc button
        self.calc_r_area = ttk.Button(self, text = "Calculate Area", command = self.calculate_rect_area)
        self.calc_r_area.grid(row = 4, column = 1, sticky = NE, padx = 5)

    def calculate_rect_area(self):
        try:
            length = int(self.length.get())
            width = int(self.width.get())
            
            self.r_area.config(text = f"{width * length}", anchor = "w")

        except:
            self.r_area.config(text = "Invalid length/width", anchor = "w")
            
class SquareArea(Frame):
    def __init__(self, parent):
        super().__init__(parent, width = 250, height = 250, bg = 'white')

        for i in range(4):
            self.rowconfigure(i, weight = 1)

        for i in range(2):
            self.columnconfigure(i, weight = 1)

        self.grid_propagate(False)

        Label(self, text = "Area of a Square", font = ('Helvetica', 11, 'bold'), bg = 'white').grid(row = 0, column = 0, columnspan = 2, pady = 5)

        # entries
        Label(self, text = "Side (s)", bg = 'white').grid(row = 1, column = 0, sticky = E)
        self.side = ttk.Entry(self)
        self.side.grid(row = 1, column = 1, sticky = EW, padx = 5)

        Label(self, text = "Area (a)", bg = 'white').grid(row = 2, column = 0, sticky = E)
        self.s_area = Label(self, text = "")
        self.s_area.grid(row = 2, column = 1, sticky = EW, padx = 5)

        # calc button
        self.calc_s_area = ttk.Button(self, text = "Calculate Area", command = self.calculate_square_area)
        self.calc_s_area.grid(row = 3, column = 1, sticky = NE, padx = 5)

    def calculate_square_area(self):
        try:
            side = int(self.side.get())
            self.s_area.config(text = f"{side ** 2}", anchor = "w")
        except:
            self.s_area.config(text = "Invalid side", anchor = "w")
 
if __name__ == "__main__":
    AreaFunc()