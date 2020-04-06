from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class DoctorLogin:

    def __init__(self, window):
        self.root=window
        self.frame = Frame(window, bg='white', height=440, width=640)
        self.frame.pack()
        self.label()
        self.entry()
        self.add_button()
        self.frame.pack_propagate(1)

    def label(self):
        self.photo = PhotoImage(file='./Images/hospital.png')
        self.image_label = Label(self.frame, bg='white')
        self.image_label.image = self.photo  # anchoring the image
        self.image_label.configure(image=self.photo)
        self.image_label.place(x=300, y=50)

        login = Label(self.frame, text='Login  :  ', padx=10, bg='white', font=('Eras Demi ITC bold', 15))
        login.place(x=180, y=150)
        password = Label(self.frame, text='Password : ', bg='white', font=('Eras Demi ITC bold',15))
        password.place(x=155, y=200)

    def entry(self):
        self.login_entry = ttk.Entry(self.frame, justify=LEFT, font=('Lucida Console', 10))
        self.login_entry.place(x=270, y=155, width=180)
        self.login_entry.focus()

        self.password_entry = ttk.Entry(self.frame, show='*', font=('Lucida Console', 10))
        self.password_entry.place(x=270, y=205, width=180)

    def add_button(self):
        submit = Button(self.frame, text='Submit', relief='groove', command=self.toPatientLogin, font=('Eras Demi ITC',15))
        submit.place(x=300, y=250)
        # reg_patient = Button(self.frame, text='Register a new patient', relief='groove', command=self.toPatientSignUp, font=('Eras Demi ITC',15))
        # reg_patient.place(x=230,y=300)

    def toPatientLogin(self):
        import patient_login
        self.frame.destroy()
        patient_login.PatientLogin(self.root)
        

if __name__=='__main__':
    window=Tk()
    DoctorLogin(window)
    window.mainloop()