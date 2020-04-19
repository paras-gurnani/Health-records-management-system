from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Connection import *
from piechart import *
from line import *
from DoctorClass import *


class PatientLogin:
    def __init__(self, window, dr=None,type='dr'):
        self.dr = dr
        # print(self.dr.id)
        self.type=type
        self.root=window
        self.root.geometry('640x500')
        self.frame = Frame(window, bg='white', height=500, width=640)
        self.frame.pack()
        self.label()
        self.entry()
        self.add_button()
        self.frame.pack_propagate(1)

    def label(self):
        if(self.type=='dr'):
            self.photo = PhotoImage(file='./Images/hospital.png')
        else:
            self.photo=PhotoImage(file='./Images/patient_login.png')
        self.image_label = Label(self.frame, bg='white')
        self.image_label.image = self.photo  # anchoring the image
        self.image_label.configure(image=self.photo)
        self.image_label.place(x=300, y=50)

        login = Label(self.frame, text='Patient ID  :  ', padx=10, bg='white', font=('Eras Demi ITC bold', 15))
        login.place(x=140, y=150)
        dob = Label(self.frame, text='DOB : ', bg='white', font=('Eras Demi ITC bold',15))
        dob.place(x=200, y=200)

    def entry(self):
        self.login_entry = ttk.Entry(self.frame, justify=LEFT, font=('Lucida Console', 10))
        self.login_entry.place(x=270, y=155, width=180)
        self.login_entry.focus()

        self.dob_entry = ttk.Entry(self.frame, font=('Lucida Console', 10))
        self.dob_entry.place(x=270, y=205, width=180)

    def add_button(self):
        submit = Button(self.frame, text='Login', relief='groove', command=self.toPatientInfo, font=('Eras Demi ITC',15))
        submit.place(x=300, y=250)
        if(self.type=='dr'):
            reg_patient = Button(self.frame, text='Register a new patient', relief='groove', command=self.toPatientSignUp,
                                 font=('Eras Demi ITC', 15))
            reg_patient.place(x=230, y=300)

            analysis = Button(self.frame, text='See analysis', relief='groove', command=draw, font=('Eras Demi ITC',15))
            analysis.place(x=270,y=350)

            self.patient_analysis=Button(self.frame,text='See patient analysis',relief='groove', command=self.drawGraph, font=('Eras Demi ITC',15))
            self.patient_analysis.place(x=240,y=400)

    def toPatientInfo(self):
        if(self.type=='dr'):
            if self.login_entry.get() in self.dr.patients:
                try:
                    patient_id=int(self.login_entry.get())
                    dob=self.dob_entry.get()
                    current_patient=getPatientbyId(patient_id, dob)
                    if(current_patient==None):
                        messagebox.showerror('Error', "No patient found")
                        self.login_entry.delete(0,'end')
                        self.dob_entry.delete(0,'end')
                    else:
                        self.frame.destroy()
                        import PatientInfo
                        self.root.geometry('740x600')
                        PatientInfo.PatientInfo(self.root,current_patient,self.dr)
                except ValueError as ve:
                    print(ve)
            else:
                messagebox.showinfo('Note', 'Enter id is not your patient')
        else:
            try:
                patient_id = int(self.login_entry.get())
                dob = self.dob_entry.get()
                current_patient = getPatientbyId(patient_id, dob)
                if (current_patient == None):
                    messagebox.showerror('Error', "No patient found")
                    self.login_entry.delete(0, 'end')
                    self.dob_entry.delete(0, 'end')
                else:
                    import Record
                    self.root.geometry('1024x500')
                    self.frame.destroy()
                    patient=getPatientbyId(patient_id,dob)
                    Record.Record(self.root,patient)
            except ValueError as ve:
                print(ve)

    def toPatientSignUp(self):
        self.frame.destroy()
        import Signup
        self.root.geometry('640x640')
        Signup.SignUp(self.root, self.dr)

    def drawGraph(self):
        # print(type(self.dr.patients))
        if(self.dr.patients==''):
            messagebox.showerror('Error','You have no patients')
        else:
            plot(self.dr)


if __name__=='__main__':
    window=Tk()
    dr=Doctor(1,'1,2,3,4')
    # dr=None
    PatientLogin(window,dr,'dr')
    window.mainloop()