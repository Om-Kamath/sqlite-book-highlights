from tkinter import *
from properties import BUTTON_FONT, HEADER
from sign_in import SignIn
from sign_up import SignUp


class Home:
    def __init__(self):
        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Resonotes")
        self.root.geometry("300x225+550+250")
        self.root.resizable(0, 0)
        self.root.iconphoto(False, PhotoImage(file='icons/logo.png'))

        self.h1 = Label(self.root, text="RESONOTES",
                        font=HEADER, bg="light grey")
        self.h1.place(x=70, y=30)

        self.signin_btn = Button(
            self.root, text="Sign In", font=BUTTON_FONT, padx=8,
            command=lambda: [self.root.destroy(), SignIn().start()])
        self.signin_btn.place(x=120, y=110)

        self.signup_btn = Button(
            self.root, text="Sign Up", font=BUTTON_FONT, padx=5,
            command=lambda: [self.root.destroy(), SignUp().start()])
        self.signup_btn.place(x=120, y=150)

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    Home().start()
