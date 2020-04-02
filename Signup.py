from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
class SignUp:
    def __init__(self, root):
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

        self.user_label = Label(self.frame, bg='white')
        self.user_img=PhotoImage(file='./Images/user.png')
        self.user_label.config(image=self.user_img)
        self.user_label.place(x=250, y=90)

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

    def add_radio(self):
        self.gender_value = IntVar()
        self.gender_value.set(2)

        self.male = Radiobutton(self.frame, text='Male', value=0, variable=self.gender_value,font=('Arial',15), bg='white')
        self.male.place(x=200, y=250)

        self.female = Radiobutton(self.frame, text='Female', value=1, variable=self.gender_value, font=('Arial',15), bg='white')
        self.female.place(x=300, y=250)

    def add_button(self):
        self.signin = Button(self.frame, highlightthickness=0, width=80, height=40, bg='white', activebackground='white', borderwidth=0, command=self.getData)
        self.img = PhotoImage(file="./Images/login.png")
        self.signin.config(image=self.img)
        self.signin.place(x=250,y=450)

    def getData(self, event=None):
        print("Name:",self.name_entry.get())
        try:
            print("Age:",int(self.age_entry.get()))
            if self.gender_value.get() == 0:
                print("Gender: MALE")
            else:
                print("Gender: FEMALE")
            print("Phonenumber = ",int(self.phone_entry.get()))
            print("EmailId = ",self.email_entry.get())
        except ValueError as ve:
            messagebox.showerror('Error', "invalid credentials")
            self.loginPage(self)

# class PatientInfoView:
#
#     def __init__(self,root):
#         self.menubar = Menu(root)
#         self.menubar.add_command(label='Info')
#
#         self.menubar.add_command(label='Visualize data')
#         self.menubar.add_command(label='History')

app = SignUp(window)
# window.config(menu=app.menubar)
window.mainloop()