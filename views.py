from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Signup
import Patient_info
import records
from login import first_page


def loginPage(current_page):
    current_page.frame.pack_forget()
    current_page = Signup.SignUp(window)


window=Tk()
# window.geometry('900x800')

current_page=first_page(window,loginPage)
window.mainloop()
