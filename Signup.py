from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from patients import *
from Connection import *


class SignUp:
    def __init__(self, root, dr):
        self.dr = dr
        self.root=root
        # Binding ENTER key with signup button:
        # self.loginPage = loginPage
        # root.pack_forget()
        root.bind('<Return>', self.getData)

        self.frame = Frame(root, height=640, width=640, bg='white')
        self.frame.pack()
        self.frame.pack_propagate(0)

        self.add_labels()
        self.add_entry()
        self.add_button()
        self.add_radio()


    def add_labels(self):
        self.main_title = Label(self.frame, text='Sign up', font=('Segoe UI Black bold', 30), bg='white')
        self.main_title.place(x=240, y=30)

        self.photo = PhotoImage(file='./Images/user.png')
        self.image_label = Label(self.frame, bg='white')
        self.image_label.image = self.photo  # anchoring the image
        self.image_label.config(image=self.photo)
        self.image_label.place(x=300, y=100)

        self.name_label = Label(self.frame, text='Name : ', font=('Eras Demi ITC bold', 15), bg='white')
        self.name_label.place(x=110, y=200)

        self.gender_label = Label(self.frame, text='Gender : ', font=('Eras Demi ITC bold', 15), bg='white')
        self.gender_label.place(x=95, y=250)

        self.age_label = Label(self.frame, text='Age : ', font=('Eras Demi ITC bold', 15), bg='white')
        self.age_label.place(x=127, y=300)

        self.email_label = Label(self.frame, text='Email id : ', font=('Eras Demi ITC bold', 15), bg='white')
        self.email_label.place(x=93, y=350)

        self.phone_num_label = Label(self.frame, text='Phone number : ', font=('Eras Demi ITC bold', 15), bg='white')
        self.phone_num_label.place(x=35, y=400)

        self.dob=Label(self.frame,text="DOB : ",font=('Eras Demi ITC bold', 15),bg='white')
        self.dob.place(x=118,y=450)

        self.img_label = Label(self.frame,text='Image : ',font=('Eras Demi ITC bold',15), bg='white')
        self.img_label.place(x=93, y=500)

    def add_entry(self):
        self.name_entry = ttk.Entry(self.frame, width=30, justify=LEFT, font=('Eras Demi ITC bold', 15))
        self.name_entry.place(x=180, y=205)
        self.name_entry.focus()

        self.age_entry = ttk.Entry(self.frame, width=30, justify=LEFT, font=('Eras Demi ITC bold', 15))
        self.age_entry.place(x=180, y=300)

        self.email_entry = ttk.Entry(self.frame, width=30, justify=LEFT, font=('Eras Demi ITC bold', 15))
        self.email_entry.place(x=180, y=350)

        self.phone_entry = ttk.Entry(self.frame, width=30, justify=LEFT, font=('Eras Demi ITC bold', 15))
        self.phone_entry.place(x=180, y=400)

        self.dob_entry=ttk.Entry(self.frame, width=30, justify=LEFT, font=('Eras Demi ITC bold', 15))
        self.dob_entry.place(x=180,y=450)

        self.img_entry=ttk.Entry(self.frame, width=30, justify=LEFT, font=('Eras Demi ITC bold', 15))
        self.img_entry.place(x=180, y=500)

    def add_radio(self):
        self.gender_value = IntVar()
        self.gender_value.set(0)

        self.male = Radiobutton(self.frame, text='Male', value=0, variable=self.gender_value,font=('Arial',15), bg='white')
        self.male.place(x=200, y=250)

        self.female = Radiobutton(self.frame, text='Female', value=1, variable=self.gender_value, font=('Arial',15), bg='white')
        self.female.place(x=300, y=250)

    def add_button(self):
        self.browseButton = Button(self.frame, highlightthickness=0, text='Browse',command=self.browse, font=('Eras Demi ITC',11))
        self.browseButton.place(x=520, y=500)

        self.signin = Button(self.frame, highlightthickness=0, text='Signup',command=self.getData, font=('Eras Demi ITC',15))
        self.signin.place(x=290, y=550)

    def getData(self, event=None):
        print("Name:",self.name_entry.get())
        gender=None
        try:
            print("Age:",int(self.age_entry.get()))
            if self.gender_value.get() == 0:
                print("Gender: MALE")
                gender='M'
            else:
                print("Gender: FEMALE")
                gender='F'
            print("Phonenumber = ",int(self.phone_entry.get()))
            print("EmailId = ",self.email_entry.get())
            img_addr = None
            if(self.img_entry.get() != None):
                img_addr = self.img_entry.get()
            new_patient=Patients(name=self.name_entry.get(),age=int(self.age_entry.get()),gender=gender,email=self.email_entry.get(),phone_number=self.phone_entry.get(),dob=self.dob_entry.get(),image = img_addr)
            insertData(new_patient)

            patient = getPatientbyName(self.name_entry.get(), self.dob_entry.get())
            print(patient.id)
            print(self.dr.patients)
            if str(patient.id) not in self.dr.patients:
                self.dr.patients = self.dr.patients + ',' + str(patient.id)
                print(self.dr.patients)
                updateDoctor(self.dr)

            import PatientInfo
            self.frame.destroy()
            self.root.geometry('740x640')
            PatientInfo.PatientInfo(self.root, patient, self.dr)   ### OPTION ###
        except ValueError as ve:
            messagebox.showerror('Error', "invalid credentials")

    def browse(self):
        filename = filedialog.askopenfilename(initialdir = '/', title='Select image')
        print(type(filename), filename)
        self.img_entry.insert(0,filename)

if __name__ == '__main__':
    window = Tk()
    import DoctorClass
    dr=DoctorClass.Doctor(1,'1,2,3')
    SignUp(window,dr)
    window.mainloop()
