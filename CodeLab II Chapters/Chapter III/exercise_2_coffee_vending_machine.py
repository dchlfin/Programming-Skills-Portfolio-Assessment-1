from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class CoffeeVendingMachine(Tk):
    def __init__(self):
        super().__init__()
        self.title("Coffee Vending Machine")
        self.resizable(False, False)

        # 3x2 layout configuration
        ## row configuration
        for i in range(3):
            self.rowconfigure(i, weight = 1)

        ## column configuration
        for i in range(2):
            self.columnconfigure(i, weight = 1)

        # styles
        self.s = ttk.Style()
        self.s.configure('bg.Vertical.TScale', background = '#f7ebdf')
        self.s.configure('Vertical.TScrollbar', background = '#f7ebdf')

        # string variables - options
        self.milk_clicked = StringVar()
        self.sugar_clicked = StringVar()
        self.strength_clicked = StringVar()
        self.toppings_clicked = StringVar()

        # widgets
        Label(self, text = "Coffee Vending Machine", background = '#110703', foreground = 'white', font = ('Helvetica', 15, 'bold')).grid(row = 0, column = 0, columnspan = 3, sticky = EW)
        
        # frames
        self.details = Details(self, self.s, self.milk_clicked, self.sugar_clicked, self.strength_clicked, self.toppings_clicked)
        self.details.grid(row = 1, rowspan = 3, column = 1, sticky = N+E+W)
        self.products = Products(self)
        self.products.grid(row = 1, column = 0, sticky = EW)
        self.options = Options(self, self.s, self.milk_clicked, self.sugar_clicked, self.strength_clicked, self.toppings_clicked)
        # self.options = Options(self, self.s)
        self.options.grid(row = 2, column = 0, sticky = EW)

        self.mainloop()

# style classes
class regLabel(Label):
    def __init__(self, parent, text, **kw):
        default = {'font': ('Helvetica', 10, 'bold'), 'background': '#f7ebdf'}
        default.update(kw)
        super().__init__(parent, text = text, **default)

class Products(Frame):
    def __init__(self, parent):
        super().__init__(parent, width = 450, height = 450, background = '#f7ebdf')

        # photo initialization
        self.esp = Image.open('assets/espresso.png').resize((100, 100))
        self.esp = ImageTk.PhotoImage(self.esp)
        self.am = Image.open('assets/americano.png').resize((100, 100))
        self.am = ImageTk.PhotoImage(self.am)
        self.cppcno = Image.open('assets/cappuccino.png').resize((100, 100))
        self.cppcno = ImageTk.PhotoImage(self.cppcno)
        self.ltt = Image.open('assets/latte.png').resize((100, 100))
        self.ltt = ImageTk.PhotoImage(self.ltt)
        self.mch = Image.open('assets/mocha.png').resize((100, 100))
        self.mch = ImageTk.PhotoImage(self.mch)
        self.mchto = Image.open('assets/macchiato.png').resize((100, 100))
        self.mchto = ImageTk.PhotoImage(self.mchto)
        self.blckffee = Image.open('assets/black-coffee.png').resize((100, 100))
        self.blckffee = ImageTk.PhotoImage(self.blckffee)

        # 3x4 layout configuration 
        ## row configuration
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)

        ## column configuration
        for i in range(3):
            self.columnconfigure(i, weight = 1)
        
        self.grid_propagate(False)

        # widgets
        Label(self, text = "PRODUCTS", background = '#230f08', foreground = 'white').grid(row = 0, column = 0, columnspan = 3, sticky = N+E+W)

        # espresso
        self.esp_frame = Frame(self)
        self.esp_frame.grid(row = 1, column = 0, sticky = N)
        self.esp_icon = Button(self.esp_frame, image = self.esp, relief = FLAT, background = '#f7ebdf', command = lambda: self.coffee_selection("Espresso", "2.50"))
        self.esp_icon.grid(row = 0, column = 0, sticky = N)
        self.espresso = Button(self.esp_frame, text = """Espresso
$2.50""", relief = FLAT, background = '#f7ebdf')
        self.espresso.grid(row = 1, column = 0, sticky = EW)

        # americano
        self.am_frame = Frame(self)
        self.am_frame.grid(row = 1, column = 1, sticky = N)
        self.am_icon = Button(self.am_frame, image = self.am, relief = FLAT, background = '#f7ebdf', command = lambda: self.coffee_selection("Americano", "3.00"))
        self.am_icon.grid(row = 0, column = 0, sticky = N)
        self.americano = Button(self.am_frame, text = """Americano
$3.00""", relief = FLAT, background = '#f7ebdf')
        self.americano.grid(row = 1, column = 0, sticky = EW)

        # cappuccino
        self.cppcno_frame = Frame(self)
        self.cppcno_frame.grid(row = 1, column = 2, sticky = N)
        self.cppcno_icon = Button(self.cppcno_frame, image = self.cppcno, relief = FLAT, background = '#f7ebdf', command = lambda: self.coffee_selection("Cappuccino", "3.50"))
        self.cppcno_icon.grid(row = 0, column = 0, sticky = N)
        self.cappuccino = Button(self.cppcno_frame, text = """Cappuccino
$3.50""",relief = FLAT, background = '#f7ebdf')
        self.cappuccino.grid(row = 1, column = 0, sticky = EW)

        # latte
        self.ltt_frame = Frame(self)
        self.ltt_frame.grid(row = 2, column = 0, sticky = N)
        self.ltt_icon = Button(self.ltt_frame, image = self.ltt, relief = FLAT, background = '#f7ebdf', command = lambda: self.coffee_selection("Latte", "4.00"))
        self.ltt_icon.grid(row = 0, column = 0, sticky = N)
        self.latte = Button(self.ltt_frame, text = """Latte
$4.00""", relief = FLAT, background = '#f7ebdf')
        self.latte.grid(row = 1, column = 0, sticky = EW)

        # mocha
        self.mch_frame = Frame(self)
        self.mch_frame.grid(row = 2, column = 1, sticky = N)
        self.mch_icon = Button(self.mch_frame, image = self.mch, relief = FLAT, background = '#f7ebdf', command = lambda: self.coffee_selection("Mocha", "4.50"))
        self.mch_icon.grid(row = 0, column = 0, sticky = N)
        self.mocha = Button(self.mch_frame, text = """Mocha
$4.50""", relief = FLAT, background = '#f7ebdf')
        self.mocha.grid(row = 1, column = 0, sticky = EW)

        # macchiato
        self.mchto_frame = Frame(self)
        self.mchto_frame.grid(row = 2, column = 2, sticky = N)
        self.mchto_icon = Button(self.mchto_frame, image = self.mchto, relief = FLAT, background = '#f7ebdf', command = lambda: self.coffee_selection("Macchiato", "3.75"))
        self.mchto_icon.grid(row = 0, column = 0, sticky = N)
        self.macchiato = Button(self.mchto_frame, text = """Macchiato
$3.75""", relief = FLAT, background = '#f7ebdf')
        self.macchiato.grid(row = 1, column = 0, sticky = EW)

        # black coffee
        self.blckffee_frame = Frame(self)
        self.blckffee_frame.grid(row = 3, column = 1, sticky = N)
        self.blckffee_icon = Button(self.blckffee_frame, image = self.blckffee, relief = FLAT, background = '#f7ebdf', command = lambda: self.coffee_selection("Black Coffee", "2.00"))
        self.blckffee_icon.grid(row = 0, column = 0, sticky = N)
        self.black_coffee = Button(self.blckffee_frame, text = """Black Coffee
$2.00""", relief = FLAT, background = '#f7ebdf')
        self.black_coffee.grid(row = 1, column = 0, sticky = EW)

    def coffee_selection(self, coffee_type, price):
        self.selected_coffee = {
            'type': coffee_type,
            'price': price
        }
        self.master.options.options_selection(self.selected_coffee)

class Options(Frame):
    def __init__(self, parent, s, milk, sugar, strength, toppings):
        super().__init__(parent, width = 550, height = 170, background = '#f7ebdf', highlightthickness = 1, highlightbackground = '#230f08')
        self.s = s

       # initialize string variables
        self.milk_clicked = milk
        self.sugar_clicked = sugar
        self.strength_clicked = strength
        self.toppings_clicked = toppings
        
        # 7x3 layout configuration
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 0)
        self.rowconfigure(3, weight = 0)
        self.rowconfigure(4, weight = 0)
        self.rowconfigure(5, weight = 0)
        self.rowconfigure(6, weight = 1)

        for i in range(3):
            self.columnconfigure(i, weight = 1)

        self.grid_propagate(False)

        # widgets
        Label(self, text = "OPTIONS", background = '#230f08', foreground = 'white').grid(row = 0, column = 0, columnspan = 3, sticky = N+E+W)

        # milk options
        regLabel(self, text = "Milk").grid(row = 2, column = 0, sticky = NSEW)
        self.milk_types = ["Whole Milk", "Skim Milk", "Oat Milk", "Almond Milk", "Soy Milk", "Cream", "No Milk"]
        self.milk = ttk.Combobox(self, values = self.milk_types, textvariable = self.milk_clicked)
        self.milk.grid(row = 3, column = 0)

        # sugar
        regLabel(self, text = "Sugar").grid(row = 4, column = 0, sticky = NSEW)
        self.sugar_types = ["No Sugar", "1 Spoon", "2 Spoons", "3 Spoons"]
        self.sugar = ttk.Combobox(self, values = self.sugar_types, textvariable = self.sugar_clicked)
        self.sugar.grid(row = 5, column = 0)

        # strength
        regLabel(self, text = "Strength").grid(row = 2, column = 1, sticky = NSEW)
        self.strength_types = ["Single Shot (standard)", "Double Shot (extra strong)", "Decaf"]
        self.strength = ttk.Combobox(self, values = self.strength_types, textvariable = self.strength_clicked)
        self.strength.grid(row = 3, column = 1)

        # toppings
        regLabel(self, text = "Toppings").grid(row = 4, column = 1, sticky = NSEW)
        self.toppings_types = ["Whipped Cream", "Chocolate Sprinkles", "Cinnamon Powder", "Caramel Drizzle"]
        self.toppings = ttk.Combobox(self, values = self.toppings_types, textvariable = self.toppings_clicked)
        self.toppings.grid(row = 5, column = 1)

        # temperature
        regLabel(self, text = "Temperature").grid(row = 2, column = 2, sticky = NSEW)
        self.temp_value = DoubleVar()
        self.temp = ttk.Scale(self, variable = self.temp_value, from_ = 1, to = 50, orient = VERTICAL, style = 'bg.Vertical.TScale')
        self.temp.grid(row = 3, rowspan = 3, column = 2, sticky = NSEW)

    def options_selection(self, coffee):
        self.coffee = coffee
        self.master.details.details_display(self.coffee, self.milk, self.sugar, self.strength, self.toppings)

class Details(Frame):
    def __init__(self, parent, s, milk, sugar, strength, toppings):
        super().__init__(parent, width = 235, height = 620, background = '#9ea7b0')
        self.s = s

        # initialize string variables
        self.milk_clicked = milk
        self.sugar_clicked = sugar
        self.strength_clicked = strength
        self.toppings_clicked = toppings

        # initialize image
        details_bg = Image.open('assets/details-frame-bg.png')
        self.details_bg = ImageTk.PhotoImage(details_bg)

        # display image
        bg_label = Label(self, image = self.details_bg)
        bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # layout configuration
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 0)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 1)
        self.rowconfigure(5, weight = 1)
        self.rowconfigure(6, weight = 1)

        self.columnconfigure(0, weight = 1)
        self.grid_propagate(False)
        
        Label(self, text = "DETAILS", background = '#230f08', foreground = 'white').grid(row = 0, column = 0, sticky = N+E+W)

        main_frame = Frame(self, width = 200, height = 300, highlightthickness = 1, highlightbackground = '#230f08')
        main_frame.grid(row = 1, column = 0, sticky = NSEW, padx = 15, pady = 15)

        # layout configuration
        main_frame.columnconfigure(0, weight = 1)
        main_frame.columnconfigure(1, weight = 1)

        # canvas
        self.my_canvas = Canvas(main_frame, width = 190, height = 200, background = '#f7ebdf')
        self.my_canvas.grid(row = 0, column = 0, sticky = W)

        # canvas scrollbar
        my_scrollbar = Scrollbar(main_frame, orient = VERTICAL, command = self.my_canvas.yview)
        my_scrollbar.grid(row = 0, column = 1, sticky = NS)

        # configure canvas
        self.my_canvas.configure(yscrollcommand = my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))
        self.my_canvas.grid_propagate(False)

        # 2nd frame in the canvas
        self.second_frame = Frame(self.my_canvas, background = "#f7ebdf", height = 200)

        self.second_frame.grid_columnconfigure(0, weight = 0)
        self.second_frame.grid_columnconfigure(1, weight = 1)

        # new frame to a window in the canvas
        self.my_canvas.create_window((0, 0), window = self.second_frame, anchor = "nw", width = 200)

        confirm = Button(self, text = "Confirm Order", background = '#230f08', foreground = '#f7ebdf', relief = FLAT, command = self.confirm)
        confirm.grid(row = 2, column = 0, sticky = NW, padx = (15, 0), ipadx = 10, ipady = 10)
    
    def details_display(self, coffee_data, *comboboxes):
        for widget in self.second_frame.winfo_children():
            widget.destroy()

        self.milk_label = Label(self.second_frame, text = "", background = '#f7ebdf')
        self.sugar_label = Label(self.second_frame, text = "", background = '#f7ebdf')
        self.strength_label = Label(self.second_frame, text = "", background = '#f7ebdf')
        self.toppings_label = Label(self.second_frame, text = "", background = '#f7ebdf')
        self.temp_label = Label(self.second_frame, text = "", background = '#f7ebdf')

        def comboclick(event):
            selected_milk = self.milk_clicked.get()
            selected_sugar = self.sugar_clicked.get()
            selected_strength = self.strength_clicked.get()
            selected_toppings = self.toppings_clicked.get()
            selected_temp = int(self.master.options.temp_value.get())

            if selected_temp <= 15:
                temp_desc = "Cold"
            elif selected_temp <= 25:
                temp_desc = "Warm"
            elif selected_temp <= 45:
                temp_desc = "Hot"
            else:
                temp_desc = "Very Hot"

            row = 2
            if selected_milk:
                self.milk_label.config(text = f"• {selected_milk}")
                self.milk_label.grid(row = row, column = 0, padx = 5, sticky = W)
                row += 1
            
            if selected_sugar:
                self.sugar_label.config(text = f"• {selected_sugar}")
                self.sugar_label.grid(row = row, column = 0, padx = 5, sticky = W)
                row += 1

            if selected_strength:
                self.strength_label.config(text = f"• {selected_strength}")
                self.strength_label.grid(row = row, column = 0, padx = 5, sticky = W)
                row += 1

            if selected_toppings:
                self.toppings_label.config(text = f"• {selected_toppings}")
                self.toppings_label.grid(row = row, column = 0, padx = 5, sticky = W)
                row += 1
            
            if selected_temp:
                self.temp_label.config(text = f"• {selected_temp}°C ({temp_desc})", background = '#f7ebdf')
                self.temp_label.grid(row = row, column = 0, padx = 5, sticky = W)
                row += 1
        
        if comboboxes:
            for cb in comboboxes:
                cb.bind("<<ComboboxSelected>>", comboclick)

        self.master.options.temp.bind("<B1-Motion>", comboclick)
        self.master.options.temp.bind("<ButtonRelease-1>", comboclick)

        Label(self.second_frame, text = "").grid(row = 0, column = 0)

        self.coffee_data = coffee_data

        if self.coffee_data:
            self.coffee_type = Label(self.second_frame, text = f"{coffee_data['type']}", font = ('Helvetica', 16, 'bold'), background = '#f7ebdf')
            self.coffee_type.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
            self.coffee_price = Label(self.second_frame, text = f"${coffee_data['price']}", font = ('Helvetica', 11, 'italic'), background = '#f7ebdf')
            self.coffee_price.grid(row = 1, column = 0, padx = 5, pady = (0, 5), sticky = W)

    def confirm(self):
        selected_milk = self.milk_clicked.get()
        selected_sugar = self.sugar_clicked.get()
        selected_strength = self.strength_clicked.get()
        selected_toppings = self.toppings_clicked.get()
        selected_temp = int(self.master.options.temp_value.get())

        if selected_temp <= 15:
            temp_desc = "Cold"
        elif selected_temp <= 25:
            temp_desc = "Warm"
        elif selected_temp <= 45:
            temp_desc = "Hot"
        else:
            temp_desc = "Very Hot"

        self.milk_clicked.set("")
        self.sugar_clicked.set("")
        self.strength_clicked.set("")
        self.toppings_clicked.set("")

        for widget in self.second_frame.winfo_children():
            widget.destroy()

        Label(self.second_frame, text = "Order Confirmed!", background = '#f7ebdf', font = ('Helvetica', 11)).grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)

        row = 1
        if self.coffee_data:
            Label(self.second_frame, text = f"{self.coffee_data['type']}", font = ('Helvetica', 16, 'bold'), background = '#f7ebdf').grid(row = row, column = 0, padx = 5, pady = 5, sticky = W)
            row += 1

            Label(self.second_frame, text = f"${self.coffee_data['price']}", font = ('Helvetica', 11, 'italic'), background = '#f7ebdf').grid(row = row, column = 0, padx = 5, pady = 5, sticky = W)
            row +=1 

        if selected_milk:
            Label(self.second_frame, text = f"• {selected_milk}", background = '#f7ebdf').grid(row = row, column = 0, padx = 5, sticky = W)
            row += 1

        if selected_sugar:
            Label(self.second_frame, text = f"• {selected_sugar}", background = '#f7ebdf').grid(row = row, column = 0, padx = 5, sticky = W)
            row += 1

        if selected_strength:
            Label(self.second_frame, text = f"• {selected_strength}", background = '#f7ebdf').grid(row = row, column = 0, padx = 5, sticky = W)
            row += 1

        if selected_toppings:
            Label(self.second_frame, text = f"• {selected_toppings}", background = '#f7ebdf').grid(row = row, column = 0, padx = 5, sticky = W)
            row += 1

        if selected_temp:
            Label(self.second_frame, text = f"• {selected_temp}°C ({temp_desc})", background = '#f7ebdf').grid(row = row, column = 0, padx = 5, sticky = W)
            row += 1

if __name__ == "__main__":
    CoffeeVendingMachine()