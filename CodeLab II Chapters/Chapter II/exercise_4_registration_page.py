import tkinter
from tkinter import *
from tkinter import ttk

class RegistrationPage(Tk):
    def __init__(self):
        super().__init__()

        # widgets
        self.title("Registration Page")
        self.geometry('338x650')
        # self.resizable(False, False)
        self.configure(bg = 'white')
        
        # store image as instance variable
        self.bsu_banner = PhotoImage(file = 'assets/bsu-banner.png')
        Label(self, image=self.bsu_banner).pack(side = TOP)

        # styles
        self.s = ttk.Style()
        self.s.configure('bg.TFrame', background = '#F5F5F6')
        self.s.configure('bg.TLabel', background = '#F5F5F6', foreground = '#22263D')
        self.s.configure('bg.TCheckbutton', background = '#F5F5F6', foreground = '#22263D')
        self.s.configure('bg.TRadiobutton', background = '#F5F5F6', foreground = '#22263D')
        self.s.configure('bg.Horizontal.TScale', background = '#F5F5F6')
        self.s.configure('bg.TButton', background = '#22263D')

        # main widget
        self.student_management = StudentManagement(self, self.s)
        self.student_management.pack(side = TOP, pady = 15)

        # run
        self.mainloop()

class StudentManagement(ttk.Frame):
    def __init__(self, parent, s):
        super().__init__(parent, width = 285, height = 545)
        
        self.s = s
        self.configure(style = 'bg.TFrame')
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 3)
        self.columnconfigure(2, weight = 1)
        self.grid_propagate(False)

        # headings
        Label(self, text = "Student Management", bg = '#F5F5F6', fg = '#22263D', font = ('Arial', 18, 'bold')).grid(row = 0, column = 0, columnspan = 3)
        Label(self, text = "New Student Registration", bg = '#F5F5F6', fg = '#22263D', font = ('Arial', 11, 'bold')).grid(row = 1, column = 1, pady = (0, 10))

        # widget
        self.entries = Entries(self, self.s)
        self.entries.grid(row = 2, column = 1, sticky = E, pady = (10, 0))
        self.courses = Courses(self, self.s)
        self.courses.grid(row = 3, column = 1, sticky = E, pady = (5, 0))
        self.languages = Languages(self, s)
        self.languages.grid(row = 4, column = 1, sticky = E, pady = (10, 0))
        self.rate = Rate(self, s)
        self.rate.grid(row = 7, column = 1, pady = (5, 5))
        self.endform = EndForm(self)
        self.endform.grid(row = 8, column = 1, columnspan = 3)
        

class Entries(ttk.Frame):
    def __init__(self, parent, s):
        super().__init__(parent, width = 252, height = 200)
        self.s = s

        self.configure(style = 'bg.TFrame')
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 5)
        self.grid_propagate(False)

        # labels
        ttk.Label(self, text = "Student Name", style = 'bg.TLabel').grid(row = 0, column = 0, sticky = E, pady = 10)
        ttk.Label(self, text = "Mobile Number", style = 'bg.TLabel').grid(row = 1, column = 0, sticky = E, pady = 10)
        ttk.Label(self, text = "Email ID", style = 'bg.TLabel').grid(row = 2, column = 0, sticky = E, pady = 10)
        ttk.Label(self, text = "Home Address", style = 'bg.TLabel').grid(row = 3, column = 0, sticky = E, pady = 10)
        ttk.Label(self, text = "Gender", style = 'bg.TLabel').grid(row = 4, column = 0, sticky = E, pady = 10)

        # entries
        Entry(self, bg = '#ADAEB7', width = 24, relief = FLAT).grid(row = 0, column = 1, sticky = E, ipady = 4)
        Entry(self, bg = '#ADAEB7', width = 24, relief = FLAT).grid(row = 1, column = 1, sticky = E, ipady = 4)
        Entry(self, bg = '#ADAEB7', width = 24, relief = FLAT).grid(row = 2, column = 1, sticky = E, ipady = 4)
        Entry(self, bg = '#ADAEB7', width = 24, relief = FLAT).grid(row = 3, column = 1, sticky = E, ipady = 4)

        # combobox
        gender = ["Male", "Female"]

        # style combobox ?
        ttk.Combobox(self, values = gender, width = 21).grid(row = 4, column = 1, sticky = E, ipady = 4) 

class Courses(ttk.Frame):
    def __init__(self, parent, s): #s
        super().__init__(parent, width = 252, height = 80)
        self.s = s
        self.configure(style = 'bg.TFrame')

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 5)
        self.grid_propagate(False)

        # courses
        ttk.Label(self, text = "Course Enrolled", style = 'bg.TLabel').grid(row = 0, column = 0, sticky = W)
        ttk.Radiobutton(self, text = 'BSc CC', style = 'bg.TRadiobutton').grid(row = 0, column = 1, sticky = W)
        ttk.Radiobutton(self, text = 'BSc CY', style = 'bg.TRadiobutton').grid(row = 1, column = 1, sticky = W)
        ttk.Radiobutton(self, text = 'BSc PSY', style = 'bg.TRadiobutton').grid(row = 2, column = 1, sticky = W)
        ttk.Radiobutton(self, text = 'BA & BM', style = 'bg.TRadiobutton').grid(row = 3, column = 1, sticky = W)

class Languages(ttk.Frame):
    def __init__(self, parent, s):
        super().__init__(parent, width = 252, height = 55)
        self.s = s
        self.configure(style = 'bg.TFrame')

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 0)
        self.columnconfigure(2, weight = 1)
        self.grid_propagate(False)

        # widgets
        ttk.Label(self, text = "Languages known", style = 'bg.TLabel').grid(row = 0, column = 0, sticky = W, pady = 4)
        ttk.Checkbutton(self, text = "English", style = 'bg.TCheckbutton').grid(row = 0, column = 1, pady = 4)
        ttk.Checkbutton(self, text = "Tagalog", style = 'bg.TCheckbutton').grid(row = 0, column = 2, pady = 4)
        ttk.Checkbutton(self, text = "Hindu/Urdu", style = 'bg.TCheckbutton').grid(row = 1, column = 1, columnspan = 2, sticky = W)
    
class Rate(ttk.Frame):
    def __init__(self, parent, s):
        super().__init__(parent, width = 252, height = 50)

        self.s = s
        self.configure(style = 'bg.TFrame')
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.grid_propagate(False)

        # widgets
        ttk.Label(self, text = "Rate Your English Communication Skills", style = 'bg.TLabel').grid(row = 0, column = 0, columnspan = 2)
        ttk.Scale(self, orient = HORIZONTAL, style = 'bg.Horizontal.TScale').grid(row = 1, column = 0, columnspan = 2, pady = 4)
        
class EndForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width = 285, height = 50)

        s = ttk.Style()
        s.configure('endform.TFrame', background = '#F5F5F6')

        self.configure(style = 'endform.TFrame')
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.grid_propagate(False)

        Button(self, text = "Submit", bg = '#22263D', fg = '#F5F5F6', relief = FLAT, font = ('Arial', 11)).grid(row = 0, column = 0, ipadx = 25, ipady = 5)
        Button(self, text = "Clear", bg = '#22263D', fg = '#F5F5F6', relief = FLAT, font = ('Arial', 11)).grid(row = 0, column = 1, ipadx = 30, ipady = 5)

if __name__ == "__main__":
    RegistrationPage()
