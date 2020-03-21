# flaticon.com for images

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# window = Tk()
# # window.geometry('640x640')

class first_page:
    def __init__(self, window,changeRegister,changeHome):
        self.changeRegister=changeRegister
        self.changeHome=changeHome
        self.frame = Frame(window, bg='white', height=500, width=500)
        self.frame.pack()
        self.label()
        self.entry()
        self.add_button()
        self.frame.pack_propagate(1)

    def label(self):
        self.login = Label(self.frame, text='LOGIN  :  ', padx=10, bg='white')
        self.login.place(x=140, y=150)
        self.password = Label(self.frame, text='PASSWORD : ', bg='white')
        self.password.place(x=140, y=200)

    def entry(self):
        self.login_entry = ttk.Entry(self.frame, justify = CENTER)
        self.login_entry.place(x=220, y=150, width=180)
        self.login_entry.focus()
        self.password_entry = ttk.Entry(self.frame)
        self.password_entry.place(x=220, y=200, width=180)

    def add_button(self):
        self.submit = Button(self.frame, text='Submit', relief='groove',command=self.changeHomePage)
        self.submit.place(x=250, y=250)
        self.reg_patient=Button(self.frame, text='Register a new patient', relief='groove',command=self.changeRegisterPage)
        self.reg_patient.place(x=210,y=290)

    def changeHomePage(self):
        self.changeHome(self)

    def changeRegisterPage(self):
        self.changeRegister(self)

#
# c = first_page(window)
# window.mainloop()