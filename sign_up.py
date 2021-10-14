from tkinter import *
from validate import validateEmail, validatePassword, validateName
from db.database import BookHighlightsDB

class SignUp:
    def __init__(self):
        self.db = BookHighlightsDB()

        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Sign Up")
        self.root.geometry("390x300")
        self.root.resizable(0, 0)

        self.name = Label(self.root, text = "Enter Name").place(x = 20, y = 60)
        self.name_input_area = Entry(self.root, width = 30)
        self.name_input_area.place(x = 180,y = 60)

        self.email = Label(self.root, text = "Enter Email").place(x = 20, y = 100)
        self.email_input_area = Entry(self.root, width = 30)
        self.email_input_area.place(x = 180,y = 100)

        self.user_pass = Label(self.root, text = "Enter Password").place(x = 20, y = 140)
        self.user_pass_input_area = Entry(self.root, width = 30, show='*')
        self.user_pass_input_area.place(x = 180,y = 140)

        self.user_repass = Label(self.root, text = "Re-Enter Password").place(x = 20, y = 180)
        self.user_repass_input_area = Entry(self.root, width = 30, show='*')
        self.user_repass_input_area.place(x = 180,y = 180)

        self.signin_btn= Button(self.root, text="Sign Up", command=self.sign_up_submit)
        self.signin_btn.place(x=180,y=220)
    

    def sign_up_submit(self):
        name = self.name_input_area.get()
        email = self.email_input_area.get()
        password = self.user_pass_input_area.get()
        re_password = self.user_repass_input_area.get()

        if not validateName(name):
            print('Bad name')
        elif not validateEmail(email):
            print('Bad email')
        elif not validatePassword(password):
            print('Bad password')
        elif password != re_password:
            print('Passwords don\'t match')
        else:
            self.db.addUser(name, email, password)

    
    def start(self):
        self.root.mainloop()
