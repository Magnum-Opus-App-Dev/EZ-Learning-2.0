import json, uuid, os, customtkinter, pyrebase
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
from tkinter import ttk
from pygame import FULLSCREEN

import shutup;shutup.please()
from dotenv import load_dotenv

from model.Editor import Editor
from model.Folder import Folder
from model.Topic import Topic
from model.User import User
from model.Shared import Share

from tkinter import messagebox

load_dotenv()

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
userId = ''

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


class LOGIN():
    def __init__(self, master):
        self.master = master
        self.master.geometry('900x500')
        self.master.title('EZ-Learning 2.0')
        self.master.iconbitmap("images/Logo.ico")
        self.master.config(bg="#121212")
        
        print("OPENED: Login Feature")

        self._Email = StringVar()
        self._Password = StringVar()

        self.change_appearance("#121212", "images/logo_darkmode.png", "#bbbbbb")

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

    def change_appearance(self, bg, image, fg):
        self.master.config(bg=bg)
        self.logo = (Image.open(image))
        self.resize_logo = self.logo.resize((80, 80), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(self.resize_logo)
        self.canvas = Label(self.master, image=self.photoimage, bd=0)
        self.canvas.place(x=410, y=15)
        self.sub = Label(self.master, text = 'IT 105 - Application Development and Emerging Technologies', justify=LEFT, font = ('Arial',7,'bold'), bg = bg, fg=fg)
        self.sub.place(x=10, y=474)
        self.dev_names = Label(self.master, text = 'Dar, John Homer Sayno\nDela Fuente, Ar-Jay\nEchano, Angelo Millares\nMalubay, Arriana Mae Vargas\nMortiga, Renze Meinard', justify=LEFT, font = ('Roboto',7), bg=bg, fg=fg)
        self.dev_names.place(x=10, y=418)
    
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

        if new_appearance_mode == "Dark": self.change_appearance("#121212", "images/logo_darkmode.png", "#bbbbbb")
        elif new_appearance_mode == "Light": self.change_appearance("#0d9187", "images/logo_lightmode.png", "#2e2e2e")
    
    def login(self):
        if self._Email.get() == '' or self._Password.get() == '': tkinter.messagebox.showinfo('Try Again', 'Please complete the required fields.')
        else:
            try:
                global userId
                login = auth.sign_in_with_email_and_password(self._Email.get(), self._Password.get())
                userId = login['localId']
                NOTES_FOLDER(self.master)
            except Exception as e:
                print(e)
                tkinter.messagebox.showinfo('Error', 'Invalid Email or Password. Try again')

    def quicklogin(self):
        NOTES_FOLDER(self.master)

    def signup(self):
        SIGNUP(self.master)
    
class SIGNUP():

    def __init__(self, master):
        self.master = master

        print("OPENED: Signup Feature")

        self._Username = StringVar()
        self._Email = StringVar()
        self._Password = StringVar()
        self._Confirm_Password = StringVar()

        self.change_appearance("#121212", "images/logo_darkmode.png", "#bbbbbb")

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

    def change_appearance(self, bg, image, fg):
        self.master.config(bg=bg)
        self.logo = (Image.open(image))
        self.resize_logo = self.logo.resize((80, 80), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(self.resize_logo)
        self.canvas = Label(self.master, image=self.photoimage, bd=0)
        self.canvas.place(x=410, y=15)
        self.sub = Label(self.master, text = 'IT 105 - Application Development and Emerging Technologies', justify=LEFT, font = ('Arial',7,'bold'), bg = bg, fg=fg)
        self.sub.place(x=10, y=474)
        self.dev_names = Label(self.master, text = 'Dar, John Homer Sayno\nDela Fuente, Ar-Jay\nEchano, Angelo Millares\nMalubay, Arriana Mae Vargas\nMortiga, Renze Meinard', justify=LEFT, font = ('Roboto',7), bg=bg, fg=fg)
        self.dev_names.place(x=10, y=418)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

        if new_appearance_mode == "Dark": self.change_appearance("#121212", "images/logo_darkmode.png", "#bbbbbb")
        elif new_appearance_mode == "Light": self.change_appearance("#0d9187", "images/logo_lightmode.png", "#2e2e2e")
    
    def signup(self):
        if self._Username.get() == '' or self._Password.get() == '' or self._Email.get() == '' or self._Password.get() == '' or self._Confirm_Password.get() == '': 
            tkinter.messagebox.showinfo('Try Again', 'Please input data')
        else:
            if self._Password.get() != self._Confirm_Password.get():tkinter.messagebox.showinfo('Try Again', 'Your Password do not match')
            else: 
                try:
                    global userId
                    signin = auth.create_user_with_email_and_password(self._Email.get(), self._Password.get())
                    userId = signin['localId']

                    profileId = str(uuid.uuid4())
                    profile = User(profileId, self._Username.get(), self._Email.get(), userId)
                    db.child("User").child(profileId).set(profile.__dict__)
                    NOTES_FOLDER(self.master)
                    
                except:
                    tkinter.messagebox.showinfo('Invalid', 'Email Exist, please input another account')

    def login(self):
        LOGIN(self.master)

class NOTES_FOLDER():
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("images/3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("images/3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("images/search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("images/search_light.png"))
        self.contentbg_dark = ImageTk.PhotoImage(Image.open("images/notesfolder_dark.png"))
        self.contentbg_light = ImageTk.PhotoImage(Image.open("images/notesfolder_light.png"))
        self.folder_dark = ImageTk.PhotoImage(Image.open("images/folder_dark.png"))
        self.folder_light = ImageTk.PhotoImage(Image.open("images/folder_light.png"))
        self.addbtn_dark = ImageTk.PhotoImage(Image.open("images/add_dark.png"))
        self.addbtn_light = ImageTk.PhotoImage(Image.open("images/add_light.png"))
        self.sidebutton_dark = ImageTk.PhotoImage(Image.open("images/side_button_dark.png"))
        self.sidebutton_light = ImageTk.PhotoImage(Image.open("images/side_button_light.png"))
        
        self.messageBox_dark = ImageTk.PhotoImage(Image.open("images/mesbox_dark.png"))
        self.messageBox_light = ImageTk.PhotoImage(Image.open("images/mesbox_light.png"))
        self.bg_color = self.master.cget("bg")
        self.rows = []

        folders = db.child("Folders").get()
        if folders.val() is not None:
            for folder in folders:
                if folder.val()['userId'] == userId:
                    self.rows.append(folder.val())

        files = db.child("Share").get()
        if files.val() is not None:
            for file in files:
                if file.val()['sharedTo'] == userId and file.val()['status'] == 1:
                    sharedFolders = db.child("Folders").get()
                    if sharedFolders.val() is not None:
                        for sharedFolder in sharedFolders:
                            if sharedFolder.val()['folderId'] == file.val()['folderId']:
                                self.rows.append(sharedFolder.val())

        # print(len(self.rows))

        self.backframe()
        self.features()

        print("OPENED: Notes Folder")

    def backframe(self):
        main_frame = Frame(self.master,
            width=900,
            height=500,
            background=self.master.cget("bg"))
        main_frame.place(x=0, y=0)

    def click_button(self, title, command, var=None):

        def submit():
            folderId = str(uuid.uuid4())
            folder = Folder(folderId, add_entry.get().capitalize(), userId)
            db.child("Folders").child(folderId).set(folder.__dict__)
            NOTES_FOLDER(self.master)

        def cancel():
            self.main_frame.destroy()
            NOTES_FOLDER(self.master)
        
        def update():
            db.child("Folders").child(var['folderId']).update({'name': f"{add_entry.get()}"})
            NOTES_FOLDER(self.master)

        def share_folder():
            isUserFound = False
            users = db.child("User").get()
            otherUser = None
            if users.val() is not None:
                for user in users:
                    if user.val()['email'] == add_entry.get() and user.val()['token'] != userId:
                        isUserFound = True
                        otherUser = user
                        break
            if isUserFound is True:
                isAlreadyShared = False
                sharedFiles = db.child("Share").get()
                if sharedFiles.val() is not None:
                    for item in sharedFiles:
                        if item.val()['folderId'] == var['folderId'] and (item.val()['sharedTo'] == otherUser.val()['token'] or item.val()['sharedTo'] == userId):
                            isAlreadyShared = True
                            break
                if isAlreadyShared is False:
                    shareId = var['folderId'] + otherUser.val()['token']
                    share = Share(shareId, var['folderId'], userId, otherUser.val()['token'], 0)
                    db.child("Share").child(shareId).set(share.__dict__)
                    self.main_frame.destroy()
                    NOTES_FOLDER(self.master)
                else:
                    tkinter.messagebox.showinfo('Error', 'Show Message Here.')
            else:
                tkinter.messagebox.showinfo('Error', 'Show Message Here.')


        if self.master.cget("bg") == "#121212":
            mesbox_image = self.messageBox_dark
            fg1 = "Black"
            bg1 = "#7a7a7a"
            bg2 = "#959595"
            bg3 = "#4b4949"
        else: 
            mesbox_image = self.messageBox_light
            fg1 = "White"
            bg1 = "#005f60"
            bg2 = "#047a7b"
            bg3 = "#014344"

        self.main_frame = Frame(self.master,
            width=350,
            height=200,
            background=self.master.cget("bg"))
        self.main_frame.place(x=276, y=170)
        search_label = Label(self.main_frame,
            image=mesbox_image,
            border=0,
            bg=self.master.cget("bg"))
        search_label.place(x=2,y=2)
        add_text = Label(self.main_frame,
            text=title,
            font=("Roboto", 13),
            bg=bg1,
            borderwidth=0,
            fg=fg1)
        add_text.place(x=100, y=35)
        add_entry = Entry(self.main_frame,
            width=24,
            font=("Roboto", 12),
            bg=bg2,
            borderwidth=0,
            fg=fg1)
        add_entry.place(x=65, y=69)
        okay_btn = Button(self.main_frame,
            text='Submit',
            font=("Roboto", 11),
            command=submit if command == 'submit' else update if command == 'update' else share_folder,
            fg=fg1,
            bg=bg3,
            activebackground=bg3,
            borderwidth=0,
            relief=FLAT,
            width=8,)
        okay_btn.place(x=74, y=122)
        cancel_btn = Button(self.main_frame,
            text='Cancel',
            command=cancel,
            font=("Roboto", 11),
            fg=fg1,
            bg=bg1,
            activebackground=bg1,
            borderwidth=0,
            relief=FLAT,
            width=8,)
        cancel_btn.place(x=205, y=122)

    def add_frame(self):
        self.click_button("Folder Name", 'submit')
        
    def content_features(self, search_img, content_img, folder_img, menu_img, quiz_a_fg, quiz_a_bg,
    notes_fg, notes_bg, btn_img, side_btn):

        row = 0
        column = 0

        search_label = Label(self.master,
            image=search_img,
            border=0,
            bg=self.bg_color)
        search_label.place(x=30,y=12)
        content_label = Label(self.master,
            image=content_img,
            border=0,)
        content_label.place(x=23,y=70)

        inline_frame = Frame(content_label, 
            width=727, 
            height=340, 
            bg=notes_bg)
        inline_frame.place(x=90, y=65)

        second_line_frame = Frame(inline_frame,
            bg=notes_bg)
        second_line_frame.pack(fill=BOTH, expand= 1)

        inline_canvas = Canvas(second_line_frame, 
            width=727, 
            height=333, 
            background=notes_bg, 
            highlightthickness=0)
        inline_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        if len(self.rows) > 18:
            scrollbar = ttk.Scrollbar(second_line_frame,
                orient=VERTICAL,
                command=inline_canvas.yview)
            scrollbar.pack(side=RIGHT, fill=Y, padx=2, pady=1)

            inline_canvas.configure(yscrollcommand=scrollbar.set)
            inline_canvas.bind('<Configure>',
                lambda e: inline_canvas.configure(scrollregion=inline_canvas.bbox("all")))
            inline_canvas.bind_all('<MouseWheel>', 
                lambda event: inline_canvas.yview('scroll', int(-2*(event.delta/120)), 'units'))

        another_frame = Frame(inline_canvas, 
            bg=notes_bg)
        inline_canvas.create_window((0,0), window=another_frame, anchor='nw')


        def button(data, state):
            openside_btn.config(state=state)
            openside_btn.config(command=lambda var = data: self.notes_list(var))

            renameside_btn.config(state=state)
            renameside_btn.config(command=lambda var = data: self.rename(var))

            deleteside_btn.config(state=state)
            deleteside_btn.config(command=lambda var = data: self.delete(var))

            shareside_btn.config(state=state)
            shareside_btn.config(command=lambda var = data: self.share(var))

        if self.rows != None:
            # print(self.rows)
            for i in self.rows:
                line_frame = Canvas(another_frame, 
                    highlightthickness=0)
                line_frame.grid(row =row, column=column, pady=5, padx=11)

                folder = Button(line_frame,
                    image=folder_img,
                    command= lambda data=i, state='normal': button(data, state),
                    border=0,
                    bg=notes_bg,
                    activebackground=notes_bg)
                folder.pack()
                foldername = Label(line_frame,
                    text=i['name'],
                    font=("Bahnschrift", 10),
                    fg=notes_fg,
                    borderwidth=0,
                    relief=FLAT,
                    width=10,
                    background=notes_bg,
                    activebackground=self.bg_color,
                    height=1)
                foldername.pack(fill=BOTH, expand= 1)

                constraints = [x for x in range(6, 500, 6)]
   
                if column + 1 in constraints:
                    row += 1
                    column = 0
                    print("row", row)
                    print("column", column)
                else: column += 1

        line_menu = Button(self.master,
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

        text_label = Label(self.master,
                text="Open",
                bg=notes_bg,
                fg=notes_fg)
        text_label.place(x=53, y=183)
        openside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=notes_bg,
            state='disabled',
            activebackground=notes_bg)
        openside_btn.place(x=46, y=137)
        text_label = Label(self.master,
            text="Rename",
            bg=notes_bg,
            fg=notes_fg)
        text_label.place(x=46, y=250)
        renameside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=notes_bg,
            state='disabled',
            activebackground=notes_bg)
        renameside_btn.place(x=46, y=204)
        text_label = Label(self.master,
            text="Delete",
            bg=notes_bg,
            fg=notes_fg)
        text_label.place(x=51, y=316)
        deleteside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=notes_bg,
            state='disabled',
            activebackground=notes_bg)
        deleteside_btn.place(x=46, y=270)

        text_label = Label(self.master,
            text="Share",
            bg=notes_bg,
            fg=notes_fg)
        text_label.place(x=53, y=382)
        shareside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=notes_bg,
            state='disabled',
            activebackground=notes_bg)
        shareside_btn.place(x=46, y=336)

    def features(self):

        if self.bg_color == "#121212": 
            self.content_features(self.search_dark, self.contentbg_dark, self.folder_dark,
            self.threelinemenu_dark, self.bg_color, "#A6A6A6", "#F2F2F2", "#2C2C2C", 
            self.addbtn_dark, self.sidebutton_dark)
        elif self.bg_color == "#0d9187":
            self.content_features(self.search_light, self.contentbg_light, self.folder_light,
            self.threelinemenu_light, "#F2F2F2", "#0c325c", "#0c325c", "#12c8bb", self.addbtn_light,
            self.sidebutton_light)

    def notes_list(self, var):
        NOTE_FILES(self.master, var)
    
    def rename(self, var): 
       self.click_button("Update Folder Name", "update", var)

    def delete(self, var=None):
        db.child("Folders").child(var['folderId']).remove()

        topics = db.child("Topics").get()
        edits = db.child("Editors").get()
        if  topics.val() is not None:
            for topic in topics:
                if var['folderId'] == topic.val()['folderId']:
                    db.child("Topics").child(topic.val()['topicId']).remove()
    
                    if  edits.val() is not None:
                        for edit in edits.each():
                                if edit.key() == topic.val()['topicId']:
                                    db.child("Editors").child(edit.key()).remove()

        NOTES_FOLDER(self.master)
        
    def side_menu(self):
        THREELINE_MENU(self.master, visit = 'Note')
    
    def goto_quizzes(self):
        QUIZ_FOLDER(self.master)
    
    def share(self, var):
        self.click_button("Share your folder to: ", "share", var)

class NOTE_FILES():
    def __init__(self, master, data=None):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("images/3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("images/3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("images/search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("images/search_light.png"))
        self.contentbg_dark = ImageTk.PhotoImage(Image.open("images/files_dark.png"))
        self.contentbg_light = ImageTk.PhotoImage(Image.open("images/files_light.png"))
        self.sidebutton_dark = ImageTk.PhotoImage(Image.open("images/side_button_dark.png"))
        self.sidebutton_light = ImageTk.PhotoImage(Image.open("images/side_button_light.png"))
        self.indivfile_dark = ImageTk.PhotoImage(Image.open("images/filescontent_dark.png"))
        self.indivfile_light = ImageTk.PhotoImage(Image.open("images/filescontent_light.png"))
        self.addbtn_dark = ImageTk.PhotoImage(Image.open("images/add_dark.png"))
        self.addbtn_light = ImageTk.PhotoImage(Image.open("images/add_light.png"))
        self.messageBox_dark = ImageTk.PhotoImage(Image.open("images/mesbox_dark.png"))
        self.messageBox_light = ImageTk.PhotoImage(Image.open("images/mesbox_light.png"))

        self.data = data
        self.rows = []

        topics = db.child("Topics").get()
        if topics.val() is not None:
            for topic in topics:
                if topic.val()['folderId'] == self.data['folderId']:
                    self.rows.append(topic.val())
        
        self.bg_color = self.master.cget("bg")
        self.backframe()
        self.features()

        print("OPENED: Note Files")

    def backframe(self):
        main_frame = Frame(self.master,
            width=900,
            height=500,
            background=self.master.cget("bg"))
        main_frame.place(x=0, y=0)

    def button_file(self, title, command, var=None):
        def submit():
            topicId = str(uuid.uuid4())
            topic = Topic(topicId, add_entry.get().capitalize(), self.data['folderId'])
            db.child("Topics").child(topicId).set(topic.__dict__)
            NOTE_FILES(self.master, self.data)

        def update_files():
            db.child("Topics").child(var['topicId']).update({'name': f"{add_entry.get()}"})
            NOTE_FILES(self.master, self.data)

        def cancel():
            self.main_frame.destroy()

        if self.master.cget("bg") == "#121212":
            mesbox_image = self.messageBox_dark
            fg1 = "Black"
            bg1 = "#7a7a7a"
            bg2 = "#959595"
            bg3 = "#4b4949"
        else:
            mesbox_image = self.messageBox_light
            fg1 = "White"
            bg1 = "#005f60"
            bg2 = "#047a7b"
            bg3 = "#014344"

        self.main_frame = Frame(self.master,
            width=350,
            height=200,
            background=self.master.cget("bg"))
        self.main_frame.place(x=276, y=170)
        search_label = Label(self.main_frame,
            image=mesbox_image,
            border=0,
            bg=self.master.cget("bg"))
        search_label.place(x=2,y=2)
        add_text = Label(self.main_frame,
            text=title,
            font=("Roboto", 13),
            bg=bg1,
            borderwidth=0,
            fg=fg1)
        add_text.place(x=100, y=35)
        add_entry = Entry(self.main_frame,
            width=24,
            font=("Roboto", 12),
            bg=bg2,
            borderwidth=0,
            fg=fg1)
        add_entry.place(x=65, y=69)
        okay_btn = Button(self.main_frame,
            text='Submit',
            command=submit if command == 'submit' else update_files,
            font=("Roboto", 11),
            fg=fg1,
            bg=bg3,
            activebackground=bg3,
            borderwidth=0,
            relief=FLAT,
            width=8,)
        okay_btn.place(x=74, y=122)
        cancel_btn = Button(self.main_frame,
            text='Cancel',
            command=cancel,
            font=("Roboto", 11),
            fg=fg1,
            bg=bg1,
            activebackground=bg1,
            borderwidth=0,
            relief=FLAT,
            width=8,)
        cancel_btn.place(x=205, y=122)
    
    def add_frame(self):
        self.button_file("File Name", 'submit')

    def content_features(self, search_image, three_line_image, content_img, side_btn, notes_fg, notes_bg, indiv_file, btn_img, list_img):
        files_search = Label(self.master,
            image=search_image,
            border=0,
            bg=self.bg_color)
        files_search.place(x=30,y=12)
        content_label = Label(self.master,
            image=content_img,
            border=0)
        content_label.place(x=23,y=110)
        files_menu = Button(self.master,
            image=three_line_image,
            command=self.side_menu,
            border=0,
            bg=self.bg_color,
            activebackground=self.bg_color)
        files_menu.place(x=50,y=24)
        files_entry_search = Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=self.bg_color,
            borderwidth=0,
            fg="#e9e9e9")
        files_entry_search.place(x=100, y=30)

        add_btn = Button(self.master,
            image=btn_img,
            command=self.add_frame,
            border=0,
            bg=self.bg_color,
            activebackground=self.bg_color)
        add_btn.place(x=760, y=78)

        inline_frame = Frame(content_label,
                             width=727,
                             height=340,
                             bg=notes_bg)
        inline_frame.place(x=90, y=35)

        second_line_frame = Frame(inline_frame,
                                  bg=notes_bg)
        second_line_frame.pack(fill=BOTH, expand=1)

        inline_canvas = Canvas(second_line_frame,
                               width=727,
                               height=315,
                               background=notes_bg,
                               highlightthickness=0)
        inline_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        if len(self.rows) > 6:
            scrollbar = ttk.Scrollbar(second_line_frame,
                                      orient=VERTICAL,
                                      command=inline_canvas.yview)
            scrollbar.pack(side=RIGHT, fill=Y, padx=2, pady=1)

            inline_canvas.configure(yscrollcommand=scrollbar.set)
            inline_canvas.bind('<Configure>',
                               lambda e: inline_canvas.configure(scrollregion=inline_canvas.bbox("all")))
            inline_canvas.bind_all('<MouseWheel>',
                                   lambda event: inline_canvas.yview('scroll', int(-2 * (event.delta / 120)), 'units'))

        another_frame = Frame(inline_canvas,
                              bg=notes_bg)
        inline_canvas.create_window((0, 0), window=another_frame, anchor='nw')

        def editor_button(data, state):
            
            openside_btn.config(state=state)
            openside_btn.config(command= lambda var=data: self.notes_edit(var))

            renameside_btn.config(state=state)
            renameside_btn.config(command= lambda var=data: self.rename(var))

            deleteside_btn.config(state=state)
            deleteside_btn.config(command= lambda var=data: self.delete(var))
            
        if self.rows != None:
            print(self.rows)
            for i in self.rows:
                line_frame = Canvas(another_frame,
                                    highlightthickness=0)
                line_frame.pack(pady=5, padx=11)

                folder = Label(line_frame,
                               image=indiv_file,
                               border=0,
                               bg=notes_bg,
                               activebackground=notes_bg).pack()
                foldername = Button(line_frame,
                                    text=i['name'],
                                    font=("Arial", 15),
                                    justify="left",
                                    anchor="w",
                                    fg=notes_fg,
                                    borderwidth=0,
                                    relief=FLAT,
                                    width=20,
                                    background=list_img,
                                    command=lambda data=i, state='normal': editor_button(data, state),
                                    activebackground=list_img,
                                    height=1).place(x=10, y=5)


        text_label = Label(self.master,
            text="Open",
            bg=notes_bg,
            fg=notes_fg)
        text_label.place(x=53, y=183)
        openside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=notes_bg,
            state='disabled',
            activebackground=notes_bg)
        openside_btn.place(x=46, y=137)
        text_label = Label(self.master,
            text="Rename",
            bg=notes_bg,
            fg=notes_fg)
        text_label.place(x=46, y=250)
        renameside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=notes_bg,
            state='disabled',
            activebackground=notes_bg)
        renameside_btn.place(x=46, y=204)
        text_label = Label(self.master,
            text="Delete",
            bg=notes_bg,
            fg=notes_fg)
        text_label.place(x=51, y=316)
        deleteside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=notes_bg,
            state='disabled',
            activebackground=notes_bg)
        deleteside_btn.place(x=46, y=270)
        text_label = Label(self.master,
            text="Back",
            bg=notes_bg,
            fg=notes_fg)
        text_label.place(x=55, y=382)
        shareside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=notes_bg,
            command=lambda : NOTES_FOLDER(self.master),
            activebackground=notes_bg)
        shareside_btn.place(x=46, y=336)
        # text_label = Label(self.master,
        #     text="Export",
        #     bg=notes_bg,
        #     fg=notes_fg,)
        # text_label.place(x=51, y=448)
        # exportside_btn = Button(self.master,
        #     image=side_btn,
        #     border=0,
        #     bg=notes_bg,
        #     command=self.share,
        #     activebackground=notes_bg)
        # exportside_btn.place(x=46, y=402)

    def features(self):

        if self.bg_color == "#121212": 
            self.content_features(self.search_dark, self.threelinemenu_dark, self.contentbg_dark,
            self.sidebutton_dark, "#F2F2F2", "#2C2C2C", self.indivfile_dark, self.addbtn_dark, "#969696")
        elif self.bg_color == "#0d9187": 
            self.content_features(self.search_light, self.threelinemenu_light, self.contentbg_light, 
            self.sidebutton_light, "#0c325c", "#12c8bb", self.indivfile_light, self.addbtn_light, "#92d050")

    def side_menu(self):
        THREELINE_MENU(self.master, visit=None)

    def rename(self, var):
        self.button_file("Update File Name", "update", var)

    def delete(self, var):
        db.child("Topics").child(var['topicId']).remove()
        edits = db.child("Editors").get()

        if edits.val() is not None:
            for edit in edits.each():
                if edit.key() == var['topicId']:
                    db.child("Editors").child(edit.key()).remove()
        NOTE_FILES(self.master, self.data)
    def share(self, var):
        pass

    # def export_PDF(self, var):
    #     pass

    def notes_edit(self, var):
        NOTE_EDITOR(self.master, var)

class NOTE_EDITOR():
    def __init__(self, master, data=None):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("images/3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("images/3line_light.png"))
        self.contentbg_dark = ImageTk.PhotoImage(Image.open("images/editor_dark.png"))
        self.contentbg_light = ImageTk.PhotoImage(Image.open("images/editor_light.png"))
        self.sidebutton_dark = ImageTk.PhotoImage(Image.open("images/side_button_dark.png"))
        self.sidebutton_light = ImageTk.PhotoImage(Image.open("images/side_button_light.png"))
        
        self.data = data
        self.contents = ''

        editors = db.child("Editors").get()
        if editors.val() is not None:
            for editor in editors:
                if editor.key() == self.data['topicId']:
                    self.contents = editor.val()['notes']
        
        self.bg_color = self.master.cget("bg")
        self.backframe()
        self.features()

        print("OPENED: Note Editor")

    def backframe(self):
        main_frame = Frame(self.master,
            width=900,
            height=500,
            background=self.master.cget("bg"))
        main_frame.place(x=0, y=0)
    
    def content_features(self, three_line_image, content_img, notes_fg, notes_bg, side_btn):
        
        def save():
            editor = Editor(Text_Entry.get(1.0, "end-1c"))
            db.child("Editors").child(self.data['topicId']).set(editor.__dict__)
            NOTE_FILES(self.master, self.data)

        editor_menu = Button(self.master,
            image=three_line_image,
            command=self.side_menu,
            border=0,
            bg=self.bg_color,
            activebackground=self.bg_color)
        editor_menu.place(x=7,y=10)
        content_label = Label(self.master,
            image=content_img,
            border=0,)
        content_label.place(x=23,y=45)
        if self.master.cget("bg") == "#121212":
            background = "#2c2c2c"
            foreground = "White"
        else:
            background = "#12c8bb"
            foreground = "Black"
        Text_Entry = Text(self.master,
            bg=background,
            height=19,
            width=78,
            font=("Roboto", 12),
            fg=foreground,
            borderwidth=0)
        Text_Entry.insert("end-1c", self.contents)
        Text_Entry.place(x=135, y=80)
        text_label = Label(self.master,
            text="Save",
            bg=notes_bg,
            fg=notes_fg)
        text_label.place(x=56, y=126)
        saveside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=notes_bg,
            command=save,
            activebackground=notes_bg)
        saveside_btn.place(x=46, y=80)
        text_label = Label(self.master,
            text="Export",
            bg=notes_bg,
            fg=notes_fg)
        text_label.place(x=53, y=286)
        shareside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=notes_bg,
            command=self.export,
            activebackground=notes_bg)
        shareside_btn.place(x=46, y=240)
        text_label = Label(self.master,
            text="Back",
            bg=notes_bg,
            fg=notes_fg)
        text_label.place(x=55, y=436)
        exportside_btn = Button(self.master,
            image=side_btn,
            command=lambda: NOTE_FILES(self.master, self.data),
            border=0,
            bg=notes_bg,
            activebackground=notes_bg)
        exportside_btn.place(x=46, y=390)

    def features(self):

        if self.bg_color == "#121212": self.content_features(self.threelinemenu_dark,
        self.contentbg_dark, "#F2F2F2", "#2C2C2C", self.sidebutton_dark)
        elif self.bg_color == "#0d9187": self.content_features(self.threelinemenu_light,
        self.contentbg_light, "#0c325c", "#12c8bb", self.sidebutton_light)

    def side_menu(self):
        THREELINE_MENU(self.master, visit=None)
    
    def export(self):
        pass

class QUIZ_FOLDER():
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("images/3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("images/3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("images/search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("images/search_light.png"))
        self.contentbg_dark = ImageTk.PhotoImage(Image.open("images/quizzesfolder_dark.png"))
        self.contentbg_light = ImageTk.PhotoImage(Image.open("images/quizzesfolder_light.png"))
        self.sidebutton_dark = ImageTk.PhotoImage(Image.open("images/side_button_dark.png"))
        self.sidebutton_light = ImageTk.PhotoImage(Image.open("images/side_button_light.png"))
        self.addbtn_dark = ImageTk.PhotoImage(Image.open("images/add_dark.png"))
        self.addbtn_light = ImageTk.PhotoImage(Image.open("images/add_light.png"))
        self.messageBox_dark = ImageTk.PhotoImage(Image.open("images/mesbox_dark.png"))
        self.messageBox_light = ImageTk.PhotoImage(Image.open("images/mesbox_light.png"))
        self.bg_color = self.master.cget("bg")
        self.backframe()
        self.features()
        
        print("OPENED: Quizzes Folder")

    def backframe(self):
        main_frame = Frame(self.master,
            width=900,
            height=500,
            background=self.master.cget("bg"))
        main_frame.place(x=0, y=0)

    def add_frame(self):
        if self.master.cget("bg") == "#121212":
            mesbox_image = self.messageBox_dark
            fg1 = "Black"
            bg1 = "#7a7a7a"
            bg2 = "#959595"
            bg3 = "#4b4949"
        else: 
            mesbox_image = self.messageBox_light
            fg1 = "White"
            bg1 = "#005f60"
            bg2 = "#047a7b"
            bg3 = "#014344"
        self.main_frame = Frame(self.master,
            width=350,
            height=200,
            background=self.master.cget("bg"))
        self.main_frame.place(x=276, y=170)
        search_label = Label(self.main_frame,
            image=mesbox_image,
            border=0,
            bg=self.master.cget("bg"))
        search_label.place(x=2,y=2)
        add_text = Label(self.main_frame,
            text="Folder Name",
            font=("Roboto", 13),
            bg=bg1,
            borderwidth=0,
            fg=fg1)
        add_text.place(x=123, y=35)
        add_entry = Entry(self.main_frame,
            width=24,
            font=("Roboto", 12),
            bg=bg2,
            borderwidth=0,
            fg=fg1)
        add_entry.place(x=65, y=69)
        okay_btn = Button(self.main_frame,
            text='Submit',
            font=("Roboto", 11),
            fg=fg1,
            bg=bg3,
            activebackground=bg3,
            borderwidth=0,
            relief=FLAT,
            width=8,)
        okay_btn.place(x=74, y=122)
        cancel_btn = Button(self.main_frame,
            text='Cancel',
            font=("Roboto", 11),
            fg=fg1,
            bg=bg1,
            activebackground=bg1,
            borderwidth=0,
            relief=FLAT,
            width=8,)
        cancel_btn.place(x=205, y=122)

    def content_features(self, search_image, content_image, three_line_image, notes_a_fg, notes_a_bg, quiz_fg, quiz_bg, side_btn, btn_img):
        quiz_search = Label(self.master,
            image=search_image,
            border=0,
            bg=self.bg_color)
        quiz_search.place(x=30,y=12)
        quiz_content = Label(self.master,
            image=content_image,
            border=0,)
        quiz_content.place(x=23,y=70)
        quiz_line_menu = Button(self.master,
            image=three_line_image,
            command=self.side_menu,
            border=0,
            bg=self.bg_color,
            activebackground=self.bg_color)
        quiz_line_menu.place(x=50,y=24)
        quiz_search_entry = Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=self.bg_color,
            borderwidth=0,
            fg="#e9e9e9")
        quiz_search_entry.place(x=100, y=30)
        notes_button = Button(self.master,
            text="Notes",
            fg=notes_a_fg,
            font=("Roboto", 14, "bold"),
            command=self.goto_notes,
            bg=notes_a_bg,
            borderwidth=0,
            activeforeground=notes_a_fg,
            activebackground=notes_a_bg)
        notes_button.place(x=315, y=85)
        quiz_label = Label(self.master,
            text="Quizzes",
            fg=quiz_fg,
            font=("Roboto", 14, "bold"),
            bg=quiz_bg,
            borderwidth=0)
        quiz_label.place(x=512, y=91)
        add_btn = Button(self.master,
            image=btn_img,
            command=self.add_frame,
            border=0,
            bg=self.bg_color,
            activebackground=self.bg_color)
        add_btn.place(x=760, y=78)
        text_label = Label(self.master,
            text="Open",
            bg=quiz_bg,
            fg=quiz_fg)
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
            fg=quiz_fg)
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
            fg=quiz_fg)
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

class QUIZ_FILES():
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("images/3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("images/3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("images/search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("images/search_light.png"))
        self.contentbg_dark = ImageTk.PhotoImage(Image.open("images/files_dark.png"))
        self.contentbg_light = ImageTk.PhotoImage(Image.open("images/files_light.png"))
        self.sidebutton_dark = ImageTk.PhotoImage(Image.open("images/side_button_dark.png"))
        self.sidebutton_light = ImageTk.PhotoImage(Image.open("images/side_button_light.png"))
        self.indivfile_dark = ImageTk.PhotoImage(Image.open("images/filescontent_dark.png"))
        self.indivfile_light = ImageTk.PhotoImage(Image.open("images/filescontent_light.png"))
        self.addbtn_dark = ImageTk.PhotoImage(Image.open("images/add2_dark.png"))
        self.addbtn_light = ImageTk.PhotoImage(Image.open("images/add2_light.png"))
        self.messageBox_dark = ImageTk.PhotoImage(Image.open("images/mesbox_dark.png"))
        self.messageBox_light = ImageTk.PhotoImage(Image.open("images/mesbox_light.png"))
        self.bg_color = self.master.cget("bg")
        self.backframe()
        self.features()

        print("OPENED: Quiz Files")

    def backframe(self):
        main_frame = Frame(self.master,
            width=900,
            height=500,
            background=self.master.cget("bg"))
        main_frame.place(x=0, y=0)

    def add_frame(self):
        if self.master.cget("bg") == "#121212":
            mesbox_image = self.messageBox_dark
            fg1 = "Black"
            bg1 = "#7a7a7a"
            bg2 = "#959595"
            bg3 = "#4b4949"
        else: 
            mesbox_image = self.messageBox_light
            fg1 = "White"
            bg1 = "#005f60"
            bg2 = "#047a7b"
            bg3 = "#014344"
        self.main_frame = Frame(self.master,
            width=350,
            height=200,
            background=self.master.cget("bg"))
        self.main_frame.place(x=276, y=170)
        search_label = Label(self.main_frame,
            image=mesbox_image,
            border=0,
            bg=self.master.cget("bg"))
        search_label.place(x=2,y=2)
        add_text = Label(self.main_frame,
            text="File Name",
            font=("Roboto", 13),
            bg=bg1,
            borderwidth=0,
            fg=fg1)
        add_text.place(x=137, y=35)
        add_entry = Entry(self.main_frame,
            width=24,
            font=("Roboto", 12),
            bg=bg2,
            borderwidth=0,
            fg=fg1)
        add_entry.place(x=65, y=69)
        okay_btn = Button(self.main_frame,
            text='Submit',
            font=("Roboto", 11),
            fg=fg1,
            bg=bg3,
            activebackground=bg3,
            borderwidth=0,
            relief=FLAT,
            width=8,)
        okay_btn.place(x=74, y=122)
        cancel_btn = Button(self.main_frame,
            text='Cancel',
            font=("Roboto", 11),
            fg=fg1,
            bg=bg1,
            activebackground=bg1,
            borderwidth=0,
            relief=FLAT,
            width=8,)
        cancel_btn.place(x=205, y=122)
    
    def content_features(self, search_image, three_line_image, content_img, side_btn, quiz_fg, quiz_bg, indiv_file, btn_img):
        files_search = Label(self.master,
            image=search_image,
            border=0,
            bg=self.bg_color)
        files_search.place(x=30,y=12)
        content_label = Label(self.master,
            image=content_img,
            border=0,)
        content_label.place(x=23,y=110)
        files_menu = Button(self.master,
            image=three_line_image,
            command=self.side_menu,
            border=0,
            bg=self.bg_color,
            activebackground=self.bg_color)
        files_menu.place(x=50,y=24)
        files_entry_search = Entry(self.master,
            width=74,
            font=("Roboto", 12, "bold"),
            bg=self.bg_color,
            borderwidth=0,
            fg="#e9e9e9")
        files_entry_search.place(x=100, y=30)
        text_label = Label(self.master,
            text="Open",
            bg=quiz_bg,
            fg=quiz_fg,)
        text_label.place(x=53, y=183)
        openside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=quiz_bg,
            command=self.quizzes_edit,
            activebackground=quiz_bg)
        openside_btn.place(x=46, y=137)
        text_label = Label(self.master,
            text="Rename",
            bg=quiz_bg,
            fg=quiz_fg,)
        text_label.place(x=46, y=250)
        renameside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=quiz_bg,
            command=self.rename,
            activebackground=quiz_bg)
        renameside_btn.place(x=46, y=204)
        text_label = Label(self.master,
            text="Delete",
            bg=quiz_bg,
            fg=quiz_fg,)
        text_label.place(x=51, y=316)
        deleteside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=quiz_bg,
            command=self.delete,
            activebackground=quiz_bg)
        deleteside_btn.place(x=46, y=270)
        text_label = Label(self.master,
            text="Share",
            bg=quiz_bg,
            fg=quiz_fg)
        text_label.place(x=53, y=382)
        shareside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=quiz_bg,
            command=self.share,
            activebackground=quiz_bg)
        shareside_btn.place(x=46, y=336)
        text_label = Label(self.master,
            text="Play Quiz",
            bg=quiz_bg,
            fg=quiz_fg)
        text_label.place(x=51, y=448)
        playside_btn = Button(self.master,
            image=side_btn,
            border=0,
            bg=quiz_bg,
            command=self.play,
            activebackground=quiz_bg)
        playside_btn.place(x=46, y=402)
        self.indivfile = Button(self.master,
            image=indiv_file,
            border=0,
            command=None,
            bg=quiz_bg,
            activebackground=quiz_bg)
        self.indivfile.place(x=121, y=135)
        add_btn = Button(self.master,
            image=btn_img,
            command=self.add_frame,
            border=0,
            bg=self.bg_color,
            activebackground=self.bg_color)
        add_btn.place(x=760, y=78)
        
    def features(self):
        if self.bg_color == "#121212": 
            self.content_features(self.search_dark, self.threelinemenu_dark, self.contentbg_dark,
            self.sidebutton_dark, "#F2F2F2", "#2C2C2C", self.indivfile_dark, self.addbtn_dark)
        elif self.bg_color == "#0d9187": 
            self.content_features(self.search_light, self.threelinemenu_light, self.contentbg_light, 
            self.sidebutton_light, "#0c325c", "#12c8bb", self.indivfile_light, self.addbtn_light)

    def side_menu(self):
        THREELINE_MENU(self.master, visit=None)

    def rename(self):
        pass

    def delete(self):
        pass

    def share(self):
        pass

    def play(self):
        pass

    def quizzes_edit(self):
        QUIZ_EDITOR(self.master)

class QUIZ_EDITOR():
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("images/3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("images/3line_light.png"))
        self.contentbg_dark = ImageTk.PhotoImage(Image.open("images/editor_dark.png"))
        self.contentbg_light = ImageTk.PhotoImage(Image.open("images/editor_light.png"))
        self.answerbg_dark = ImageTk.PhotoImage(Image.open("images/ansquiz_dark.png"))
        self.answerbg_light = ImageTk.PhotoImage(Image.open("images/ansquiz_light.png"))
        self.bg_color = self.master.cget("bg")
        self.backframe()
        self.features()
        self.blockframe()

        print("OPENED: Quiz Editor")

    def backframe(self):
        main_frame = Frame(self.master,
        width=900,
        height=500,
        background=self.master.cget("bg"))
        main_frame.place(x=0, y=0)

    def show_true_false(self):
        display_true_or_false = self.true_false.get()

        if display_true_or_false == 1:
            print("CHOSE: True")
        elif display_true_or_false == 2:
            print("CHOSE: False")
        else:
            print("ERROR: Something Went Wrong")

    def content_features(self, three_line_image, content_img, content_fg, content_bg):
        search_editor = Button(self.master,
            image=three_line_image,
            command=self.side_menu,
            border=0,
            bg=self.bg_color,
            activebackground=self.bg_color)
        search_editor.place(x=7,y=10)
        content_label = Label(self.master,
            image=content_img,
            border=0,)
        content_label.place(x=23,y=45)
        question_label = Label(self.master,
            text="Question:",
            bg=content_bg,
            foreground=content_fg,
            font=("arial", 15))
        question_label.place(x=130, y=80)
        add_question_entry = Entry(self.master,
            bg=content_bg, 
            foreground=content_fg, 
            width=78, 
            font=50)
        add_question_entry.place(x=133, y=120)
        question_label = Label(self.master,
            text="Quiz Method: ",
            bg=content_bg,
            foreground=content_fg,
            font=("arial", 15))
        question_label.place(x=130, y=160)

        self.r1_v = IntVar()
        self.r2_v = IntVar()
        self.r1_v.set(None)
        self.r2_v.set(None)

        method_one = Radiobutton(self.master, 
            text="Identification",
            foreground=content_fg,
            bg=content_bg,
            variable=self.r1_v, value=1,
            font=("arial", 12),
            activebackground=content_bg,
            command=self.show_method)
        method_one.place(x=190, y=200)
        method_two = Radiobutton(self.master, 
            text="Multiple Choice",
            foreground=content_fg,
            bg=content_bg,
            variable=self.r1_v, value=2,
            font=("arial", 12),
            activebackground=content_bg,
            command=self.show_method)
        method_two.place(x=415, y=200)
        method_three = Radiobutton(self.master, 
            text="True or False",
            foreground=content_fg,
            bg=content_bg,
            variable=self.r1_v, value=3,
            font=("arial", 12),
            activebackground=content_bg,
            command=self.show_method)
        method_three.place(x=665, y=200)
        answer_label = Label(self.master, 
            text="Answer:",
            bg=content_bg,
            foreground=content_fg,
            font=("arial", 15))
        answer_label.place(x=130, y=230)
        new_question = Button(self.master,
            text="Add Question", 
            bg=content_bg,
            foreground=content_fg,
            width=15,
            font=("arial", 13))
        new_question.place(x=695, y=410)

    def features(self):
        if self.bg_color == "#121212": 
            self.content_features(self.threelinemenu_dark, self.contentbg_dark, "#F2F2F2", "#2C2C2C",)
        elif self.bg_color == "#0d9187": 
            self.content_features(self.threelinemenu_light, self.contentbg_light, "#0c325c", "#12c8bb")

    def blockframe(self):
        if self.bg_color == "#121212": bg = self.answerbg_dark
        elif self.bg_color == "#0d9187": bg = self.answerbg_light
        content_label = Label(self.master,
            image=bg,
            border=0,)
        content_label.place(x=143,y=260)

    def show_method(self):
        if self.bg_color == "#121212": 
            color = "#2c2c2c"
            fg = "#a4a4a4"
        elif self.bg_color == "#0d9187": 
            color = "#12c8bb"
            fg = "#0c325c"
        display_method = self.r1_v.get()
        
        if display_method == 1:
            self.blockframe()
            answer_entry = Entry(self.master,
                bg=color,
                foreground=fg,
                width=55, 
                font=14)
            answer_entry.place(x=235, y=305)
            print("SHOW: Identification")
        elif display_method == 2:
            self.blockframe()
            answer_label = Label(self.master, text="Answer:",
                foreground=fg,
                bg=color,
                font=("arial", 14))
            answer_label.place(x=201, y=291)
            choices_label = Label(self.master, text="Choices:",
                foreground=fg,
                bg=color,
                font=("arial", 14))
            choices_label.place(x=195, y=316)
            answer = Entry(self.master,
                bg=color,
                foreground=fg,
                width=55, 
                font=10)
            answer.place(x=280, y=295)
            choices = Entry(self.master,
                bg=color,
                foreground=fg,
                width=55,
                font=10)
            choices.place(x=280, y=317)
            print("SHOW: Multiple Choice")
        elif display_method == 3:
            self.blockframe()
            self.true_false = IntVar()
            self.true_false.set(None)
            self.rb1 = Radiobutton(self.master, text="True",
                foreground=fg,
                bg=color,
                variable=self.true_false, 
                value=1,
                font=("arial", 14),
                command=self.show_true_false).place(x=325, y=299)
            self.rb2 = Radiobutton(self.master, text="False",
                foreground=fg,
                bg=color,
                variable=self.true_false, 
                value=2,
                font=("arial", 14),
                command=self.show_true_false).place(x=555, y=299)
            print("SHOW: True or False")
        else:
            print("ERROR: Something Went Wrong")

    def side_menu(self):
        THREELINE_MENU(self.master, visit=None)

class RECYCLE_BIN():
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("images/3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("images/3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("images/search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("images/search_light.png"))
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

        if self.bg_color == "#121212": 
            self.content_features(self.search_dark, self.threelinemenu_dark)
        elif self.bg_color == "#0d9187": 
            self.content_features(self.search_light, self.threelinemenu_light)

    def side_menu(self):
        THREELINE_MENU(self.master,visit='Bin')

class PROFILE_SETTINGS():
    def __init__(self, master):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("images/3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("images/3line_light.png"))
        self.settings_template_dark = ImageTk.PhotoImage(Image.open("images/profilesettings_dark.png"))
        self.settings_template_light = ImageTk.PhotoImage(Image.open("images/profilesettings_light.png"))
        self.usericon = ImageTk.PhotoImage(Image.open("images/sample_usericon.png"))
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

        profilesettings_temp = Label(self.master,
            image=settings_template,
            border=0,)
        profilesettings_temp.place(x=240,y=45)

    def side_menu_icon(self):
        if self.master.cget("bg") == "#121212": self.side_menu_icon_content(self.threelinemenu_dark, self.settings_template_dark)
        elif self.master.cget("bg") == "#0d9187": self.side_menu_icon_content(self.threelinemenu_light, self.settings_template_light)
           
    def side_menu(self):
        THREELINE_MENU(self.master, visit='Profile')

class LOGOUT():
    def __init__(self, master):
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
            print("CLOSED: Logged Out")
            LOGIN(self.master)
        elif response == False:
            pass

class SHARED_FILES():

    def __init__(self, master, type):
        self.master = master
        self.threelinemenu_dark = ImageTk.PhotoImage(Image.open("images/3line_dark.png"))
        self.threelinemenu_light = ImageTk.PhotoImage(Image.open("images/3line_light.png"))
        self.search_dark = ImageTk.PhotoImage(Image.open("images/search_dark.png"))
        self.search_light = ImageTk.PhotoImage(Image.open("images/search_light.png"))
        self.contentbg_dark = ImageTk.PhotoImage(Image.open("images/notesfolder_dark.png"))
        self.contentbg_light = ImageTk.PhotoImage(Image.open("images/notesfolder_light.png"))
        self.quizbtn_dark = ImageTk.PhotoImage(Image.open("images/quizzesfolder_dark.png"))
        self.quizbtn_light = ImageTk.PhotoImage(Image.open("images/quizzesfolder_light.png"))
        self.folder_dark = ImageTk.PhotoImage(Image.open("images/folder_dark.png"))
        self.folder_light = ImageTk.PhotoImage(Image.open("images/folder_light.png"))
        self.sidebutton_dark = ImageTk.PhotoImage(Image.open("images/side_button_dark.png"))
        self.sidebutton_light = ImageTk.PhotoImage(Image.open("images/side_button_light.png"))

        self.rows = []

        files = db.child("Share").get()
        if files.val() is not None:
            for file in files:
                if file.val()['sharedTo'] == userId and file.val()['status'] == 0:
                    topics = db.child("Folders").get()
                    if topics.val() is not None:
                        for topic in topics:
                            if topic.val()['folderId'] == file.val()['folderId']:
                                self.rows.append({**topic.val(), **file.val()})

        self.bg_color = self.master.cget("bg")
        self.type = type

        self.backframe()
        self.features()

        print("OPENED: Shared Folder")

    def backframe(self):
        main_frame = Frame(self.master,
                           width=900,
                           height=500,
                           background=self.master.cget("bg"))
        main_frame.place(x=0, y=0)


    def click_button(self, title, command, var=None):
        pass


    def add_frame(self):
        self.click_button("Folder Name", 'submit')


    def content_features(self, search_img, content_img, folder_img, menu_img, afg, abg,
                         fg, bg, side_btn):
        row = 0
        column = 0

        search_label = Label(self.master,
                             image=search_img,
                             border=0,
                             bg=self.bg_color)
        search_label.place(x=30, y=12)
        content_label = Label(self.master,
                              image=content_img,
                              border=0, )
        content_label.place(x=23, y=70)

        inline_frame = Frame(content_label,
                             width=727,
                             height=340,
                             bg=bg)
        inline_frame.place(x=90, y=65)

        second_line_frame = Frame(inline_frame,
                                  bg=bg)
        second_line_frame.pack(fill=BOTH, expand=1)

        inline_canvas = Canvas(second_line_frame,
                               width=727,
                               height=333,
                               background=bg,
                               highlightthickness=0)
        inline_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        if len(self.rows) > 18:
            scrollbar = ttk.Scrollbar(second_line_frame,
                                      orient=VERTICAL,
                                      command=inline_canvas.yview)
            scrollbar.pack(side=RIGHT, fill=Y, padx=2, pady=1)

            inline_canvas.configure(yscrollcommand=scrollbar.set)
            inline_canvas.bind('<Configure>',
                               lambda e: inline_canvas.configure(scrollregion=inline_canvas.bbox("all")))
            inline_canvas.bind_all('<MouseWheel>',
                                   lambda event: inline_canvas.yview('scroll', int(-2 * (event.delta / 120)), 'units'))

        another_frame = Frame(inline_canvas,
                              bg=bg)
        inline_canvas.create_window((0, 0), window=another_frame, anchor='nw')

        def button(data, state):
            haha = tkinter.messagebox.askyesno('Error', 'Show Message Here.')
            if haha:
                db.child("Share").child(data['folderId'] + data['sharedTo']).update({'status': 1})
                SHARED_FILES(self.master, 'notes')

        if self.rows != None:
            # print(self.rows)
            for i in self.rows:
                line_frame = Canvas(another_frame,
                                    highlightthickness=0)
                line_frame.grid(row=row, column=column, pady=5, padx=11)

                folder = Button(line_frame,
                                image=folder_img,
                                command=lambda data=i, state='normal': button(data, state),
                                border=0,
                                bg=bg,
                                activebackground=bg)
                folder.pack()
                foldername = Label(line_frame,
                                   text=i['name'],
                                   font=("Bahnschrift", 10),
                                   fg=fg,
                                   borderwidth=0,
                                   relief=FLAT,
                                   width=10,
                                   background=bg,
                                   activebackground=self.bg_color,
                                   height=1)
                foldername.pack(fill=BOTH, expand=1)

                constraints = [x for x in range(6, 500, 6)]

                if column + 1 in constraints:
                    row += 1
                    column = 0
                    print("row", row)
                    print("column", column)
                else:
                    column += 1

        line_menu = Button(self.master,
                           image=menu_img,
                           command=self.side_menu,
                           border=0,
                           bg=self.bg_color,
                           activebackground=self.bg_color)
        line_menu.place(x=50, y=24)
        search_entry = Entry(self.master,
                             width=74,
                             font=("Roboto", 12, "bold"),
                             bg=self.bg_color,
                             borderwidth=0,
                             fg="#e9e9e9")
        search_entry.place(x=100, y=30)

        if self.type == 'notes':
            quiz_button = Button(self.master,
                                 text="Quizzes",
                                 fg=afg,
                                 font=("Roboto", 14, "bold"),
                                 command=lambda: SHARED_FILES(self.master, 'quiz'),
                                 bg=abg,
                                 borderwidth=0,
                                 activeforeground=afg,
                                 activebackground=abg)
            quiz_button.place(x=506, y=85)
            notes_label = Label(self.master,
                                text="Notes",
                                fg=fg,
                                font=("Roboto", 14, "bold"),
                                bg=bg,
                                borderwidth=0)
            notes_label.place(x=322, y=90)
        elif self.type == 'quiz':
            notes_button = Button(self.master,
                                  text="Notes",
                                  fg=afg,
                                  font=("Roboto", 14, "bold"),
                                  command=lambda: SHARED_FILES(self.master, 'notes'),
                                  bg=abg,
                                  borderwidth=0,
                                  activeforeground=afg,
                                  activebackground=abg)
            notes_button.place(x=315, y=85)
            quiz_label = Label(self.master,
                               text="Quizzes",
                               fg=fg,
                               font=("Roboto", 14, "bold"),
                               bg=bg,
                               borderwidth=0)
            quiz_label.place(x=512, y=91)


    def features(self):
        if self.bg_color == "#121212" and self.type == 'notes':
            self.content_features(self.search_dark, self.contentbg_dark, self.folder_dark,
                                  self.threelinemenu_dark, self.bg_color, "#A6A6A6", "#F2F2F2", "#2C2C2C",
                                  self.sidebutton_dark)
        elif self.bg_color == "#0d9187" and self.type == 'notes':
            self.content_features(self.search_light, self.contentbg_light, self.folder_light,
                                  self.threelinemenu_light, "#F2F2F2", "#0c325c", "#0c325c", "#12c8bb",
                                  self.sidebutton_light)
        elif self.bg_color == "#121212" and self.type == 'quiz':
            self.content_features(self.search_dark, self.quizbtn_dark, self.folder_dark,
                                  self.threelinemenu_dark, self.bg_color, "#A6A6A6", "#F2F2F2", "#2C2C2C",
                                  self.sidebutton_dark)
        elif self.bg_color == "#0d9187" and self.type == 'quiz':
            self.content_features(self.search_light, self.quizbtn_light, self.folder_light,
                                  self.threelinemenu_light, "#F2F2F2", "#0c325c", "#0c325c", "#12c8bb",
                                  self.sidebutton_light)


    def side_menu(self):
        THREELINE_MENU(self.master, visit='Share')

class THREELINE_MENU():
    def __init__(self, master, visit):
        self.master = master
        self.closemenu_dark = ImageTk.PhotoImage(Image.open("images/close_dark.png"))
        self.closemenu_light = ImageTk.PhotoImage(Image.open("images/close_light.png"))
        self.visit = visit
        self.burger_menu()

        print("OPENED: Three-Line Menu")

    def notes_folder(self):
        NOTES_FOLDER(self.master)
    
    def quiz_folder(self):
        QUIZ_FOLDER(self.master)
    
    def shared_files(self):
        SHARED_FILES(self.master, 'notes')
    
    def recycle_bin(self):
        RECYCLE_BIN(self.master)
    
    def profile_settings(self):
        PROFILE_SETTINGS(self.master)

    def logout(self):
        LOGOUT(self.master)

    def burger_menu(self):

        def destroy_threeline():
            threeline_menu.destroy()
            if self.visit == 'Note': self.notes_folder()
            elif self.visit == 'Quiz': self.quiz_folder()
            elif self.visit == 'Share': self.shared_files()
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

        def side_buttons(note, quiz, share, bin, profile, logout, state):
            
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
        
            Shared_files = Button(threeline_menu,
                text="     Shared Folder",
                anchor=W,font=fontstyle,
                command=self.shared_files,
                border=0,
                fg=fg_color,
                activeforeground=activefg,
                bg=share,
                activebackground=activebg,
                width=20, 
                disabledforeground=fg_color,
                state=no_state[2])
            Shared_files.place(x=0, y=171)
            
            if no_state[2] != 'disabled':
                Shared_files.bind("<Enter>", lambda _: on_entera(None, Shared_files))
                Shared_files.bind("<Leave>", lambda _: on_leavea(None, Shared_files))
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
                state=no_state[3])
            Recycle_Bin.place(x=0, y=219)

            if no_state[3] != 'disabled':
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
                state=no_state[4])
            Profile_Settings.place(x=0, y=267)
            
            if no_state[4] != 'disabled':
                Profile_Settings.bind("<Enter>", lambda _: on_entera(None, Profile_Settings))
                Profile_Settings.bind("<Leave>", lambda _: on_leavea(None, Profile_Settings))
            else: pass
        
            Logout = Button(threeline_menu,
                text="     Logout",
                anchor=W,
                font=fontstyle,
                command=self.logout,
                border=0,
                fg=fg_color,
                activeforeground=activefg,
                bg=logout,
                activebackground=activebg,
                disabledforeground=fg_color,
                width=20,
                state=no_state[5])
            Logout.place(x=0, y=315)

            if no_state[5] != 'disabled':
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
            notes_state = ['disabled', 'normal', 'normal', 'normal', 'normal', 'normal']
            side_buttons(clickedbg, bg_color, bg_color, bg_color, bg_color, bg_color, notes_state)
        elif self.visit == 'Quiz':
            quiz_state = ['normal', 'disabled', 'normal', 'normal', 'normal', 'normal']
            side_buttons(bg_color, clickedbg, bg_color, bg_color, bg_color, bg_color, quiz_state) 
        
        elif self.visit == 'Share':
            share_state = ['normal', 'normal', 'disabled', 'normal', 'normal','normal']
            side_buttons(bg_color, bg_color, clickedbg, bg_color, bg_color, bg_color, share_state)
        
        elif self.visit == 'Bin':
            bin_state = ['normal', 'normal', 'normal', 'disabled', 'normal','normal']
            side_buttons(bg_color, bg_color, bg_color, clickedbg, bg_color, bg_color, bin_state) 
        elif self.visit == 'Profile':
            profile_state = ['normal','normal','normal', 'normal', 'disabled', 'normal']
            side_buttons(bg_color, bg_color, bg_color, bg_color, clickedbg, bg_color, profile_state)
        elif self.visit == 'Logout':
            logout_state = ['normal', 'normal','normal','normal', 'normal' 'disabled']
            side_buttons(bg_color, bg_color, bg_color,bg_color, bg_color, clickedbg, logout_state)         
        else:
            general_state = ['normal', 'normal','normal','normal', 'normal', 'normal']
            side_buttons(bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, general_state) 

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

