import tkinter
from tkinter import *
from tkinter import ttk

class RegistrationPage(Tk):
    def __init__(self):
        super().__init__()

        # widgets
        self.title("Registration Page")
        self.geometry('338x600')
        self.resizable(False, False)
        self.configure(bg = 'white')
        
        # store image as instance variable
        self.bsu_banner = PhotoImage(file = 'assets/bsu-banner.png')
        Label(self, image=self.bsu_banner).pack(side = TOP)
        
        self.student_management = StudentManagement(self)
        self.student_management.pack(side = TOP, pady = 15)

        
        # run
        self.mainloop()

class StudentManagement(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width = 285, height = 484)
        
        s = ttk.Style()
        s.configure('StudentManagement.TFrame', background = '#F5F5F6')
        s.configure('StudentManagement.TLabel', background = '#F5F5F6', foreground = '#22263D')
        
        self.configure(style='StudentManagement.TFrame')
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 3)
        self.columnconfigure(2, weight = 1)
        self.grid_propagate(False)

        # headings
        Label(self, text = "Student Management", bg = '#F5F5F6', fg = '#22263D', font = ('Arial', 15, 'bold')).grid(row = 0, column = 0, columnspan = 3)
        Label(self, text = "New Student Registration", bg = '#F5F5F6', fg = '#22263D', font = ('Arial', 11, 'bold')).grid(row = 1, column = 1, pady = (0, 10))

        self.entries = Entries(self)
        self.entries.grid(row = 2, column = 0, columnspan = 3, sticky = EW)

        # form
        # ttk.Label(self, text = 'Student Name', style = 'Custom.TLabel').grid(row = 2, column = 1, sticky = EW)
        # ttk.Label(self, text = 'Mobile Number', style = 'Custom.TLabel').grid(row = 3, column = 1, sticky = EW)
        # ttk.Label(self, text = 'Email ID', style = 'Custom.TLabel').grid(row = 4, column = 1, sticky = EW)
        # ttk.Label(self, text = 'Home Address', style = 'Custom.TLabel').grid(row = 5, column = 1, sticky = EW)
        # ttk.Label(self, text = 'Course Enrolled', style = 'Custom.TLabel').grid(row = 6, column = 1, sticky = EW)
        # ttk.Entry(self, width=15).grid(row = 2, column = 2)
        
        # Label(self, text = "Student Management System", bg = '#F5F5F6', fg = '#22263D', font = ('Arial', 13, 'bold')).grid(row = 0, column = 0, columnspan = 3)
        # Label(self, text = "New Student Registration", bg = '#F5F5F6', fg = '#22263D', font = ('Arial', 11, 'bold')).grid(row = 1, column = 2, sticky = EW)
        # ttk.Label(self, text = 'Student Name', style = 'Custom.TLabel').grid(row = 2, column = 0, sticky = W, padx = 10, pady = 10)
        # ttk.Label(self, text = 'Mobile Number', style = 'Custom.TLabel').grid(row = 3, column = 0, sticky = E, padx = 10, pady = 10)
        # ttk.Label(self, text = 'Mobile Number', style = 'Custom.TLabel').grid(row = 4, column = 0, sticky = E, padx = 10, pady = 10)

class Entries(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width = 285, height = 170)

        s1 = ttk.Style()

        s1.configure('Entries.TFrame', background = "#454590")
        s1.configure('Entries.TLabel', background = '#F5F5F6', foreground = '#22263D')

        self.configure(style = 'Entries.TFrame')
        self.grid_propagate(False)


if __name__ == "__main__":
    RegistrationPage()
