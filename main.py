from tkinter import *
from sign_in import SignIn
from sign_up import SignUp


class Home:
    def __init__(self):
        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Registration")
        self.root.geometry("300x225+550+250")
        self.root.resizable(0, 0)

        self.h1 = Label(self.root, text="Resonotes",
                        font=('Arial', 18, 'bold'), bg="light grey")
        self.h1.place(x=87, y=30)

        self.signin_btn = Button(
            self.root, text="Sign In", command=lambda: [self.root.destroy(), SignIn().start()])
        self.signin_btn.place(x=130, y=110)

        self.signup_btn = Button(
            self.root, text="Sign Up", command=lambda: [self.root.destroy(), SignUp().start()])
        self.signup_btn.place(x=128, y=150)

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    Home().start()
