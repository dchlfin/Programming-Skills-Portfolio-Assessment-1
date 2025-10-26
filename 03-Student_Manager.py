import tkinter as tk
from tkinter import ttk

main = tk.Tk()
main.title("Student Manager")

info = [
    {"code": 9357, "name": "Grace Johns", "course_work": [10, 16, 4],"exam_score": 62},
    {"code": 6727, "name": "Rosie Gray", "course_work": [12, 8, 16],"exam_score": 65},
    {"code": 4175, "name": "Hallie Morrison", "course_work": [3, 15, 11],"exam_score": 64},
    {"code": 8439, "name": "Jake Hobbs", "course_work": [10, 11, 10],"exam_score": 43},
    {"code": 3921, "name": "Arthur Kelly", "course_work": [11, 7, 19],"exam_score": 93},
    {"code": 7724, "name": "Freddie Scott", "course_work": [9, 11, 17],"exam_score": 63},
    {"code": 9413, "name": "Caleb Hunter", "course_work": [7, 9, 20],"exam_score": 56},
    {"code": 3746, "name": "George Peterson", "course_work": [14, 12, 13],"exam_score": 89},
    {"code": 9643, "name": "Ivy Cameron", "course_work": [15, 19, 14],"exam_score": 96},
    {"code": 6055, "name": "Arlo Martin", "course_work": [19, 12, 2],"exam_score": 55}
]

record = None
grade = None

# individual record overrides the viewAll

def viewAll():
    global record
    global grade 
    for student in info:
        cw, es = student["course_work"], student["exam_score"]
        cw_total = sum(cw)
        # pct = round(((cw_total + es) / 160) * 100)
        pct = round((cw_total + es) / 160 * 100, 2)
        
        if pct < 40:
            grade = "F"
        elif pct >= 40 and pct < 50:
            grade = "D"
        elif pct >= 50 and pct < 60:
            grade = "C"
        elif pct >= 60 and pct < 70:
            grade = "B"
        elif pct >= 70:
            grade = "A"

        details = f"Name: {student["name"]}\nNumber: {student["code"]}\nCoursework Total: {cw_total}\nExam Mark: {es}\nOverall Percentage: {pct}%\nGrade: {grade}\n"

        if record:
                record.grid_forget()

        for r in range(10):
            record = tk.Label(f3, text = details, justify = "left", background = "white")
            record.grid(row = r, sticky = "W", pady = (0, 5))
      
        

def selected():
    global record
    global grade
    name = clicked.get()
    for student in info:
        if student["name"] == name:
            cw, es = student.get("course_work"), student.get("exam_score")
            cw_total = sum(cw)
            # pct = round(((cw_total + es) / 160) * 100)
            pct = round((cw_total + es) / 160 * 100, 2)
            
            if pct < 40:
                grade = "F"
            elif pct >= 40 and pct < 50:
                grade = "D"
            elif pct >= 50 and pct < 60:
                grade = "C"
            elif pct >= 60 and pct < 70:
                grade = "B"
            elif pct >= 70:
                grade = "A"

            details = f"Name: {student.get("name")}\nNumber: {student.get("code")}\nCoursework Total: {cw_total}\nExam Mark: {es}\nOverall Percentage: {pct}%\nGrade: {grade}"

            if record:
                record.grid_forget()

            record = tk.Label(f3, text = details, justify = "left", background = "white")
            record.grid(row = 0, sticky = "W", pady = (0, 5))
            break


clicked = tk.StringVar()

names = [student["name"] for student in info]

# first frame
f1 = tk.Frame(main, width = 500, height = 100)
f1.grid(row = 0, column = 0, padx = 50, pady = 10, sticky = "EW", )

l1 = ttk.Label(f1, text = "Student Manager", font = (11)).grid(row = 0, column = 0, columnspan = 3, pady = (0,20))

# buttons
records = ttk.Button(f1, text = "View All Student Records", command = viewAll).grid(row = 1, column = 0, padx = (0,15), ipadx = 5, ipady = 5, sticky = "W")
high = ttk.Button(f1, text = "Show Highest Score").grid(row = 1, column = 1, ipadx = 5, ipady = 5, sticky = tk.W,)
low = ttk.Button(f1, text = "Show Lowest Score").grid(row = 1, column = 2, ipadx = 5, ipady = 5, padx = (15,0), sticky = tk.W,)

# second frame
f2 = tk.Frame(main, width = 500, height = 200)
f2.grid(row = 1, column = 0, padx = 50, pady = 10, sticky = "EW")
l2 = ttk.Label(f2, text = "View Individual Student Record:", font = ('Arial', 11)).grid(row = 0, column = 0,  ipadx = 5, sticky = "W")

# combobox
names_combo = ttk.Combobox(f2, width = 15, textvariable = clicked, values = names)
names_combo.grid(row = 0, column = 1, sticky = "EW")

view_record = ttk.Button(f2, text = "View Record", command = selected).grid(row = 0, column = 3, padx = (10, 0), ipadx = 5, ipady = 5)

# listbox = ttk.Listbox(f2, height = 7, listvariable="")
f3 = ttk.Frame(main, width = 400, height = 125, borderwidth = 1, relief = "groove")
# sb = tk.Scrollbar(f3, orient = "vertical")
# sb.grid(row = 0, column = 1, sticky = "NS")
f3.grid(row = 2, column = 0, columnspan = 4, padx = 50, pady = 10, sticky = "NSEW")
f3.grid_propagate(False)

# sb = tk.Scrollbar(f3, orient = "vertical")
# sb.grid(sticky = "E")
# cv = tk.Canvas(f3, bd = 0, highlightthickness = 0, yscrollcommand = sb.set)
# cv.grid(row = 0, column = 0, sticky = "E")

# cv.xview_moveto(0)
# cv.yview_moveto(0)

s = ttk.Style()
s.configure('TFrame', background = 'white')

main.mainloop()
