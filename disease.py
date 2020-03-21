from tkinter import *
from tkinter import ttk
from datetime import date
from tkinter import messagebox

# window = Tk()


class disease_details:
    def __init__(self, window):
        self.frame = Frame(window, height=640, width=640, bg='white')
        self.frame.pack()
        self.frame.pack_propagate(0)
        self.add_label()
        self.add_entry()
        self.add_button()

    def add_label(self):
        current_date = str(date.today())
        self.date_of_visit = Label(self.frame, text='Date:' + current_date, font=('Eras Demi ITC bold', 15), bg='white')
        self.date_of_visit.place(x=10, y=10)

        self.sym_label = Label(self.frame, text='Symptoms  : ', padx=10, bg='white', font=('Eras Demi ITC bold', 15))
        self.sym_label.place(x=50, y=160)

        dis_label = Label(self.frame, text='Disease  : ', padx=10, bg='white', font=('Eras Demi ITC bold', 15))
        dis_label.place(x=70, y=280)

        med_label = Label(self.frame, text='Medicines  : ', bg='white', font=('Eras Demi ITC bold', 15))
        med_label.place(x=63, y=330)

    def add_entry(self):
        self.sym_entry = Text(self.frame,  font=('Eras Demi ITC bold', 15))
        # self.e1.bind('<Enter>',self.addFocus)
        # self.e1.bind('<Leave>',self.addFocus)
        self.sym_entry.place(x=180, y=130, width=400, height=100)
        self.sym_entry.focus()

        self.dis_entry = ttk.Entry(self.frame,  font=('Eras Demi ITC bold', 15))
        self.dis_entry.place(x=180, y=280, width=400)

        self.med_entry = ttk.Entry(self.frame,  font=('Eras Demi ITC bold', 15))
        self.med_entry.place(x=180, y=325, width=400, height=50)

    # def addFocus(self,event):
    #     if event=='<Enter>':
    #         self.e1.configure(highlightbackground='blue')
    #     else:
    #         self.e1.configure(highlightbackground = 'black')
    def add_button(self):
        b1 = Button(self.frame, text='Submit', relief='groove', font=('Eras Demi ITC bold', 12), command=self.getData)
        b1.place(x=350, y=420)

    def getData(self):
        disease_name = self.dis_entry.get()
        med_list = self.med_entry.get().split(',')
        symptoms = self.sym_entry.get('1.0',END)
        print(disease_name, med_list, symptoms)

#
# disease_details(window)
# window.mainloop()
