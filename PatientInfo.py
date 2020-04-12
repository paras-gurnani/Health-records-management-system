from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
from Connection import *

class PatientInfo:
    def __init__(self, root,patient):
        self.root=root
        self.patient=patient
        self.frame = Frame(root, height=640, width=740, bg="white")
        self.frame.pack()
        self.create_border()
        self.add_labels()
        self.add_patient_info()
        self.add_buttons()
        self.frame.pack_propagate()

    def create_border(self):
        self.canvas = Canvas(self.frame, height=500, width=400, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.place(x=15, y=15)


    def add_labels(self):
        self.name = Label(self.frame, text="Name:",padx=10, font=('Segoe UI Black bold', 15), bg='white')
        self.name.place(x=30, y=210)
        self.age= Label(self.frame,text="Age:",padx=10,font=("Segoe UI Black bold", 15),bg="white")
        self.age.place(x=30, y=270)
        self.gender = Label(self.frame, text="Gender:",padx=10, font=("Segoe UI Black bold", 15), bg="white")
        self.gender.place(x=30, y=330)
        self.contact = Label(self.frame,padx=10, text="Contact No:", font=("Segoe UI Black bold", 15), bg="white")
        self.contact.place(x=30, y=390)
        self.email=Label(self.frame, text="Email:",padx=10, font=("Segoe UI Black bold", 15), bg="white")
        self.email.place(x=30, y=450)

    #Add one parameter in add_patient_info Patient object which will get its values from database
    def add_patient_info(self):
        #text in each label will be changed by tapping into patient object
        self.p_name = Label(self.frame, text=self.patient.name, font=('Segoe UI Black ',15), bg='white')
        self.p_name.place(x=150, y=210)
        self.p_age = Label(self.frame, text=self.patient.age, font=("Segoe UI Black ", 15), bg="white")
        self.p_age.place(x=150, y=270)
        self.p_gender = Label(self.frame, text=self.patient.gender, font=("Segoe UI Black ", 15), bg="white")
        self.p_gender.place(x=150, y=330)
        self.p_contact = Label(self.frame, text=self.patient.phone_number, font=("Segoe UI Black ", 15), bg="white")
        self.p_contact.place(x=150, y=390)
        self.p_email = Label(self.frame, text=self.patient.email, font=("Segoe UI Black ", 15), bg="white")
        self.p_email.place(x=150, y=450)

    def add_buttons(self):
        self.logout = Button(self.frame, text='logout',font=('Segoe UI Black ', 10), command=self.toPatientLogin)
        self.logout.place(x=680, y=5)
        self.show_records=Button(self.frame,text="Show Previous Records",font=('Segoe UI Black ', 15), command=self.toRecords)
        self.show_records.place(x=450,y=200)
        self.add_entry = Button(self.frame, text="Add new Entry", font=('Segoe UI Black ', 15), command=self.toDisease)
        self.add_entry.place(x=450, y=300)

    def toPatientLogin(self):
        import patient_login
        self.frame.destroy()
        self.root.geometry('640x440')
        patient_login.PatientLogin(self.root)

    def toRecords(self):
        import Record
        win = Toplevel()
        win.title('Records')
        Record.Record(win,self.patient)


    def toDisease(self):
        import Disease
        win = Toplevel()
        win.title('Diagnose')
        Disease.Disease(win,self.patient)


if __name__=='__main__':
    window = Tk()
    window.geometry('740x640')     # TO SUPPORT FULL SCREEN
    PatientInfo(window)
    window.mainloop()
