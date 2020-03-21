from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Signup import SignUp
from Patient_info import PatientInfo
from records import Record
from login import first_page
from disease import disease_details


def signupPage(current_page):
    current_page.frame.pack_forget()
    current_page = SignUp(window,loginPage)

def loginPage(current_page):
    current_page.frame.pack_forget()
    current_page=first_page(window,signupPage,patientInfoPage)

def recordsPage(current_page):
    current_page.frame.pack_forget()
    current_page=Record(window,patientInfoPage)

def diseasePage(current_page):
    current_page.frame.pack_forget()
    current_page=disease_details(window)

def patientInfoPage(current_page):
    current_page.frame.pack_forget()
    current_page=PatientInfo(window,recordsPage,diseasePage)


window=Tk()

current_page=first_page(window,signupPage,patientInfoPage)
window.mainloop()
