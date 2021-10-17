from tkinter import *
from tkinter import font
from db.database import BookHighlightsDB
from books import *
import sign_up


class SignIn:
    def __init__(self):
        self.db = BookHighlightsDB()

        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Sign In")
        self.root.geometry("340x340+550+200")
        self.root.resizable(0, 0)
        self.root.after(1, lambda: self.root.focus_force())

        self.h1 = Label(self.root, text="HighlightR",
                        font=('Arial', 18, 'bold'), bg="light grey")
        self.h1.place(x=110, y=30)

        self.email = Label(self.root, text="Enter Email", bg="light grey")
        self.email.place(x=20, y=100)

        self.email_input_area = Entry(self.root, width=30)
        self.email_input_area.place(x=130, y=100)
        # auto-focus the email input
        self.email_input_area.focus()

        self.user_pass = Label(
            self.root, text="Enter Password", bg="light grey")
        self.user_pass.place(x=20, y=140)
        self.user_pass_input_area = Entry(self.root, width=30, show='*')
        self.user_pass_input_area.place(x=130, y=140)

        self.error_label = Label(self.root, font=("Arial", 10), fg="red", bg="light grey")
        self.error_label.place(y=175)

        self.signin_btn = Button(
            self.root, text="Sign In", command=self.signInSubmit)
        self.signin_btn.place(x=145, y=240)

        self.sign_up_instead = Label(self.root, text="Looking to sign up?", fg="blue",
                                     bg="light grey", cursor="hand2", font=("Arial", 9, "underline"))
        self.sign_up_instead.place(x=113, y=280)
        self.sign_up_instead.bind("<Button-1>", lambda e: self.signUpInstead())
    
    def signUpInstead(self):
        self.root.destroy()
        sign_up.SignUp().start()

    def signInSubmit(self):
        email = self.email_input_area.get()
        password = self.user_pass_input_area.get()
        expected_password = self.db.getPassword(email)

        # TODO: handle state
        if expected_password is None:
            self.error_label.config(text="Could not find user!")
            self.error_label.place(x=110)
        else:
            if expected_password == password:
                email = self.email_input_area.get()
                self.root.destroy()
                Books(email).start()
            else:
                self.error_label.config(text="Incorrect Password!")
                self.error_label.place(x=115)

    def start(self):
        self.root.mainloop()

if __name__ == '__main__':
    SignIn().start()
