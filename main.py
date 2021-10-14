from tkinter import *
from sign_in import SignIn
from sign_up import SignUp

def signin():
    signin = SignIn()
    signin.start()

def signup():
    signup = SignUp()
    signup.start()


class Home:
    def __init__(self):
        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Registration")
        self.root.geometry("400x200")
        self.signin_btn= Button(self.root, text="Sign In", command=signin).place(x=140,y=60)
        self.signup_button= Button(self.root, text="Sign Up", command=signup).place(x=140,y=100)

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    Home().start()
