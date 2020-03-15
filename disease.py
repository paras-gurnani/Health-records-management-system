from tkinter import *
from tkinter import ttk
window = Tk()
# tkinter.Labelframe(window, text='User details')
class disease_details:

    def __init__(self, window):
        self.frame = LabelFrame(window, width=640, height=640, bg='pink', text='User details', font=('Lucida Bright', 15), borderwidth='20')
        self.frame.pack()
        self.add_label()
        self.add_entry()
        self.add_button()

    def add_label(self):
        l1 = Label(self.frame, text='Symptoms  : ', padx=10, bg='pink', font=('Dubai', 12))
        l1.place(x=80, y=80)

        l2 = Label(self.frame, text='Disease  : ',padx=10, bg='pink', font=('Dubai', 12))
        l2.place(x=80, y=200)

        l3 = Label(self.frame, text='Medicines  : ',bg='pink', font=('Dubai', 12))
        l3.place(x=80, y=240)
    def add_entry(self):
        e1 = ttk.Entry(self.frame)
        e1.place(x=180, y=80, width=400, height=100)
        e1.focus()

        e2 = ttk.Entry(self.frame)
        e2.place(x=180, y=200, width=400)

        e3 = ttk.Entry(self.frame)
        e3.place(x=180, y=240, width=400, height=50)

    def add_button(self):
        b1 = Button(self.frame, text='Submit', relief='groove', font=('Dubai', 12))
        b1.place(x=250, y=340)
c = disease_details(window)
window.mainloop()
