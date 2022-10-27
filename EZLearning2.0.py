from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import tkinter.messagebox
#pip install pyrebase4
import pyrebase
from pygame import FULLSCREEN
import shutup;shutup.please()

#SAMPLE EMAIL AND PASSWORD FOR LOGIN:
#2@gmail.com
#//////

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
        print("OPENED: Login Feature")

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
        print("OPENED: Signup Feature")

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
                except:
                    tkinter.messagebox.showinfo('Invalid', 'Email Exist, please input another account')

    def login(self):
        LOGIN(self.master)

class NOTES_FOLDER(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("search_light.png"))
        self.contentbg_dark = ImageTk.PhotoImage(Image.open("notesfolder_dark.png"))
        self.contentbg_light = ImageTk.PhotoImage(Image.open("notesfolder_light.png"))
        self.quizbtn_dark = ImageTk.PhotoImage(Image.open("quizzesbutton_dark.png"))
        self.quizbtn_light = ImageTk.PhotoImage(Image.open("quizzesbutton_light.png"))
        self.backframe()
        self.features()
        print("OPENED: Notes Folder")

    def backframe(self):
        Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg")).place(x=0, y=0)

    def features(self):

        bg_color = self.master.cget("bg")

        if bg_color == "#121212":
            Label(self.master,
            image=self.search_dark,
            border=0,
            bg=bg_color).place(x=30,y=12)

            Label(self.master,
            image=self.contentbg_dark,
            border=0,).place(x=23,y=70)

            Button(self.master,
            image=self.threelinemenu_dark,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=50,y=24)

            Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=bg_color,
            borderwidth=0,
            fg="#e9e9e9").place(x=100, y=30)

            Button(self.master,
            text="Quizzes",
            fg=bg_color,
            font=("Roboto", 14, "bold"),
            command=self.goto_quizzes,
            bg="#A6A6A6",
            borderwidth=0,
            activeforeground=bg_color,
            activebackground="#A6A6A6").place(x=506, y=85)

            Label(self.master,
            text="Notes",
            fg="#F2F2F2",
            font=("Roboto", 14, "bold"),
            bg="#2C2C2C",
            borderwidth=0).place(x=322, y=90)
        elif bg_color == "#0d9187":

            Label(self.master,
            image=self.search_light,
            border=0,
            bg=bg_color).place(x=30,y=12)

            Label(self.master,
            image=self.contentbg_light,
            border=0,).place(x=23,y=70)

            Button(self.master,
            image=self.threelinemenu_light,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=50,y=24)
            
            Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=bg_color,
            borderwidth=0,
            fg="#e9e9e9").place(x=100, y=30)

            Button(self.master,
            text="Quizzes",
            fg="#F2F2F2",
            font=("Roboto", 14, "bold"),
            command=self.goto_quizzes,
            bg="#0c325c",
            borderwidth=0,
            activeforeground="#F2F2F2",
            activebackground="#0c325c").place(x=506, y=85)

            Label(self.master,
            text="Notes",
            fg="#0c325c",
            font=("Roboto", 14, "bold"),
            bg="#12c8bb",
            borderwidth=0).place(x=322, y=90)
    
    def side_menu(self):
        THREELINE_MENU(self.master, visit = 'Note')
    
    def goto_quizzes(self):
        QUIZ_FOLDER(self.master)

class NOTE_FILES(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("search_light.png"))
        self.backframe()
        self.features()
        print("OPENED: Note Files")

    def backframe(self):
        Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg")).place(x=0, y=0)

    def features(self):

        bg_color = self.master.cget("bg")

        if bg_color == "#121212":
            Label(self.master,
            image=self.search_dark,
            border=0,
            bg=bg_color).place(x=30,y=12)

            Button(self.master,
            image=self.threelinemenu_dark,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=50,y=24)

            Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=bg_color,
            borderwidth=0,
            fg="#e9e9e9").place(x=100, y=30)

        elif bg_color == "#0d9187":

            Label(self.master,
            image=self.search_light,
            border=0,
            bg=bg_color).place(x=30,y=12)

            Button(self.master,
            image=self.threelinemenu_light,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=50,y=24)
            
            Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=bg_color,
            borderwidth=0,
            fg="#e9e9e9").place(x=100, y=30)
    
    def side_menu(self):
        THREELINE_MENU(self.master)

class NOTE_EDITOR(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.backframe()
        self.features()
        print("OPENED: Note Editor")

    def backframe(self):
        Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg")).place(x=0, y=0)

    def features(self):

        bg_color = self.master.cget("bg")

        if bg_color == "#121212":

            Button(self.master,
            image=self.threelinemenu_dark,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=7,y=10)

        elif bg_color == "#0d9187":

            Button(self.master,
            image=self.threelinemenu_light,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=7,y=10)
    
    def side_menu(self):
        THREELINE_MENU(self.master)

class QUIZ_FOLDER(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("search_light.png"))
        self.contentbg_dark = ImageTk.PhotoImage(Image.open("quizzesfolder_dark.png"))
        self.contentbg_light = ImageTk.PhotoImage(Image.open("quizzesfolder_light.png"))
        self.quizbtn_dark = ImageTk.PhotoImage(Image.open("quizzesbutton_dark.png"))
        self.quizbtn_light = ImageTk.PhotoImage(Image.open("quizzesbutton_light.png"))
        self.backframe()
        self.features()
        print("OPENED: Quizzes Folder")

    def backframe(self):
        Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg")).place(x=0, y=0)

    def features(self):

        bg_color = self.master.cget("bg")

        if bg_color == "#121212":
            Label(self.master,
            image=self.search_dark,
            border=0,
            bg=bg_color).place(x=30,y=12)

            Label(self.master,
            image=self.contentbg_dark,
            border=0,).place(x=23,y=70)

            Button(self.master,
            image=self.threelinemenu_dark,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=50,y=24)

            Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=bg_color,
            borderwidth=0,
            fg="#e9e9e9").place(x=100, y=30)

            Button(self.master,
            text="Notes",
            fg=bg_color,
            font=("Roboto", 14, "bold"),
            command=self.goto_notes,
            bg="#A6A6A6",
            borderwidth=0,
            activeforeground=bg_color,
            activebackground="#A6A6A6").place(x=315, y=85)

            Label(self.master,
            text="Quizzes",
            fg="#F2F2F2",
            font=("Roboto", 14, "bold"),
            bg="#2C2C2C",
            borderwidth=0).place(x=512, y=91)
        elif bg_color == "#0d9187":

            Label(self.master,
            image=self.search_light,
            border=0,
            bg=bg_color).place(x=30,y=12)

            Label(self.master,
            image=self.contentbg_light,
            border=0,).place(x=23,y=70)

            Button(self.master,
            image=self.threelinemenu_light,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=50,y=24)
            
            Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=bg_color,
            borderwidth=0,
            fg="#e9e9e9").place(x=100, y=30)

            Button(self.master,
            text="Notes",
            fg="#F2F2F2",
            font=("Roboto", 14, "bold"),
            command=self.goto_notes,
            bg="#0c325c",
            borderwidth=0,
            activeforeground="#F2F2F2",
            activebackground="#0c325c").place(x=315, y=85)

            Label(self.master,
            text="Quizzes",
            fg="#0c325c",
            font=("Roboto", 14, "bold"),
            bg="#12c8bb",
            borderwidth=0).place(x=512, y=91)
    
    def side_menu(self):
        THREELINE_MENU(self.master, visit='Quiz')
    
    def goto_notes(self):
        NOTES_FOLDER(self.master)

class QUIZ_FILES(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("search_light.png"))
        self.backframe()
        self.features()
        print("OPENED: Quiz Files")

    def backframe(self):
        Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg")).place(x=0, y=0)

    def features(self):

        bg_color = self.master.cget("bg")

        if bg_color == "#121212":
            Label(self.master,
            image=self.search_dark,
            border=0,
            bg=bg_color).place(x=30,y=12)

            Button(self.master,
            image=self.threelinemenu_dark,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=50,y=24)

            Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=bg_color,
            borderwidth=0,
            fg="#e9e9e9").place(x=100, y=30)

        elif bg_color == "#0d9187":

            Label(self.master,
            image=self.search_light,
            border=0,
            bg=bg_color).place(x=30,y=12)

            Button(self.master,
            image=self.threelinemenu_light,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=50,y=24)
            
            Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=bg_color,
            borderwidth=0,
            fg="#e9e9e9").place(x=100, y=30)
    
    def side_menu(self):
        THREELINE_MENU(self.master)

class QUIZ_EDITOR(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.backframe()
        self.features()
        print("OPENED: Quiz Editor")

    def backframe(self):
        Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg")).place(x=0, y=0)

    def features(self):

        bg_color = self.master.cget("bg")

        if bg_color == "#121212":

            Button(self.master,
            image=self.threelinemenu_dark,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=7,y=10)

        elif bg_color == "#0d9187":

            Button(self.master,
            image=self.threelinemenu_light,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=7,y=10)
    
    def side_menu(self):
        THREELINE_MENU(self.master)

class RECYCLE_BIN(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("search_light.png"))
        self.backframe()
        self.features()
        print("OPENED: Recycle Bin")

    def backframe(self):
        Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg")).place(x=0, y=0)

    def features(self):

        bg_color = self.master.cget("bg")

        if bg_color == "#121212":
            Label(self.master,
            image=self.search_dark,
            border=0,
            bg=bg_color).place(x=30,y=12)

            Button(self.master,
            image=self.threelinemenu_dark,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=50,y=24)

            Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=bg_color,
            borderwidth=0,
            fg="#e9e9e9").place(x=100, y=30)

        elif bg_color == "#0d9187":

            Label(self.master,
            image=self.search_light,
            border=0,
            bg=bg_color).place(x=30,y=12)

            Button(self.master,
            image=self.threelinemenu_light,
            command=self.side_menu,
            border=0,
            bg=bg_color,
            activebackground=bg_color).place(x=50,y=24)
            
            Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=bg_color,
            borderwidth=0,
            fg="#e9e9e9").place(x=100, y=30)
    
    def side_menu(self):
        THREELINE_MENU(self.master,visit='Bin')

class PROFILE_SETTINGS(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.backframe()
        self.side_menu_icon()    
        print("OPENED: Profile Settings")

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
        THREELINE_MENU(self.master, visit='Profile')

class THREELINE_MENU(customtkinter.CTk):
    def __init__(self, master, visit):
        self.master = master
        self.closemenu_dark = ImageTk.PhotoImage(Image.open("close_dark.png"))
        self.closemenu_light = ImageTk.PhotoImage(Image.open("close_light.png"))
        self.visit = visit

        self.burger_menu()
        print("OPENED: Three-Line Menu")

    def notes_folder(self):
        NOTES_FOLDER(self.master)
    
    def quiz_folder(self):
        QUIZ_FOLDER(self.master)
    
    def recycle_bin(self):
        RECYCLE_BIN(self.master)

    def profile_settings(self):
        PROFILE_SETTINGS(self.master)

    def TBC(self):
        pass

    def burger_menu(self):

        def destroy_threeline():
            threeline_menu.destroy()
            print("CLOSED: Three-Line Menu")
        fg_color = "#ffffff"
        activefg = "#ffffff"
        fontstyle = ("Roboto", 17, "bold")

        if self.master.cget("bg") == "#121212":
            bg_color = "#3B3838"
            activebg = "#2d2d2d"
            clickedbg = "#2d2d2d"
        else: 
            bg_color = "#15559B"
            activebg = "#114681"
            clickedbg = "#114681"
            
        threeline_menu = Frame(self.master,
        width=286,
        height=500,
        background=bg_color)
        threeline_menu.place(x=0, y=0)
        
        if bg_color == "#3B3838":
            close_button = self.closemenu_dark
        else: close_button = self.closemenu_light
        Button(threeline_menu,
        image=close_button,
        command=destroy_threeline,
        border=0,
        bg=bg_color,
        activebackground=bg_color).place(x=7,y=10)
        
        def side_buttons(note, quiz, bin, profile, logout, state):
            
            no_state = []
            for x in state: no_state.append(x)

            Notes = Button(threeline_menu,
            text="     Notes",
            command=self.notes_folder,
            anchor=W,
            font=fontstyle,
            border=0,
            fg=fg_color,
            activeforeground=activefg,
            bg=note,
            activebackground=activebg,
            width=20, 
            disabledforeground=fg_color,
            state=no_state[0])
            Notes.place(x=0,y=75)

            if no_state[0] != 'disabled':
                Notes.bind("<Enter>", lambda _: on_entera(None, Notes))
                Notes.bind("<Leave>", lambda _: on_leavea(None, Notes))
            else: pass
            
            Quizzes = Button(threeline_menu,
            text="     Quizzes",
            anchor=W,
            font=fontstyle,
            command=self.quiz_folder,
            border=0,fg=fg_color,
            activeforeground=activefg,
            bg=quiz,
            activebackground=activebg,
            width=20, 
            disabledforeground=fg_color,
            state=no_state[1])
            Quizzes.place(x=0, y=123)

            if no_state[1] != 'disabled':
                Quizzes.bind("<Enter>", lambda _: on_entera(None, Quizzes))
                Quizzes.bind("<Leave>", lambda _: on_leavea(None, Quizzes))
            else: pass
        
            Recycle_Bin = Button(threeline_menu,
            text="     Recycle Bin",
            anchor=W,font=fontstyle,
            command=self.recycle_bin,
            border=0,
            fg=fg_color,
            activeforeground=activefg,
            bg=bin,
            activebackground=activebg,
            width=20, 
            disabledforeground=fg_color,
            state=no_state[2])
            Recycle_Bin.place(x=0, y=171)

            if no_state[2] != 'disabled':
                Recycle_Bin.bind("<Enter>", lambda _: on_entera(None, Recycle_Bin))
                Recycle_Bin.bind("<Leave>", lambda _: on_leavea(None, Recycle_Bin))
            else: pass
        
            Profile_Settings = Button(threeline_menu,
            text="     Profile Settings",
            anchor=W,
            font=fontstyle,
            command=self.profile_settings,
            border=0,
            fg=fg_color,
            activeforeground=activefg,
            bg=profile,
            activebackground=activebg,
            width=20,
            disabledforeground=fg_color,
            state=no_state[3])
            Profile_Settings.place(x=0, y=219)
            
            if no_state[3] != 'disabled':
                Profile_Settings.bind("<Enter>", lambda _: on_entera(None, Profile_Settings))
                Profile_Settings.bind("<Leave>", lambda _: on_leavea(None, Profile_Settings))
            else: pass
        
            Logout = Button(threeline_menu,
            text="     Logout",
            anchor=W,
            font=fontstyle,
            command=self.TBC,
            border=0,
            fg=fg_color,
            activeforeground=activefg,
            bg=logout,
            activebackground=activebg,
            disabledforeground=fg_color,
            width=20,
            
            state=no_state[4])
            Logout.place(x=0, y=267)

            if no_state[4] != 'disabled':
                Logout.bind("<Enter>", lambda _: on_entera(None, Logout))
                Logout.bind("<Leave>", lambda _: on_leavea(None, Logout))
            else: pass
        
        def on_entera(_, button):
            button['background'] = activebg 
            button['foreground']= activefg 

        def on_leavea(_, button):
            button['background'] = bg_color
            button['foreground']= activefg
    
        if self.visit == 'Note':
            notes_state = ['disabled', 'normal', 'normal', 'normal', 'normal']
            side_buttons(clickedbg, bg_color, bg_color, bg_color, bg_color, notes_state)
        elif self.visit == 'Quiz':
            quiz_state = ['normal', 'disabled', 'normal', 'normal', 'normal']
            side_buttons(bg_color, clickedbg, bg_color, bg_color, bg_color, quiz_state) 
        elif self.visit == 'Bin':
            bin_state = ['normal', 'normal', 'disabled', 'normal','normal']
            side_buttons(bg_color, bg_color, clickedbg, bg_color, bg_color, bin_state) 
        elif self.visit == 'Profile':
            profile_state = ['normal','normal','normal','disabled', 'normal']
            side_buttons(bg_color, bg_color, bg_color, clickedbg, bg_color, profile_state)
        else:
            logout_state = ['normal', 'normal','normal','normal', 'disabled']
            side_buttons(bg_color, bg_color, bg_color, bg_color, clickedbg, logout_state) 
    
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
    the_hundreds = LOGIN(window)
    window.mainloop()
