import tkinter as tk
from tkinter import ttk

class studentManager(tk.Tk):
    def __init__(self):

        # main setup
        super().__init__()
        self.title('Student Manager')

        # data 
        self.info = [
        {'code': 9357, 'name': 'Grace Johns', 'course_work': [10, 16, 4],'exam_score': 62},
        {'code': 6727, 'name': 'Rosie Gray', 'course_work': [12, 8, 16],'exam_score': 65},
        {'code': 4175, 'name': 'Hallie Morrison', 'course_work': [3, 15, 11],'exam_score': 64},
        {'code': 8439, 'name': 'Jake Hobbs', 'course_work': [10, 11, 10],'exam_score': 43},
        {'code': 3921, 'name': 'Arthur Kelly', 'course_work': [11, 7, 19],'exam_score': 93},
        {'code': 7724, 'name': 'Freddie Scott', 'course_work': [9, 11, 17],'exam_score': 63},
        {'code': 9413, 'name': 'Caleb Hunter', 'course_work': [7, 9, 20],'exam_score': 56},
        {'code': 3746, 'name': 'George Peterson', 'course_work': [14, 12, 13],'exam_score': 89},
        {'code': 9643, 'name': 'Ivy Cameron', 'course_work': [15, 19, 14],'exam_score': 96},
        {'code': 6055, 'name': 'Arlo Martin', 'course_work': [19, 12, 2],'exam_score': 55}
        ]   

        # search record
        self.clicked = tk.StringVar()


        # widgets 
        self.menu = Menu(self)
        self.menu.grid(row = 0, column = 0, padx = 50, pady = 10, sticky = 'EW')

        self.records = Records(self, self.info, self.clicked)
        self.records.grid(row = 1, column = 0, padx = 50, pady = 10, sticky = 'EW')

        self.record_display = RecordsDisplay(self)
        self.record_display.grid(row = 3, column = 0, columnspan = 4, padx = 50, pady = 10, sticky = 'NSEW')
        self.record_display.grid_propagate(False)

        # run
        self.mainloop()    

        # data handlers
    def formatted_info(self, student):
        cw, es = student['course_work'], student['exam_score']
        cw_total = sum(cw)
        pct = round((cw_total + es) / 160 * 100, 2)

        if pct < 40:
            grade = 'F'
        elif pct >= 40 and pct < 50:
            grade = 'D'
        elif pct >= 50 and pct < 60:
            grade = 'C'
        elif pct >= 60 and pct < 70:
            grade = 'B'
        else:
            grade = 'A'

        return f"""Name: {student['name']}
Number: {student['code']}
Coursework Total: {cw_total}
Exam Mark: {es}
Overall Percentage: {pct}%
Grade: {grade}"""

    def individual_record(self, student_name):
        student = None
        for s in self.info:
            if s['name'] == student_name:
                student = s
                break

        if student:
            record = self.formatted_info(student)
            self.record_display.display_record(record)

        else:
            self.record_display.display_record('Student not found.')

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text = 'Student Manager', font = ('Calibri', 15)).grid(row = 0, column = 0, columnspan = 3, pady = (0, 20))

        self.buttons()

    def buttons(self):
        records = ttk.Button(self, text = 'View All Student Records')
        records.grid(row = 1, column = 0, padx = (0,15), ipadx = 5, ipady = 5, sticky = 'W')
        high = ttk.Button(self, text = 'Show Highest Score')
        high.grid(row = 1, column = 1, ipadx = 5, ipady = 5, sticky = tk.W)
        low = ttk.Button(self, text = 'Show Lowest Score')
        low.grid(row = 1, column = 2, ipadx = 5, ipady = 5, padx = (15,0), sticky = tk.W)

class Records(ttk.Frame):
    def __init__(self, parent, info, clicked): 
        super().__init__(parent)
        self.info = info
        self.clicked = clicked
        self.widgets()
        
    def widgets(self):
        names = [student['name'] for student in self.info]
        ttk.Label(self, text = 'View Individual Student Record:', font = ('Arial', 11)).grid(row = 0, column = 0,  ipadx = 5, sticky = 'W')

        search_record = ttk.Combobox(self, width = 15, textvariable = self.clicked, values = names)
        search_record.grid(row = 0, column = 1, sticky = 'EW')
        view_record = ttk.Button(self, text = 'View Record', command = self.view_record)
        view_record.grid(row = 0, column = 3, padx = (10,0), ipadx = 5, ipady = 5)

    def view_record(self):
        selected_name = self.clicked.get()
        if selected_name:
            self.master.individual_record(selected_name)
        else:
            self.master.record_display.display_record('')

class RecordsDisplay(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width = 400, height = 125, borderwidth = 1, relief = 'groove')
        self.configure(style = 'Display.TFrame')

        s = ttk.Style()
        s.configure('Display.TFrame', background = 'white')

        self.record_label = tk.Label(self, text = '', background = 'white', justify = 'left', wraplength = 380)
        self.record_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'W')

        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def display_record(self, record_text):
        self.record_label.config(text = record_text)

def main():
    studentManager()

if __name__ == '__main__':
    main()


