from tkinter import *

class SignIn:
    
    def __init__(self):
        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Sign In")
        self.root.geometry("500x300")
        self.user_name = Label(self.root, text = "Enter Name").place(x = 20, y = 60)
        self.user_name_input_area = Entry(self.root, width = 30).place(x = 180,y = 60)

        self.email = Label(self.root, text = "Enter Email").place(x = 20, y = 100)
        self.email_input_area = Entry(self.root, width = 30).place(x = 180,y = 100)

        self.user_pass = Label(self.root, text = "Enter Password").place(x = 20, y = 140)
        self.user_pass_input_area = Entry(self.root, width = 30, show='*').place(x = 180,y = 140)

        self.signin_btn= Button(self.root, text="Sign In").place(x=180,y=180)
    
    def start(self):
        self.root.mainloop()

