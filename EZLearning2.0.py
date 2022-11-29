from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import tkinter.messagebox
from tkinter import ttk
from cv2 import line
#pip install pyrebase4
import pyrebase
from pygame import FULLSCREEN
import shutup;shutup.please()
from tkinter import messagebox
from dotenv import load_dotenv
import os


#SAMPLE EMAIL AND PASSWORD FOR LOGIN:
#2@gmail.com
#//////

load_dotenv()

#content(.env)
api_key = os.getenv("api_key")
auth_domain = os.getenv("auth_domain")
database_url = os.getenv("database_url")
project_id = os.getenv("project_id")
storage_bucket = os.getenv("storage_bucket")
messaging_sender_id = os.getenv("messaging_sender_id")
app_id = os.getenv("app_id")
measurement_id = os.getenv("measurement_id")

config = {"apiKey": api_key  ,
  "authDomain": auth_domain,
  "databaseURL": database_url ,
  "projectId": project_id ,
  "storageBucket": storage_bucket ,
  "messagingSenderId": messaging_sender_id,
  "appId": app_id ,
  "measurementId": measurement_id}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

db = firebase.database()
# data = {'name': 'Gelo', 'age': 20}
# db.push(data)

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
            command=self.quicklogin)
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

    def quicklogin(self):
        NOTES_FOLDER(self.master)

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
        self.folder_dark = ImageTk.PhotoImage(Image.open("folder_dark.png"))
        self.folder_light = ImageTk.PhotoImage(Image.open("folder_light.png"))
        self.addbtn_dark = ImageTk.PhotoImage(Image.open("add_dark.png"))
        self.addbtn_light = ImageTk.PhotoImage(Image.open("add_light.png"))
        self.sidebutton_dark = ImageTk.PhotoImage(Image.open("side_button_dark.png"))
        self.sidebutton_light = ImageTk.PhotoImage(Image.open("side_button_light.png"))
        
        self.bg_color = self.master.cget("bg")
        self.rows = 2

        self.backframe()
        self.features()
        print("OPENED: Notes Folder")

    def backframe(self):
        self.main_frame = Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg"))
        self.main_frame.place(x=0, y=0)

    def add_frame(self):
        self.main_frame = Frame(self.master,
        width=500,
        height=200,
        background=self.master.cget("bg"))
        self.main_frame.place(x=200, y=150)

        self.add_entry = Entry(self.main_frame,
        width=40,
        font=("Roboto", 12, "bold"),
        bg="#c2c2c2",
        borderwidth=0,
        fg="#000000")
        self.add_entry.place(x=50, y=50)

        self.okay_btn = Button(self.main_frame,
        text='Submit',
        font=("Comic Sans MS", 11),
        fg='#000000',
        borderwidth=0,
        relief=FLAT,
        width=10,)
        self.okay_btn.place(x=200, y=100)

        self.cancel_btn = Button(self.main_frame,
        text='Cancel',
        font=("Comic Sans MS", 11),
        fg='#000000',
        borderwidth=0,
        relief=FLAT,
        width=10,)
        self.cancel_btn.place(x=200, y=150)

    def content_features(self, search_img, content_img, folder_img, menu_img, quiz_a_fg, quiz_a_bg, notes_fg, notes_bg, btn_img, side_btn):
        
        search_label = Label(self.master,
        image=search_img,
        border=0,
        bg=self.bg_color)
        search_label.place(x=30,y=12)

        content_label = Label(self.master,
        image=content_img,
        border=0,)
        content_label.place(x=23,y=70)

        add_btn = Button(self.master,
        image=btn_img,
        border = 0,
        bg=self.bg_color,
        activebackground=self.bg_color)
        add_btn.place(x=760, y=78)

        # Create frame and canvas
        inline_frame = Frame(content_label, width=727, height=340, bg=notes_bg)
        inline_frame.place(x=90, y=65)

        second_line_frame = Frame(inline_frame, bg=notes_bg)
        second_line_frame.pack(fill=BOTH, expand= 1)

        inline_canvas = Canvas(second_line_frame, width=727, height=333, background=notes_bg, highlightthickness=0)
        inline_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        if self.rows > 3:

            scrollbar = ttk.Scrollbar(second_line_frame,
                orient=VERTICAL,
                command=inline_canvas.yview)
            scrollbar.pack(side=RIGHT, fill=Y, padx=2, pady=1)

            inline_canvas.configure(yscrollcommand=scrollbar.set)
            inline_canvas.bind('<Configure>',
                lambda e: inline_canvas.configure(scrollregion=inline_canvas.bbox("all")))
            inline_canvas.bind_all('<MouseWheel>', 
                lambda event: inline_canvas.yview('scroll', int(-2*(event.delta/120)), 'units'))


        another_frame = Frame(inline_canvas, bg=notes_bg)
        inline_canvas.create_window((0,0), window=another_frame, anchor='nw')

        line_frame = Canvas(another_frame, highlightthickness=0)
        line_frame.grid(row =0, column=0, pady=5, padx=11)

        folder = Button(line_frame,
            image=folder_img,
            command= None,
            border=0,
            bg=notes_bg,
            activebackground=notes_bg)
        folder.pack()

        foldername = Label(line_frame,
        text='Mathematics',
        font=("Arial", 10),
        fg=notes_fg,
        borderwidth=0,
        relief=FLAT,
        width=10,
        background=notes_bg,
        activebackground=self.bg_color,
        height=1)
        foldername.pack(fill=BOTH, expand= 1)

        line_menu =Button(self.master,
        image=menu_img,
        command=self.side_menu,
        border=0,
        bg=self.bg_color,
        activebackground=self.bg_color)
        line_menu.place(x=50,y=24)

        search_entry = Entry(self.master,
        width=74,
        font=("Roboto", 12, "bold"),
        bg=self.bg_color,
        borderwidth=0,
        fg="#e9e9e9")
        search_entry.place(x=100, y=30)

        add_btn = Button(self.master,
        image=btn_img,
        command=self.add_frame,
        border=0,
        bg=self.bg_color,
        activebackground=self.bg_color)
        add_btn.place(x=760, y=78)

        quiz_button = Button(self.master,
        text="Quizzes",
        fg=quiz_a_fg,
        font=("Roboto", 14, "bold"),
        command=self.goto_quizzes,
        bg=quiz_a_bg,
        borderwidth=0,
        activeforeground=quiz_a_fg,
        activebackground=quiz_a_bg)
        quiz_button.place(x=506, y=85)

        notes_label = Label(self.master,
        text="Notes",
        fg=notes_fg,
        font=("Roboto", 14, "bold"),
        bg=notes_bg,
        borderwidth=0)
        notes_label.place(x=322, y=90)

        #SIDE BUTTONS

        text_label = Label(self.master,
        text="Open",
        bg=notes_bg,
        fg=notes_fg,
        )
        text_label.place(x=53, y=196)

        openside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=notes_bg,
        command=self.notes_list,
        activebackground=notes_bg)
        openside_btn.place(x=46, y=150)

        text_label = Label(self.master,
        text="Rename",
        bg=notes_bg,
        fg=notes_fg,
        )
        text_label.place(x=46, y=316)

        renameside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=notes_bg,
        command=self.rename,
        activebackground=notes_bg)
        renameside_btn.place(x=46, y=270)

        text_label = Label(self.master,
        text="Delete",
        bg=notes_bg,
        fg=notes_fg,
        )
        text_label.place(x=51, y=436)

        deleteside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=notes_bg,
        command=self.delete,
        activebackground=notes_bg)
        deleteside_btn.place(x=46, y=390)

    def features(self):

        if self.bg_color == "#121212": self.content_features(self.search_dark, self.contentbg_dark, self.folder_dark, self.threelinemenu_dark, self.bg_color, "#A6A6A6", "#F2F2F2", "#2C2C2C", self.addbtn_dark, self.sidebutton_dark)
            
        elif self.bg_color == "#0d9187": self.content_features(self.search_light, self.contentbg_light, self.folder_light, self.threelinemenu_light, "#F2F2F2", "#0c325c", "#0c325c", "#12c8bb", self.addbtn_light, self.sidebutton_light)

    def notes_list(self):
        NOTE_FILES(self.master)
    
    def rename(self):
        pass

    def delete(self):
        pass

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
        self.contentbg_dark = ImageTk.PhotoImage(Image.open("files_dark.png"))
        self.contentbg_light = ImageTk.PhotoImage(Image.open("files_light.png"))
        self.sidebutton_dark = ImageTk.PhotoImage(Image.open("side_button_dark.png"))
        self.sidebutton_light = ImageTk.PhotoImage(Image.open("side_button_light.png"))
        self.indivfile_dark = ImageTk.PhotoImage(Image.open("filescontent_dark.png"))
        self.indivfile_light = ImageTk.PhotoImage(Image.open("filescontent_light.png"))
        self.bg_color = self.master.cget("bg")

        self.backframe()
        self.features()

        print("OPENED: Note Files")

    def backframe(self):
        self.main_frame = Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg"))
        self.main_frame.place(x=0, y=0)
    
    def content_features(self, search_image, three_line_image, content_img, side_btn, notes_fg, notes_bg, indiv_file):
        self.files_search = Label(self.master,
        image=search_image,
        border=0,
        bg=self.bg_color)
        self.files_search.place(x=30,y=12)

        content_label = Label(self.master,
        image=content_img,
        border=0,)
        content_label.place(x=23,y=110)

        self.files_menu = Button(self.master,
        image=three_line_image,
        command=self.side_menu,
        border=0,
        bg=self.bg_color,
        activebackground=self.bg_color)
        self.files_menu.place(x=50,y=24)

        self.files_entry_search = Entry(self.master,
        width=74,
        font=("Roboto", 12, "bold"),
        bg=self.bg_color,
        borderwidth=0,
        fg="#e9e9e9")
        self.files_entry_search.place(x=100, y=30)

        #SIDE BUTTONS

        text_label = Label(self.master,
        text="Open",
        bg=notes_bg,
        fg=notes_fg,
        )
        text_label.place(x=53, y=183)

        openside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=notes_bg,
        command=self.notes_edit,
        activebackground=notes_bg)
        openside_btn.place(x=46, y=137)

        text_label = Label(self.master,
        text="Rename",
        bg=notes_bg,
        fg=notes_fg,
        )
        text_label.place(x=46, y=250)

        renameside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=notes_bg,
        command=self.rename,
        activebackground=notes_bg)
        renameside_btn.place(x=46, y=204)

        text_label = Label(self.master,
        text="Delete",
        bg=notes_bg,
        fg=notes_fg,
        )
        text_label.place(x=51, y=316)

        deleteside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=notes_bg,
        command=self.delete,
        activebackground=notes_bg)
        deleteside_btn.place(x=46, y=270)

        text_label = Label(self.master,
        text="Share",
        bg=notes_bg,
        fg=notes_fg,
        )
        text_label.place(x=53, y=382)

        shareside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=notes_bg,
        command=self.share,
        activebackground=notes_bg)
        shareside_btn.place(x=46, y=336)

        text_label = Label(self.master,
        text="Export",
        bg=notes_bg,
        fg=notes_fg,
        )
        text_label.place(x=51, y=448)

        exportside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=notes_bg,
        command=self.share,
        activebackground=notes_bg)
        exportside_btn.place(x=46, y=402)

        #END OF SIDE BUTTONS

        #INDIVIDUAL FILES

        self.indivfile = Button(self.master,
        image=indiv_file,
        border=0,
        command=None,
        bg=notes_bg,
        activebackground=notes_bg)
        self.indivfile.place(x=121, y=135)

        
    def features(self):

        if self.bg_color == "#121212": self.content_features(self.search_dark, self.threelinemenu_dark, self.contentbg_dark, self.sidebutton_dark, "#F2F2F2", "#2C2C2C", self.indivfile_dark)
        elif self.bg_color == "#0d9187": self.content_features(self.search_light, self.threelinemenu_light, self.contentbg_light, self.sidebutton_light, "#0c325c", "#12c8bb", self.indivfile_light)

    def side_menu(self):
        THREELINE_MENU(self.master, visit = "Notes_Files")

    def rename(self):
        pass

    def delete(self):
        pass

    def share(self):
        pass

    def export_PDF(self):
        pass

    def notes_edit(self):
        NOTE_EDITOR(self.master)

class NOTE_EDITOR(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))

        self.bg_color = self.master.cget("bg")

        self.backframe()
        self.features()

        print("OPENED: Note Editor")

    def backframe(self):
        self.main_frame = Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg"))
        self.main_frame.place(x=0, y=0)
    
    def content_features(self, three_line_image):

        self.editor_menu = Button(self.master,
        image=three_line_image,
        command=self.side_menu,
        border=0,
        bg=self.bg_color,
        activebackground=self.bg_color)
        self.editor_menu.place(x=7,y=10)



    def features(self):

        if self.bg_color == "#121212": self.content_features(self.threelinemenu_dark)
        elif self.bg_color == "#0d9187": self.content_features(self.threelinemenu_light)

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
        self.sidebutton_dark = ImageTk.PhotoImage(Image.open("side_button_dark.png"))
        self.sidebutton_light = ImageTk.PhotoImage(Image.open("side_button_light.png"))
        self.addbtn_dark = ImageTk.PhotoImage(Image.open("add_dark.png"))
        self.addbtn_light = ImageTk.PhotoImage(Image.open("add_light.png"))
        self.bg_color = self.master.cget("bg")
        
        self.backframe()
        self.features()
        
        print("OPENED: Quizzes Folder")

    def backframe(self):
        self.main_frame = Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg"))
        self.main_frame.place(x=0, y=0)

    def content_features(self, search_image, content_image, three_line_image, notes_a_fg, notes_a_bg, quiz_fg, quiz_bg, side_btn, btn_img):

        self.quiz_search = Label(self.master,
        image=search_image,
        border=0,
        bg=self.bg_color)
        self.quiz_search.place(x=30,y=12)

        quiz_content = Label(self.master,
        image=content_image,
        border=0,)
        quiz_content.place(x=23,y=70)

        self.quiz_line_menu = Button(self.master,
        image=three_line_image,
        command=self.side_menu,
        border=0,
        bg=self.bg_color,
        activebackground=self.bg_color)
        self.quiz_line_menu.place(x=50,y=24)

        self.quiz_search_entry = Entry(self.master,
        width=74,
        font=("Roboto", 12, "bold"),
        bg=self.bg_color,
        borderwidth=0,
        fg="#e9e9e9")
        self.quiz_search_entry.place(x=100, y=30)

        self.notes_button = Button(self.master,
        text="Notes",
        fg=notes_a_fg,
        font=("Roboto", 14, "bold"),
        command=self.goto_notes,
        bg=notes_a_bg,
        borderwidth=0,
        activeforeground=notes_a_fg,
        activebackground=notes_a_bg)
        self.notes_button.place(x=315, y=85)

        self.quiz_label = Label(self.master,
        text="Quizzes",
        fg=quiz_fg,
        font=("Roboto", 14, "bold"),
        bg=quiz_bg,
        borderwidth=0)
        self.quiz_label.place(x=512, y=91)

        add_btn = Button(self.master,
        image=btn_img,
        border = 0,
        bg=self.bg_color,
        activebackground=self.bg_color)
        add_btn.place(x=760, y=78)

        #SIDE BUTTONS

        text_label = Label(self.master,
        text="Open",
        bg=quiz_bg,
        fg=quiz_fg,
        )
        text_label.place(x=53, y=196)

        openside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=quiz_bg,
        command=self.quiz_list,
        activebackground=quiz_bg)
        openside_btn.place(x=46, y=150)

        text_label = Label(self.master,
        text="Rename",
        bg=quiz_bg,
        fg=quiz_fg,
        )
        text_label.place(x=46, y=316)

        renameside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=quiz_bg,
        command=self.rename,
        activebackground=quiz_bg)
        renameside_btn.place(x=46, y=270)

        text_label = Label(self.master,
        text="Delete",
        bg=quiz_bg,
        fg=quiz_fg,
        )
        text_label.place(x=51, y=436)

        deleteside_btn = Button(self.master,
        image=side_btn,
        border=0,
        bg=quiz_bg,
        command=self.delete,
        activebackground=quiz_bg)
        deleteside_btn.place(x=46, y=390)
    
    def features(self):
    
        if self.bg_color == "#121212":

            self.content_features(self.search_dark, self.contentbg_dark, self.threelinemenu_dark, 
            self.bg_color, "#A6A6A6", "#F2F2F2","#2C2C2C", self.sidebutton_dark, self.addbtn_dark)

        elif self.bg_color == "#0d9187":

            self.content_features(self.search_light, self.contentbg_light, self.threelinemenu_light, 
            "#F2F2F2", "#0c325c", "#0c325c","#12c8bb", self.sidebutton_light, self.addbtn_light)

    def side_menu(self):
        THREELINE_MENU(self.master, visit='Quiz')
    
    def goto_notes(self):
        NOTES_FOLDER(self.master)

    def quiz_list(self):
        QUIZ_FILES(self.master)

    def rename(self):
        pass

    def delete(self):
        pass

class QUIZ_FILES(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("search_light.png"))

        self.bg_color = self.master.cget("bg")

        self.backframe()
        self.features()

        print("OPENED: Quiz Files")

    def backframe(self):
        self.main_frame = Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg"))
        self.main_frame.place(x=0, y=0)

    def content_features(self, search_image, three_line_image):
        self.files_search = Label(self.master,
        image=search_image,
        border=0,
        bg= self.bg_color)
        self.files_search.place(x=30,y=12)

        self.files_menu = Button(self.master,
        image=three_line_image,
        command=self.side_menu,
        border=0,
        bg= self.bg_color,
        activebackground= self.bg_color)
        self.files_menu.place(x=50,y=24)

        self.files_entry = Entry(self.master,
        width=74,
        font=("Roboto", 12, "bold"),
        bg= self.bg_color,
        borderwidth=0,
        fg="#e9e9e9")
        self.files_entry.place(x=100, y=30)
    
    def features(self):

        if  self.bg_color == "#121212": self.content_features(self.search_dark, self.threelinemenu_dark)
        elif  self.bg_color == "#0d9187": self.content_features(self.search_light, self.threelinemenu_light)

    def side_menu(self):
        THREELINE_MENU(self.master)

class QUIZ_EDITOR(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))

        self.bg_color = self.master.cget("bg")

        self.backframe()
        self.features()
        self.edit_quiz()

        print("OPENED: Quiz Editor")

    def backframe(self):
        self.main_frame = Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg"))
        self.main_frame.place(x=0, y=0)

    def content_features(self, three_line_image):
        self.search_editor = Button(self.master,
        image=three_line_image,
        command=self.side_menu,
        border=0,
        bg=self.bg_color,
        activebackground=self.bg_color)
        self.search_editor.place(x=7,y=10)

    def features(self):

        if self.bg_color == "#121212": self.content_features(self.threelinemenu_dark)
        elif self.bg_color == "#0d9187": self.content_features(self.threelinemenu_light)

    def show_true_false(self):
        display_true_or_false = self.true_false.get()
        if display_true_or_false == 1:
            print("Chose: True")
        elif display_true_or_false == 2:
            print("Chose: False")
        else:
            print("Something went wrong")

    def show_method(self):
        display_method = self.r1_v.get()
        if display_method == 1:
            self.identfication_frame = LabelFrame(self.label_frame, width=645,
                                                height=70, bg="#00FFFF",
                                                highlightbackground="#104E8B",
                                                highlightthickness=1).grid(row=0, column=0, padx=52, pady=168, sticky="s")

            # self.label_guhit = Label(self.label_frame,bg="red",width=80,height=0).place(x=167,y=303)
            self.answer_entry1 = Entry(self.identfication_frame, bg="#00FFFF",
                                    foreground="#00008B", width=55, font=10).place(x=205, y=308)

            print("SHOW: Identification")

        elif display_method == 2:
            self.identfication_frame = LabelFrame(self.label_frame, width=645, height=70, bg="#00FFFF",
                                                highlightbackground="#104E8B",
                                                highlightthickness=1).grid(row=0, column=0, padx=52, pady=168,
                                                                            sticky="s")

            self.answer_answer = Label(self.identfication_frame, text="Answer:",
                                    foreground="#00008B",
                                    bg="#00FFFF",
                                    font=("arial", 14)
                                    ).place(x=153, y=300)
            self.answer_choices = Label(self.identfication_frame, text="Choices:",
                                        foreground="#00008B",
                                        bg="#00FFFF",
                                        font=("arial", 14)
                                        ).place(x=153, y=324)

            self.answer_entry1 = Entry(self.identfication_frame, bg="#00FFFF",
                                    foreground="#00008B", width=55, font=10).place(x=235, y=302)
            self.answer_entry2 = Entry(self.identfication_frame, bg="#00FFFF",
                                    foreground="#00008B", width=55, font=10).place(x=235, y=324)

            print("SHOW: Multiple Choice")
        elif display_method == 3:
            self.identfication_frame = LabelFrame(self.label_frame, width=645, height=70, bg="#00FFFF",
                                                highlightbackground="#104E8B",
                                                highlightthickness=1).grid(row=0, column=0, padx=52, pady=168,
                                                                            sticky="s")
            self.true_false = IntVar()
            self.true_false.set(None)

            self.rb1 = Radiobutton(self.label_frame, text="True",
                                foreground="#00008B",
                                bg="#00FFFF",
                                variable=self.true_false, value=1,
                                font=("arial", 12),
                                command=self.show_true_false).place(x=275, y=308)
            self.rb2 = Radiobutton(self.label_frame, text="False",
                                foreground="#00008B",
                                bg="#00FFFF",
                                variable=self.true_false, value=2,
                                font=("arial", 12),
                                command=self.show_true_false).place(x=515, y=308)

            print("SHOW: True or False")
        else:
            print("something wrong")


    def edit_quiz(self):
        self.label_frame = LabelFrame(self.master, width=831, height=410, bg="#00FFFF", highlightbackground="#104E8B",
                                    highlightthickness=5).grid(row=0, column=0, padx=32, pady=60)

        self.question_label = Label(self.label_frame,
                                    text="Question: ",
                                    bg="#00FFFF",
                                    foreground="#00008B",
                                    font=("arial", 17)).place(x=75, y=100)

        self.add_question_entry = Entry(self.label_frame, bg="#00FFFF",
                                        foreground="#00008B", width=77, font=50).place(x=100, y=145)

        # Quiz method label
        self.question_label = Label(self.label_frame,
                                    text="Quiz Method: ",
                                    bg="#00FFFF",
                                    foreground="#00008B",
                                    font=("arial", 17)).place(x=75, y=180)
        self.r1_v = IntVar()
        self.r2_v = IntVar()
        self.r1_v.set(None)
        self.r2_v.set(None)

        self.r1 = Radiobutton(self.label_frame, text="Identification",
                            foreground="#00008B",
                            bg="#00FFFF",
                            variable=self.r1_v, value=1,
                            font=("arial", 12),
                            command=self.show_method).place(x=125, y=220)
        self.r2 = Radiobutton(self.label_frame, text="Multiple Choice",
                            foreground="#00008B",
                            bg="#00FFFF",
                            variable=self.r1_v, value=2,
                            font=("arial", 12),
                            command=self.show_method).place(x=350, y=220)
        self.r3 = Radiobutton(self.label_frame, text="True or False",
                            foreground="#00008B",
                            bg="#00FFFF",
                            variable=self.r1_v, value=3,
                            font=("arial", 12),
                            command=self.show_method).place(x=600, y=220)

        self.r4 = Radiobutton(self.label_frame,
                            indicatoron=0,
                            bg="#FF6103",
                            width=7,
                            height=2,
                            activebackground="pink",
                            variable=self.r2_v, value=1,
                            font=("arial", 12)).place(x=91, y=385)

        self.r5 = Radiobutton(self.label_frame,
                            indicatoron=0,
                            bg="#FF6103",
                            width=7,
                            height=2,
                            activebackground="pink",
                            variable=self.r2_v, value=2,
                            font=("arial", 12)).place(x=219, y=385)

        self.r6 = Radiobutton(self.label_frame,
                            indicatoron=0,
                            bg="#FF6103",
                            width=7,
                            height=2,
                            activebackground="pink",
                            variable=self.r2_v, value=3,
                            font=("arial", 12)).place(x=350, y=385)

        self.answer_method_label = Label(self.label_frame, text="Answer:",
                                        bg="#00FFFF",
                                        foreground="#00008B",
                                        font=("arial", 17)).place(x=75, y=255)

        self.submit_button = Button(self.label_frame, text="Add question", bg="#00FFFF",
                                    foreground="#00008B", width=20, font=("arial", 13)).place(x=490, y=385)

    def side_menu(self):
        THREELINE_MENU(self.master)

class RECYCLE_BIN(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("search_light.png"))
        self.bg_color = self.master.cget("bg")

        self.backframe()
        self.features()

        print("OPENED: Recycle Bin")

    def backframe(self):
        self.mainframe = Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg"))
        self.mainframe.place(x=0, y=0)
    
    def content_features(self, search_image, three_line_image):
        
        bin_search = Label(self.master,
        image=search_image,
        border=0,
        bg=self.bg_color)
        bin_search.place(x=30,y=12)

        bin_button = Button(self.master,
        image=three_line_image,
        command=self.side_menu,
        border=0,
        bg=self.bg_color,
        activebackground=self.bg_color)
        bin_button.place(x=50,y=24)

        bin_entry = Entry(self.master,
        width=74,
        font=("Roboto", 12, "bold"),
        bg=self.bg_color,
        borderwidth=0,
        fg="#e9e9e9")
        bin_entry.place(x=100, y=30)

    def features(self):

        if self.bg_color == "#121212": self.content_features(self.search_dark, self.threelinemenu_dark)
        elif self.bg_color == "#0d9187": self.content_features(self.search_light, self.threelinemenu_light)

    def side_menu(self):
        THREELINE_MENU(self.master,visit='Bin')

class PROFILE_SETTINGS(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("3line_light.png"))
        self.settings_template_dark = ImageTk.PhotoImage(Image.open("profilesettings_dark.png"))
        self.settings_template_light = ImageTk.PhotoImage(Image.open("profilesettings_light.png"))
        self.usericon = ImageTk.PhotoImage(Image.open("sample_usericon.png"))
        self.backframe()
        self.side_menu_icon()    
        print("OPENED: Profile Settings")

    def backframe(self):
        self.mainframe = Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg"))
        self.mainframe.place(x=0, y=0)
    
    def side_menu_icon_content(self, three_line_menu, settings_template):

        profile_menu = Button(self.master,
        image=three_line_menu,
        command=self.side_menu,
        border=0,
        bg=self.master.cget("bg"),
        activebackground=self.master.cget("bg"))
        profile_menu.place(x=5,y=8)

        profilesettings_temp =Label(self.master,
        image=settings_template,
        border=0,)
        profilesettings_temp.place(x=240,y=45)

        # self.usericon = (Image.open("sample_usericon.png"))
        # self.resize_usericon = self.usericon.resize((80,80), Image.ANTIALIAS)
        # self.profilephoto = ImageTk.PhotoImage(self.resize_usericon) 
        # self.profile = Label(self.master, 
        # image=self.profile,
        # bd=0,
        # border=0,
        # bg=self.master.cget("bg"),)
        # self.profile.place(x=260, y=75)

    def side_menu_icon(self):
        if self.master.cget("bg") == "#121212": self.side_menu_icon_content(self.threelinemenu_dark, self.settings_template_dark)
        elif self.master.cget("bg") == "#0d9187": self.side_menu_icon_content(self.threelinemenu_light, self.settings_template_light)
           
    def side_menu(self):
        THREELINE_MENU(self.master, visit='Profile')

class LOGOUT(customtkinter.CTk):
    def __init__(self, master):
        messagebox.askquestion('Log out','Are you sure you want to log out?')
        print("Logged out")
        self.master = master
        self.logout()

    def backframe(self):
        self.main_frame = Frame(self.master,
                                width=900,
                                height=500,
                                background=self.master.cget("bg"))
        self.main_frame.place(x=0, y=0)

    def logout(self):
        response = messagebox.askyesno('Log out', 'Are you sure you want to log out?')
        if response == True:
            self.backframe()
            print("Logged out")
            redirect = LOGIN(self.master)
        elif response == False:
            pass

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
        QUIZ_EDITOR(self.master)
    
    def recycle_bin(self):
        RECYCLE_BIN(self.master)

    def profile_settings(self):
        PROFILE_SETTINGS(self.master)

    def TBC(self):
        pass

    def burger_menu(self):

        def destroy_threeline():
            threeline_menu.destroy()

            if self.visit == 'Note': self.notes_folder()
            elif self.visit == 'Quiz': self.quiz_folder()
            elif self.visit == 'Bin': self.recycle_bin()
            elif self.visit == 'Profile': self.profile_settings()
            else: pass

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
        closed = Button(threeline_menu,
        image=close_button,
        command=destroy_threeline,
        border=0,
        bg=bg_color,
        activebackground=bg_color)
        closed.place(x=7,y=10)

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
