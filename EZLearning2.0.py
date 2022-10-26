from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import tkinter.messagebox
#pip install pyrebase4
import pyrebase
from pygame import FULLSCREEN
import random

#SAMPLE EMAIL AND PASSWORD FOR LOGIN:
#fake@gmail.com
#1234567

config = {"apiKey": "AIzaSyBARpuvAyruul-wLV0APfAsd0oT7W5rOuU",
  "authDomain": "fir-a97e4.firebaseapp.com",
  "databaseURL": "https://fir-a97e4.firebaseio.com",
  "projectId": "fir-a97e4",
  "storageBucket": "fir-a97e4.appspot.com",
  "messagingSenderId": "1093466307621",
  "appId": "1:1093466307621:web:c15c81e28e2b468d4853cc",
  "measurementId": "G-LF9NKKBDQ8"}

firebase = pyrebase.initialize_app(config)
auth =firebase.auth()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class login(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.master.geometry('900x500')
        self.master.title('EZ-Learning 2.0')
        self.master.iconbitmap("Logo.ico")
        self.master.config(bg="#121212")

        self._Email = StringVar()
        self._Password = StringVar()

        self.logo = (Image.open("logo_darkmode.png"))
        self.resize_logo = self.logo.resize((80, 80), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(self.resize_logo)
        self.canvas = Label(self.master, image=self.photoimage, bd=0)
        self.canvas.place(x=410, y=15)

        self.sub = Label(self.master, text = 'IT 105 - Application Development and Emerging Technologies', justify=LEFT, font = ('Arial',7,'bold'), bg = '#121212', fg="#bbbbbb")
        self.sub.place(x=10, y=474)
        self.dev_names = Label(self.master, text = 'Dar, John Homer Sayno\nDela Fuente, Ar-Jay\nEchano, Angelo Millares\nMalubay, Arriana Mae Vargas\nMortiga, Renze Meinard', justify=LEFT, font = ('Roboto',7), bg = '#121212', fg="#bbbbbb")
        self.dev_names.place(x=10, y=418)

        self.template = customtkinter.CTkFrame(self.master,
            width=500,
            height=310,)
        self.template.place(x=200, y=100)

        self.create_acc = customtkinter.CTkLabel(self.template,
            text="Login Account:",
            text_font=("Roboto Medium", -16))
        self.create_acc.place(x=180, y=25)

        self.acc_name = customtkinter.CTkLabel(self.template,
            text="Email:")
        self.acc_name.place(x=112, y=65)

        self.name_entry = customtkinter.CTkEntry(self.template,
            width=180,
            fg_color=None,
            textvariable=self._Email)
        self.name_entry.place(x=162, y=95)

        self.acc_pass = customtkinter.CTkLabel(self.template,
            text="Password:")
        self.acc_pass.place(x=125, y=135)

        self.pass_entry = customtkinter.CTkEntry(self.template,
            width=180,
            fg_color=None,
            textvariable=self._Password,
            show="*")
        self.pass_entry.place(x=162, y=165)

        self.enter_btn = customtkinter.CTkButton(self.template,
            text="Login",
            border_width=2,
            fg_color=None,
            command=self.Login)
        self.enter_btn.place(x=270, y=230)

        self.signup_btn = customtkinter.CTkButton(self.template,
            text="Create New Account",
            border_width=2,
            fg_color=None,
            command=self.Signup)
        self.signup_btn.place(x=85, y=230)

        self.app_label = customtkinter.CTkLabel(self.master,
            text="Appearance Mode:",
            text_font=("Roboto Medium", 10))
        self.app_label.place(x=605, y=17)        

        self.appearance = customtkinter.CTkComboBox(self.master,
            values=["Dark", "Light"],
            command=self.change_appearance_mode)
        self.appearance.place(x=745, y=15)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        if new_appearance_mode == "Dark":
            self.master.config(bg="#121212")
            self.logo = (Image.open("logo_darkmode.png"))
            self.resize_logo = self.logo.resize((80, 80), Image.ANTIALIAS)
            self.photoimage = ImageTk.PhotoImage(self.resize_logo)
            self.canvas = Label(self.master, image=self.photoimage, bd=0)
            self.canvas.place(x=410, y=15)
            self.sub = Label(self.master, text = 'IT 105 - Application Development and Emerging Technologies', justify=LEFT, font = ('Arial',7,'bold'), bg = '#121212', fg="#bbbbbb")
            self.sub.place(x=10, y=474)
            self.dev_names = Label(self.master, text = 'Dar, John Homer Sayno\nDela Fuente, Ar-Jay\nEchano, Angelo Millares\nMalubay, Arriana Mae Vargas\nMortiga, Renze Meinard', justify=LEFT, font = ('Roboto',7), bg = '#121212', fg="#bbbbbb")
            self.dev_names.place(x=10, y=418)
        elif new_appearance_mode == "Light":
            self.master.config(bg="#0d9187")
            self.logo = (Image.open("logo_lightmode.png"))
            self.resize_logo = self.logo.resize((80, 80), Image.ANTIALIAS)
            self.photoimage = ImageTk.PhotoImage(self.resize_logo)
            self.canvas = Label(self.master, image=self.photoimage, bd=0)
            self.canvas.place(x=410, y=15)
            self.sub = Label(self.master, text = 'IT 105 - Application Development and Emerging Technologies', justify=LEFT, font = ('Arial',7,'bold'), bg = '#0d9187', fg="#2e2e2e")
            self.sub.place(x=10, y=474)
            self.dev_names = Label(self.master, text = 'Dar, John Homer Sayno\nDela Fuente, Ar-Jay\nEchano, Angelo Millares\nMalubay, Arriana Mae Vargas\nMortiga, Renze Meinard', justify=LEFT, font = ('Roboto',7), bg = '#0d9187', fg="#2e2e2e")
            self.dev_names.place(x=10, y=418)
    
    def Login(self):
        if self._Email.get() == '' or self._Password.get() == '': tkinter.messagebox.showinfo('Try Again', 'Please complete the required fields.')
        else: 
            try:
                login = auth.sign_in_with_email_and_password(self._Email.get(), self._Password.get())
                print("Login Successfully")
                home(self.master)
            except:
                tkinter.messagebox.showinfo('Error', 'Invalid Email or Password. Try again')


    def Signup(self):
        signup(self.master)
    

class signup(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.master.geometry('900x500')
        self.master.title('EZ-Learning 2.0')
        self.master.iconbitmap("Logo.ico")
        self.master.config(bg="#121212")

        self._Username = StringVar()
        self._Email = StringVar()
        self._Password = StringVar()
        self._Confirm_Password = StringVar()

        self.logo = (Image.open("logo_darkmode.png"))
        self.resize_logo = self.logo.resize((80, 80), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(self.resize_logo)
        self.canvas = Label(self.master, image=self.photoimage, bd=0)
        self.canvas.place(x=410, y=15)

        self.sub = Label(self.master, text = 'IT 105 - Application Development and Emerging Technologies', justify=LEFT, font = ('Arial',7,'bold'), bg = '#121212', fg="#bbbbbb")
        self.sub.place(x=10, y=474)
        self.dev_names = Label(self.master, text = 'Dar, John Homer Sayno\nDela Fuente, Ar-Jay\nEchano, Angelo Millares\nMalubay, Arriana Mae Vargas\nMortiga, Renze Meinard', justify=LEFT, font = ('Roboto',7), bg = '#121212', fg="#bbbbbb")
        self.dev_names.place(x=10, y=418)

        self.template = customtkinter.CTkFrame(self.master,
            width=500,
            height=310)
        self.template.place(x=200, y=100)

        self.create_acc = customtkinter.CTkLabel(self.template,
            text="Create New Account:",
            text_font=("Roboto Medium", -16))
        self.create_acc.place(x=180, y=25)

        self.acc_name = customtkinter.CTkLabel(self.template,
            text="Username:")
        self.acc_name.place(x=12, y=65)

        self.name_entry = customtkinter.CTkEntry(self.template,
            width=180,
            fg_color=None,
            textvariable=self._Username)
        self.name_entry.place(x=50, y=95)

        self.acc_email = customtkinter.CTkLabel(self.template,
            text="Email:")
        self.acc_email.place(x=217, y=65)

        self.name_entry = customtkinter.CTkEntry(self.template,
            width=180,
            fg_color=None,
            textvariable=self._Email)
        self.name_entry.place(x=270, y=95)

        self.acc_name = customtkinter.CTkLabel(self.template,
            text="Password:")
        self.acc_name.place(x=12, y=135)

        self.name_entry = customtkinter.CTkEntry(self.template,
            width=180,
            fg_color=None,
            textvariable=self._Password,
            show="*")
        self.name_entry.place(x=50, y=165)

        self.acc_pass = customtkinter.CTkLabel(self.template,
            text="Confirm Password:")
        self.acc_pass.place(x=254, y=135)

        self.pass_entry = customtkinter.CTkEntry(self.template,
            width=180,
            fg_color=None,
            textvariable=self._Confirm_Password,
            show="*")
        self.pass_entry.place(x=270, y=165)

        self.enter_btn = customtkinter.CTkButton(self.template,
            text="Signup Account",
            border_width=2,
            fg_color=None,
            command=self.Signup)
        self.enter_btn.place(x=270, y=230)

        self.signup_btn = customtkinter.CTkButton(self.template,
            text="Use Existing Account",
            border_width=2,
            fg_color=None,
            command=self.Login)
        self.signup_btn.place(x=85, y=230)

        self.app_label = customtkinter.CTkLabel(self.master,
            text="Appearance Mode:",
            text_font=("Roboto Medium", 10))
        self.app_label.place(x=605, y=17)        

        self.appearance = customtkinter.CTkComboBox(self.master,
            values=["Dark", "Light"],
            command=self.change_appearance_mode)
        self.appearance.place(x=745, y=15)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        if new_appearance_mode == "Dark":
            self.master.config(bg="#121212")
            self.logo = (Image.open("logo_darkmode.png"))
            self.resize_logo = self.logo.resize((80, 80), Image.ANTIALIAS)
            self.photoimage = ImageTk.PhotoImage(self.resize_logo)
            self.canvas = Label(self.master, image=self.photoimage, bd=0)
            self.canvas.place(x=410, y=15)
            self.sub = Label(self.master, text = 'IT 105 - Application Development and Emerging Technologies', justify=LEFT, font = ('Arial',7,'bold'), bg = '#121212', fg="#bbbbbb")
            self.sub.place(x=10, y=474)
            self.dev_names = Label(self.master, text = 'Dar, John Homer Sayno\nDela Fuente, Ar-Jay\nEchano, Angelo Millares\nMalubay, Arriana Mae Vargas\nMortiga, Renze Meinard', justify=LEFT, font = ('Roboto',7), bg = '#121212', fg="#bbbbbb")
            self.dev_names.place(x=10, y=418)
        elif new_appearance_mode == "Light":
            self.master.config(bg="#0d9187")
            self.logo = (Image.open("logo_lightmode.png"))
            self.resize_logo = self.logo.resize((80, 80), Image.ANTIALIAS)
            self.photoimage = ImageTk.PhotoImage(self.resize_logo)
            self.canvas = Label(self.master, image=self.photoimage, bd=0)
            self.canvas.place(x=410, y=15)
            self.sub = Label(self.master, text = 'IT 105 - Application Development and Emerging Technologies', justify=LEFT, font = ('Arial',7,'bold'), bg = '#0d9187', fg="#2e2e2e")
            self.sub.place(x=10, y=474)
            self.dev_names = Label(self.master, text = 'Dar, John Homer Sayno\nDela Fuente, Ar-Jay\nEchano, Angelo Millares\nMalubay, Arriana Mae Vargas\nMortiga, Renze Meinard', justify=LEFT, font = ('Roboto',7), bg = '#0d9187', fg="#2e2e2e")
            self.dev_names.place(x=10, y=418)
    
    def Signup(self):
        if self._Username.get() == '' or self._Password.get() == '' or self._Email.get() == '' or self._Password.get() == '' or self._Confirm_Password.get() == '': 
            tkinter.messagebox.showinfo('Try Again', 'Please input data')
        else:
            if self._Password.get() != self._Confirm_Password.get():tkinter.messagebox.showinfo('Try Again', 'Your Password do not match')
            else: 
                try:
                    signin = auth.create_user_with_email_and_password(self._Email.get(), self._Password.get())
                    print("Signin Successfully")
                except:
                    tkinter.messagebox.showinfo('Invalid', 'Email Exist, please input another account')

    def Login(self):
        login(self.master)

class home(customtkinter.CTk):
    def __init__(self, master):
        self.master = master

        def backframe():
            defaultbackground = Frame(self.master,
            width=900,
            height=500,
            background=self.master.cget("bg"))
            defaultbackground.place(x=0, y=0)

        def default_home():
            backframe()
        
        default_home()

        
window = Tk()
window.resizable(False, False)
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen
w = 900 # width for the Tk root
h = 500 # height for the Tk root

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/1.7)

# set the dimensions of the screen 
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
if __name__ == "__main__":
    the_hundreds = signup(window)
    window.mainloop()