from distutils.log import Log
from re import L
from tkinter import *
from turtle import back
from PIL import ImageTk, Image
import customtkinter
import tkinter.messagebox
#pip install pyrebase4
import pyrebase
from pygame import FULLSCREEN
import random
import shutup;shutup.please()

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
auth = firebase.auth()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class LOGIN(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.master.geometry('900x500')
        self.master.title('EZ-Learning 2.0')
        self.master.iconbitmap("Logo.ico")
        self.master.config(bg="#121212")
        print("The Login class has been opened")

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
            command=self.login)
        self.enter_btn.place(x=270, y=230)

        self.signup_btn = customtkinter.CTkButton(self.template,
            text="Create New Account",
            border_width=2,
            fg_color=None,
            command=self.signup)
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
    
    def login(self):
        if self._Email.get() == '' or self._Password.get() == '': tkinter.messagebox.showinfo('Try Again', 'Please complete the required fields.')
        else: 
            try:
                login = auth.sign_in_with_email_and_password(self._Email.get(), self._Password.get())
                print("Login Successfully")
                NOTES_FOLDER(self.master)
            except:
                tkinter.messagebox.showinfo('Error', 'Invalid Email or Password. Try again')


    def signup(self):
        SIGNUP(self.master)
    
class SIGNUP(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.master.geometry('900x500')
        self.master.title('EZ-Learning 2.0')
        self.master.iconbitmap("Logo.ico")
        self.master.config(bg="#121212")
        print("The Signup class has been opened")

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
            command=self.signup)
        self.enter_btn.place(x=270, y=230)

        self.signup_btn = customtkinter.CTkButton(self.template,
            text="Use Existing Account",
            border_width=2,
            fg_color=None,
            command=self.login)
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
    
    def signup(self):
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

    def login(self):
        LOGIN(self.master)

class NOTES_FOLDER(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.closemenu_dark = ImageTk.PhotoImage(Image.open("close_dark.png"))
        self.closemenu_light = ImageTk.PhotoImage(Image.open("close_light.png"))
        self.backframe()
        self.side_menu_icon()    
        print("The Home class has been opened")

    def backframe(self):
        Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg")).place(x=0, y=0)

    def side_menu_icon(self):
        if self.master.cget("bg") == "#121212":
            Button(self.master,
            image=self.threelinemenu_dark,
            command=self.side_menu,
            border=0,
            bg=self.master.cget("bg"),
            activebackground=self.master.cget("bg")).place(x=5,y=8)
        elif self.master.cget("bg") == "#0d9187":
            Button(self.master,
            image= self.threelinemenu_light,
            command=self.side_menu,
            border=0,
            bg=self.master.cget("bg"),
            activebackground=self.master.cget("bg")).place(x=5,y=8)
    
    def side_menu(self):
        THREELINE_MENU(self.master)

class QUIZ_FOLDER(customtkinter.CTk):
    ""

class RECYCLE_BIN(customtkinter.CTk):
    ""

class PROFILE_SETTINGS(customtkinter.CTk):
    ""

class THREELINE_MENU(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.closemenu_dark = ImageTk.PhotoImage(Image.open("close_dark.png"))
        self.closemenu_light = ImageTk.PhotoImage(Image.open("close_light.png"))

        self.burger_menu()
        print("The Three-Line Menu class has been opened")

    def menu(self):
        pass
    
    def burger_menu(self):
        fg_color = "#ffffff"
        activefg = "#ffffff"
        fontstyle = ("Roboto", 17, "bold")

        if self.master.cget("bg") == "#121212":
            bg_color = "#3B3838"
            activebg = "#6B6565"
        else: 
            bg_color = "#15559B"
            activebg = "#114681"
            
        threeline_menu = Frame(self.master,
        width=286,
        height=500,
        background=bg_color)
        threeline_menu.place(x=0, y=0)
        if bg_color == "#3B3838":
            close_button = self.closemenu_dark
        else: close_button = self.closemenu_light
        Button(self.master,
        image=close_button,
        command=self.menu,
        border=0,
        bg=bg_color,
        activebackground=bg_color).place(x=7,y=10)
        Notes = Button(self.master,
                text="     Notes",
                command=self.menu,
                anchor=W,
                font=fontstyle,
                border=0,
                fg=fg_color,
                activeforeground=activefg,
                bg=bg_color,
                activebackground=activebg,
                width=20)
        Quizzes = Button(self.master,
                text="     Quizzes",
                anchor=W,
                font=fontstyle,
                command=self.menu,
                border=0,
                fg=fg_color,
                activeforeground=activefg,
                bg=bg_color,
                activebackground=activebg,
                width=20)
        Recycle_Bin = Button(self.master,
                text="     Recycle Bin",
                anchor=W,
                font=fontstyle,
                command=self.menu,
                border=0,
                fg=fg_color,
                activeforeground=activefg,
                bg=bg_color,
                activebackground=activebg,
                width=20)
        Profile_Settings = Button(self.master,
                text="     Profile Settings",
                anchor=W,
                font=fontstyle,
                command=self.menu,
                border=0,
                fg=fg_color,
                activeforeground=activefg,
                bg=bg_color,
                activebackground=activebg,
                width=20)
        Logout = Button(self.master,
                text="     Logout",
                anchor=W,
                font=fontstyle,
                command=self.menu,
                border=0,
                fg=fg_color,
                activeforeground=activefg,
                bg=bg_color,
                activebackground=activebg,
                width=20)
        Notes.place(x=0,y=75)
        Quizzes.place(x=0, y=123)
        Recycle_Bin.place(x=0, y=171)
        Profile_Settings.place(x=0, y=219)
        Logout.place(x=0, y=267)
    
window = Tk()
window.resizable(False, False)
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
w = 900
h = 500

x = (ws/2) - (w/2)
y = (hs/2) - (h/1.7)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
if __name__ == "__main__":
    the_hundreds = SIGNUP(window)
    window.mainloop()