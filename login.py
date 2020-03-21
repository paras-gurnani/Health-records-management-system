# flaticon.com for images

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# window = Tk()
# # window.geometry('640x640')

class first_page:
    def __init__(self, window,changePage):
        self.changePage=changePage
        self.auth_val=0
        self.frame = Frame(window, bg='white', height=500, width=500)
        self.frame.pack()
        self.label()
        self.entry()
        self.add_button()
        self.frame.pack_propagate(1)

    def label(self):
        self.l1 = Label(self.frame, text='LOGIN  :  ', padx=10, bg='white')
        self.l1.place(x=140, y=150)
        self.l2 = Label(self.frame, text='PASSWORD : ', bg='white')
        self.l2.place(x=140, y=200)

    def entry(self):
        self.e1 = ttk.Entry(self.frame, justify = CENTER)
        self.e1.place(x=220, y=150, width=180)
        self.e1.focus()
        self.e2 = ttk.Entry(self.frame)
        self.e2.place(x=220, y=200, width=180)

    def add_button(self):
        self.submit = Button(self.frame, text='Submit', relief='groove',command=self.auth)
        self.submit.place(x=220, y=250)

    def auth(self):
        print("i got clicked")
        self.changePage(self)

#
# c = first_page(window)
# window.mainloop()