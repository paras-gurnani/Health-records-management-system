from tkinter import *
# from tkinter import ttk
from datetime import date
# from tkinter import messagebox

class Disease:
    def __init__(self, window):
        self.root=window
        self.frame = Frame(window, height=600, width=640, bg='white')
        self.frame.pack()
        self.frame.pack_propagate(0)
        self.add_label()
        self.add_entry()
        self.add_button()

    def add_label(self):
        current_date = str(date.today())
        date_of_visit = Label(self.frame, text='Date: ' + current_date, font=('Eras Demi ITC bold', 15), bg='white')
        date_of_visit.place(x=10, y=10)

        img = PhotoImage(file='./Images/disease_logo.png')
        logo_label = Label(self.frame, bg='white')
        logo_label.image=img
        logo_label.configure(image=img)
        logo_label.place(x=290, y=50)

        sym_label = Label(self.frame, text='Symptoms  : ', padx=10, bg='white', font=('Eras Demi ITC bold', 15))
        sym_label.place(x=50, y=200)

        dis_label = Label(self.frame, text='Disease  : ', padx=10, bg='white', font=('Eras Demi ITC bold', 15))
        dis_label.place(x=70, y=310)

        med_label = Label(self.frame, text='Medicines  : ', bg='white', font=('Eras Demi ITC bold', 15))
        med_label.place(x=63, y=390)

    def add_entry(self):
        self.sym_entry = Text(self.frame, relief='solid', font=('Lucida console', 10))
        self.sym_entry.place(x=180, y=200, width=400, height=100)
        self.sym_entry.focus_set()

        self.dis_entry = Text(self.frame, relief='solid', font=('Lucida console', 10))
        self.dis_entry.place(x=180, y=320, width=400, height=50)

        self.med_entry = Text(self.frame, relief='solid',  font=('Lucida console', 10))
        self.med_entry.place(x=180, y=390, width=400, height=65)



    def add_button(self):
        b_submit = Button(self.frame, text='Submit', relief='groove', font=('Eras Demi ITC bold', 15), command=self.get_data)
        b_submit.place(x=320, y=480)

    def get_data(self):
        disease_name = self.dis_entry.get("1.0","end-1c")
        med_list = self.med_entry.get("1.0","end-1c")
        symptoms = self.sym_entry.get("1.0","end-1c")
        print(disease_name, med_list, symptoms)
        self.root.destroy()


if __name__=='__main__':
    window=Tk()
    Disease(window)
    window.mainloop()
