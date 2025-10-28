import tkinter as tk
from tkinter import ttk

class studentManager(tk.Tk):
    def __init__(self):

        # main setup
        super().__init__()
        self.title('Student Manager')

        # data 
        self.info = [
        {'code': 1001, 'name': 'Ava Williams', 'course_work': [13, 15, 17],'exam_score': 70},
        {'code': 1002, 'name': 'Liam Thompson', 'course_work': [11, 13, 15],'exam_score': 60},
        {'code': 1003, 'name': 'Sophia Brown', 'course_work': [17, 18, 19],'exam_score': 80},
        {'code': 1004, 'name': 'Noah Wilson', 'course_work': [9, 11, 13],'exam_score': 50},
        {'code': 1005, 'name': 'Mia Garcia', 'course_work': [14, 13, 12],'exam_score': 65},
        {'code': 1006, 'name': 'James Lee', 'course_work': [14, 16, 18],'exam_score': 75},
        {'code': 1007, 'name': 'Isabella Scott', 'course_work': [12, 14, 16],'exam_score': 68},
        {'code': 1008, 'name': 'Mason Harris', 'course_work': [13, 15, 17],'exam_score': 72},
        {'code': 1009, 'name': 'Lily Adams', 'course_work': [11, 13, 14],'exam_score': 48},
        {'code': 1010, 'name': 'Ethan Moore', 'course_work': [15, 17, 19],'exam_score': 78}
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
        es = self.exam_score(student)
        cw_total = self.course_work_total(student)
        overall_marks = self.overall_marks(student)
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

    def overall_marks(self, student):
        return self.course_work_total(student) + self.exam_score(student)
    
    def course_work_total(self, student):
        return sum(student['course_work'])
    
    def exam_score(self, student):
        return student['exam_score']

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

    def all_records(self):
        records = []
        for student in self.info:
            records.append(self.formatted_info(student))
        
        all_records = "\n\n".join(records)
        self.record_display.display_record(all_records)

    def high_OR_low(self, value):
        if value == True:
            student = self.formatted_info(max(self.info, key = self.overall_marks))
        else:
            student = self.formatted_info(min(self.info, key = self.overall_marks))

        self.record_display.display_record(student)

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text = 'Student Manager', font = ('Arial', 15)).grid(row = 0, column = 0, columnspan = 3, pady = (0, 20))

        self.buttons()

    def buttons(self):
        self.value = False
        
        records = ttk.Button(self, text = 'View All Student Records', command = self.view_all)
        records.grid(row = 1, column = 0, padx = (0,15), ipadx = 5, ipady = 5, sticky = 'W')
        high = ttk.Button(self, text = 'Show Highest Score', command = self.view_high)
        high.grid(row = 1, column = 1, ipadx = 5, ipady = 5, sticky = tk.W)
        low = ttk.Button(self, text = 'Show Lowest Score', command = self.view_low)
        low.grid(row = 1, column = 2, ipadx = 5, ipady = 5, padx = (15,0), sticky = tk.W)

    def view_all(self):
        self.master.all_records()

    def view_high(self):
        self.value = True
        self.master.high_OR_low(self.value)

    def view_low(self):
        self.value = False
        self.master.high_OR_low(self.value)

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
        s.configure('Vertical.TScrollbar', background = 'white')

        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        # canvas
        self.canvas = tk.Canvas(self, bg = 'white', highlightbackground = 'white')
        self.canvas.grid(row = 0, column = 0, sticky = "NSEW")

        # scrollable frame
        self.scrollable = tk.Frame(self.canvas, bg = 'white')

        # scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient = 'vertical', command = self.canvas.yview)
        self.scrollbar_position = self.scrollbar.get()
        
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 0)

        # attach scrollbar to canvas
        self.canvas.configure(yscrollcommand = self.scrollbar.set)

        self.canvas.create_window((0,0), window = self.scrollable, anchor = "nw")

    def display_record(self, record_text):
        self.scrollbar.grid_forget()
        self.canvas.yview_moveto(0)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

        for widget in self.scrollable.winfo_children():
            widget.destroy()

        record_label = tk.Label(self.scrollable, text = record_text, background = 'white', justify = 'left', wraplength = 380)
        record_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'W')

def main():
    studentManager()

if __name__ == '__main__':
    main()
