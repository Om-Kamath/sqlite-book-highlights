from tkinter import *
from db.database import BookHighlightsDB
from books import *
from tkinter import messagebox

class SignIn:
    
    def __init__(self):
        self.db = BookHighlightsDB()

        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Sign In")
        self.root.geometry("500x300")

        self.email = Label(self.root, text = "Enter Email")
        self.email.place(x = 20, y = 100)
        self.email_input_area = Entry(self.root, width = 30)
        self.email_input_area.place(x = 180,y = 100)

        self.user_pass = Label(self.root, text = "Enter Password").place(x = 20, y = 140)
        self.user_pass_input_area = Entry(self.root, width = 30, show='*')
        self.user_pass_input_area.place(x = 180, y = 140)

        self.signin_btn= Button(self.root, text="Sign In", command=self.sign_in_submit)
        self.signin_btn.place(x=180,y=180)
    

    def sign_in_submit(self):
        email = self.email_input_area.get()
        password = self.user_pass_input_area.get()
        expected_password = self.db.getPassword(email)

        if expected_password is None:
            print('Could not find user')
        else:
            if expected_password == password:
                email = self.email_input_area.get()
                self.root.destroy()
                Books(email).start()
                
            else:
                print('Failure')

    
    def start(self):
        self.root.mainloop()

