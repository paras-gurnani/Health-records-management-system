# flaticon.com for images

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
window = Tk()
# window.geometry('640x640')

class first_page:

    def __init__(self, window):
        self.frame = Frame(window, bg='pink', height=640, width=640)
        self.frame.pack()
        self.label()
        self.entry()
        self.add_button()
        self.frame.pack_propagate(0)

    def label(self):
        self.l1 = Label(self.frame, text='LOGIN  :  ', padx=10, bg='pink')
        self.l1.place(x=240, y=250)
        self.l2 = Label(self.frame, text='PASSWORD : ', bg='pink')
        self.l2.place(x=240, y=300)

    def entry(self):
        self.e1 = ttk.Entry(self.frame, justify = CENTER)
        self.e1.place(x=320, y=250, width=180)
        self.e1.focus()
        self.e2 = ttk.Entry(self.frame)
        self.e2.place(x=320, y=300, width=180)

    def add_button(self):
        self.b1 = Button(self.frame, text='Submit', relief='groove')
        self.b1.place(x=320, y=350)


c = first_page(window)
window.mainloop()