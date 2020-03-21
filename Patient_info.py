from tkinter import *

# from tkinter.ttk import *

# root = Tk()
# # root.geometry('1024x700')
# root.title("Patients info")


class PatientInfo:
    def __init__(self,root,recordsPage,diseasePage):
        self.diseasePage=diseasePage
        self.recordsPage=recordsPage
        self.frame = Frame(root, height=700, width=1024, bg="white")
        self.frame.pack()
        self.create_border()
        self.add_labels()
        self.add_patient_info()
        self.add_buttons()
        self.frame.pack_propagate()

    def create_border(self):
        self.canvas=Canvas(self.frame,height=600,width=550,bg="white",highlightthickness=1,highlightbackground="black")
        self.canvas.place(x=15,y=15)


    def add_labels(self):
        self.name = Label(self.frame, text="Name:", font=('Segoe UI Black bold', 20), bg='white')
        self.name.place(x=50, y=310)
        self.age= Label(self.frame,text="Age:",font=("Segoe UI Black bold",20),bg="white")
        self.age.place(x=50,y=370)
        self.gender = Label(self.frame, text="Gender:", font=("Segoe UI Black bold", 20), bg="white")
        self.gender.place(x=50, y=430)
        self.contact = Label(self.frame, text="Contact No:", font=("Segoe UI Black bold", 20), bg="white")
        self.contact.place(x=50, y=490)
        self.email=Label(self.frame, text="Email:", font=("Segoe UI Black bold", 20), bg="white")
        self.email.place(x=50, y=550)

    #Add one parameter in add_patient_info Patient object which will get its values from database
    def add_patient_info(self):
        #text in each label will be changed by tapping into patient object
        self.p_name = Label(self.frame, text="Dummy_name", font=('Segoe UI Black ', 20), bg='white')
        self.p_name.place(x=150, y=310)
        self.p_age = Label(self.frame, text="Dummy_Age", font=("Segoe UI Black ", 20), bg="white")
        self.p_age.place(x=150, y=370)
        self.p_gender = Label(self.frame, text="Male", font=("Segoe UI Black ", 20), bg="white")
        self.p_gender.place(x=150, y=430)
        self.p_contact = Label(self.frame, text="1234567890", font=("Segoe UI Black ", 20), bg="white")
        self.p_contact.place(x=150, y=490)
        self.p_email = Label(self.frame, text="Dummy_email@gmail.com", font=("Segoe UI Black ", 20), bg="white")
        self.p_email.place(x=150, y=550)

    def add_buttons(self):
        self.show_records=Button(self.frame,text="Show Previous Records",font=('Segoe UI Black ', 20),bg="grey",command=self.changeRecordsPage)
        self.show_records.place(x=650,y=200)
        self.add_entry = Button(self.frame, text="Add new Entry", font=('Segoe UI Black ', 20), bg="grey",command=self.changeDiseasePage)
        self.add_entry.place(x=700, y=300)

    def changeDiseasePage(self):
        self.diseasePage(self)
    def changeRecordsPage(self):
        self.recordsPage(self)

#
#
# p = PatientInfo(root)
#
# root.mainloop()
