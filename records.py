from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title('Records')
window.geometry('1024x1024')

class Record:
    def __init__(self, root):
        self.frame = Frame(root, height=1024, width=1024, bg='white')
        self.frame.pack()
        self.frame.pack_propagate(0)
        self.addLabels()

    def addLabels(self):
        name = 'Dummy name'
        age = 20
        email = 'dummy@gmail.com'

        # Cannot add image

        self.photo = PhotoImage(file='pat.png')
        self.image_label = Label(self.frame, bg='white')
        self.image_label.image=self.photo                   # anchoring the image
        self.image_label.configure(image=self.photo)
        self.image_label.place(x=10, y=10)

        self.name_label = Label(self.frame, text='Name = ' + name, font=('Eras Demi bold', 15), bg='white')
        self.name_label.place(x=5, y=70)
        self.age_label = Label(self.frame, text='Age = ' + str(age), font=('Eras Demi bold', 15), bg='white')
        self.age_label.place(x=5, y=110)
        self.email_label = Label(self.frame, text='Email = ' + email, font=('Eras Demi bold', 15), bg='white')
        self.email_label.place(x=5, y=150)

        # Making table:
        info = [[1,'d1','m1,m2,m3','s1s2'],[10,'d5','m1,m10,m3','s10s2']]
        cols=('Date of visit', 'Disease', 'medications', 'Symptoms')
        self.record = ttk.Treeview(self.frame, columns=cols, show='headings')   #sets identifier to each columns using parameter 'COLUMNS'
        self.record.column('Symptoms', width=380)
        for col in cols:
            self.record.heading(col, text=col)      #Sets column headings
        for ele in info:
            self.record.insert('', 'end',  values=(ele[0], ele[1], ele[2], ele[3])) # parameters:1) root of element(root node here since table) 2) after enter 3) Values
        self.record.place(x=20, y=200)


Record(window)
window.mainloop()