from tkinter import *
from properties import HEADER, MAIN_BUTTON_FONT, BACKGROUND_COLOR, BUTTON_COLOR
import sign_in 
import sign_up


class Home:
    def __init__(self):
        self.root = Tk()
        self.root.title("Resonotes")
        self.root.geometry("300x300+550+250")
        self.root.resizable(0, 0)
        self.root.config(bg=BACKGROUND_COLOR)
        self.root.iconphoto(False, PhotoImage(file='icons/logo.png'))

        Frame(self.root, width=250, height=250, bg="white").place(x=25, y=25)
        self.h1 = Label(self.root, text="RESONOTES",
                        font=HEADER, bg='white')
        self.h1.place(x=70, y=30)

        self.signin_btn = Button(
            self.root, text="Sign In", font=MAIN_BUTTON_FONT, bg=BUTTON_COLOR, fg="white", relief=FLAT, padx=12,
            command=lambda: [self.root.destroy(), sign_in.SignIn().start()])
        self.signin_btn.place(x=100, y=110)

        self.signup_btn = Button(
            self.root, text="Sign Up", font=MAIN_BUTTON_FONT, padx=10, bg=BUTTON_COLOR, fg="white", relief=FLAT,
            command=lambda: [self.root.destroy(), sign_up.SignUp().start()])
        self.signup_btn.place(x=100, y=170)

    def start(self):
        self.root.mainloop()

if __name__ == '__main__':
    Home().start()
