from tkinter import *
# from tkinter import ttk
from datetime import date
# from tkinter import messagebox

window = Tk()


class disease_details:
    def __init__(self, window):
        self.frame = Frame(window, height=640, width=640, bg='white')
        self.frame.pack()
        self.frame.pack_propagate(0)
        self.add_label()
        self.add_entry()
        self.add_button()
        self.get_data()

    def add_label(self):
        current_date = str(date.today())
        date_of_visit = Label(self.frame, text='Date: ' + current_date, font=('Eras Demi ITC bold', 15), bg='white')
        date_of_visit.place(x=10, y=10)

        sym_label = Label(self.frame, text='Symptoms  : ', padx=10, bg='white', font=('Eras Demi ITC bold', 15))
        sym_label.place(x=50, y=160)

        dis_label = Label(self.frame, text='Disease  : ', padx=10, bg='white', font=('Eras Demi ITC bold', 15))
        dis_label.place(x=70, y=280)

        med_label = Label(self.frame, text='Medicines  : ', bg='white', font=('Eras Demi ITC bold', 15))
        med_label.place(x=63, y=350)

    def add_entry(self):
        sym_entry = Text(self.frame, relief='solid', font=('Eras Demi ITC bold', 15))
        sym_entry.place(x=180, y=160, width=400, height=100)
        sym_entry.focus_set()

        dis_entry = Text(self.frame, relief='solid', font=('Eras Demi ITC bold', 15))
        dis_entry.place(x=180, y=280, width=400, height=50)

        med_entry = Text(self.frame, relief='solid',  font=('Eras Demi ITC bold', 15))
        med_entry.place(x=180, y=350, width=400, height=50)

    # def addFocus(self,event):
    #     if event=='<Enter>':
    #         self.e1.configure(highlightbackground='blue')
    #     else:
    #         self.e1.configure(highlightbackground = 'black')

    def get_data(self):
        disease_name = self.dis_entry.get()
        med_list = self.med_entry.get()
        symptoms = self.sym_entry.get('1.0', END)
        print(disease_name, med_list, symptoms)

    def add_button(self):
        b_submit = Button(self.frame, text='Submit', relief='groove', font=('Eras Demi ITC bold', 12), command=self.get_data)
        b_submit.place(x=350, y=420)


disease_details(window)
window.mainloop()
