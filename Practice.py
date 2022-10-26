from tkinter import *
from tkinter import messagebox
# import pyrebase


class Fullscreen_Window:

    def __init__(self, main):
        self.tk = main
        self.tk.attributes('-fullscreen', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<Escape>", self.end_fullscreen)
        signin = FirstWindow(self.tk).signin_menu()

    def end_fullscreen(self, event=None):
        result = messagebox.askquestion("Notice!", "Are you sure you want to exit?")
        if result == 'yes': self.tk.destroy()
        else: pass

class FirstWindow:
    def __init__(self, main):
        self.main = main

    def login_menu(self):
        self.template = Frame(main,
            width=1000,
            height=1000)
        self.template.place(x=800, y=300)
        self.frame = Frame(self.main,width=1080, height=1800)
        self.frame.pack()
        email = Label(main, text="Email").place(x=850, y=450)
        user_password = Label(main,text = "Password").place(x = 850,y = 500)

        submit_button = Button(main,text = "Submit").place(x = 850,y = 550)
        create_acc = Button(main, text="Do not have an account? Signup", command=self.signin_menu).place(x=850, y=600)

        user_email = Entry(main, width=30).place(x=960, y=450)
        user_password_entry_area = Entry(main,width = 30).place(x = 960,y = 500)
    
    def signin_menu(self):
        self.template = Frame(main,
            width=1000,
            height=1000)
        self.template.place(x=800, y=300)
        user_name = Label(main,text = "Username").place(x = 850, y = 400) 
        email = Label(main, text="Email").place(x=850, y=450)
        user_password = Label(main,text = "Password").place(x = 850,y = 500)
        confirm_pass = Label(main, text="Confirm Password").place(x=850, y=550)
        
        submit_button = Button(main,text = "Submit").place(x = 850,y = 600)
        already_login = Button(main,text="Already have an account? Login", command=self.login_menu).place(x=850, y=650)
        user_name_input_area = Entry(main,width = 30).place(x = 960, y = 400)
        user_email = Entry(main, width=30).place(x=960, y=450)
        user_password_entry_area = Entry(main,width = 30).place(x = 960,y = 500) 
        confirm_user_pass = Entry(main, width=30).place(x=960, y=550)



if __name__ == '__main__':
    main = Tk()
    w = Fullscreen_Window(main)
    main.mainloop()