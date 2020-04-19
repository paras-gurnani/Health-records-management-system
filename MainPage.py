from tkinter import *
# from PIL import Image
class MainPage:
    def __init__(self,root):
        self.root=root
        self.frame=Frame(self.root,height=400,width=600,bg='white')
        self.patientImage=PhotoImage(file="./Images/patientSquare.png")
        self.patientImage.subsample(207,214)
        self.doctorImage=PhotoImage(file='./Images/stethoscope.png')
        self.doctorImage.subsample(200,200)
        self.frame.pack()
        self.addButtons()
    def addButtons(self):
        self.doctorButton=Button(self.frame,text='Doctor Login',font=('Eras Demi ITC',15),image=self.doctorImage,bg='WHITE',compound=TOP,command=self.toDoctorLogin)
        self.doctorButton.place(x=75,y=50)
        self.patientButton=Button(self.frame,text='Patient Login',font=('Eras Demi ITC',15),image=self.patientImage,bg='WHITE',compound=TOP,command=self.toPatientLogin)
        self.patientButton.place(x=325,y=50)

    def toDoctorLogin(self):
        import DoctorLogin
        self.frame.destroy()
        DoctorLogin.DoctorLogin(self.root)

    def toPatientLogin(self):
        import patient_login
        self.frame.destroy()
        patient_login.PatientLogin(self.root,None,'patient')

if(__name__=='__main__'):
    root=Tk()
    root.geometry('600x400')
    m=MainPage(root)
    root.mainloop()
