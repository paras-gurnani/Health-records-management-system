from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Connection import *

# window = Tk()
# window.title('Records')
# # window.geometry('1024x1024')

class Record:
    def __init__(self, root,patient):
        self.frame = Frame(root, height=500, width=1024, bg='white')
        self.patient=patient
        self.frame.pack()
        self.frame.pack_propagate(0)
        self.addLabels()

    def addLabels(self):
        name = self.patient.name
        age = self.patient.age
        email = self.patient.email

        self.photo = PhotoImage(file='./Images/pat.png')
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

        #fetching data from db

        query='''select date_of_entry,disease_name,medicines,note
                from entries e
                join disease d on e.disease_id=d.disease_id
                where patient_id=%d;'''
        # print(self.patient.id)
        params=(self.patient.id,)
        res=getRecords(query,params)
        info=[]
        for entries in res:
            new_entry=[]
            for data in entries:
                new_entry.append(data)
            info.append(entries)


        # Making table:
        #info = [[1,'d1','m1,m2,m3','s1s2'],[10,'d5','m1,m10,m3','s10s2']]
        cols=('Date of visit', 'Disease', 'medications', 'Notes')
        self.record = ttk.Treeview(self.frame, columns=cols, show='headings')   #sets identifier to each columns using parameter 'COLUMNS'
        self.record.column('Notes', width=380)
        for col in cols:
            self.record.heading(col, text=col)      #Sets column headings
        for ele in info:
            self.record.insert('', 'end',  values=(ele[0], ele[1], ele[2], ele[3])) # parameters:1) root of element(root node here since table) 2) after enter 3) Values
        self.record.place(x=20, y=200)

        #Making a back button
        self.back=Button(self.frame,text="Back", font=('Eras Demi bold', 15), bg='grey')
        self.back.place(x=20,y=440)


if __name__=='__main__':
    window = Tk()
    import patients
    dummy_patient=patients.Patients(id=int(1),name="dummy_name",age=20,email="dumm_mail@gmail.com",gender="M",phone_number="1234567890",dob='2000-6-10')
    Record(window,dummy_patient)
    window.mainloop()