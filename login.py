# flaticon.com for images

from tkinter import *
from tkinter import ttk
# from tkinter import messagebox
window = Tk()
# # window.geometry('640x640')

class first_page:

    def __init__(self, window):
        self.frame = Frame(window, bg='white', height=640, width=640)
        self.frame.pack()
        self.label()
        self.entry()
        self.add_button()
        self.frame.pack_propagate(1)

    def label(self):
        login = Label(self.frame, text='LOGIN  :  ', padx=10, bg='white')
        login.place(x=140, y=150)
        password = Label(self.frame, text='PASSWORD : ', bg='white')
        password.place(x=140, y=200)

    def entry(self):
        login_entry = ttk.Entry(self.frame, justify=LEFT)
        login_entry.place(x=220, y=150, width=180)
        login_entry.focus()
        password_entry = ttk.Entry(self.frame)
        password_entry.place(x=220, y=200, width=180)

    def add_button(self):
        submit = Button(self.frame, text='Submit', relief='groove',command=self.changeHomePage)
        submit.place(x=250, y=250)
        reg_patient = Button(self.frame, text='Register a new patient', relief='groove', command=self.changeRegisterPage)
        reg_patient.place(x=210,y=290)

    def changeHomePage(self):
        self.changeHome(self)

    def changeRegisterPage(self):
        self.changeRegister(self)


c = first_page(window)
window.mainloop()