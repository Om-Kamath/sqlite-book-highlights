from tkinter import *
from validate import validateName, validateEmail, validatePassword
from db.database import BookHighlightsDB
import sign_in
from books import Books


class SignUp:
    def __init__(self):
        self.db = BookHighlightsDB()

        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Sign Up")
        self.root.geometry("370x400+550+200")
        self.root.resizable(0, 0)
        self.root.after(1, lambda: self.root.focus_force())

        self.h1 = Label(self.root, text="Resonotes",
                        font=('Arial', 18, 'bold'), bg="light grey")
        self.h1.place(x=110, y=30)

        self.name = Label(self.root, text="Enter Name", bg="light grey")
        self.name.place(x=20, y=100)
        self.name_input_area = Entry(self.root, width=30)
        self.name_input_area.place(x=160, y=100)
        self.name_input_area.focus()

        self.email = Label(self.root, text="Enter Email", bg="light grey")
        self.email.place(x=20, y=140)
        self.email_input_area = Entry(self.root, width=30)
        self.email_input_area.place(x=160, y=140)

        self.user_pass = Label(
            self.root, text="Enter Password", bg="light grey")
        self.user_pass.place(x=20, y=180)
        self.user_pass_input_area = Entry(self.root, width=30, show='*')
        self.user_pass_input_area.place(x=160, y=180)

        self.user_repass = Label(
            self.root, text="Re-Enter Password", bg="light grey")
        self.user_repass.place(x=20, y=220)
        self.user_repass_input_area = Entry(self.root, width=30, show='*')
        self.user_repass_input_area.place(x=160, y=220)

        self.error_label = Label(self.root, text="", font=(
            "Arial", 10), fg="red", bg="light grey", wraplength=300)
        self.error_label.place(y=250)

        self.signin_btn = Button(
            self.root, text="Sign Up", command=self.signUpSubmit)
        self.signin_btn.place(x=150, y=320)

        self.sign_in_instead = Label(self.root, text="Looking to sign in?", fg="blue",
                                     bg="light grey", cursor="hand2", font=("Arial", 9, "underline"))
        self.sign_in_instead.place(x=120, y=360)
        self.sign_in_instead.bind("<Button-1>", lambda e: self.signInInstead())

    def signInInstead(self):
        self.root.destroy()
        sign_in.SignIn().start()

    def signUpSubmit(self):
        name = self.name_input_area.get().strip()
        email = self.email_input_area.get().strip()
        password = self.user_pass_input_area.get().strip()
        re_password = self.user_repass_input_area.get().strip()

        # TODO: handle state
        if not validateName(name):
            self.error_label.config(
                text="Name must be min. 2 characters long and must contain alphabets only")
            self.error_label.place(x=35)
        elif not validateEmail(email):
            self.error_label.config(text="Invalid email!")
            self.error_label.place(x=135)
        elif not validatePassword(password):
            self.error_label.config(text="Weak password!")
            self.error_label.place(x=125)
        elif password != re_password:
            self.error_label.config(text="Passwords don't match")
            self.error_label.place(x=100)
        else:
            self.db.addUser(name, email, password)
            email = self.email_input_area.get()
            self.root.destroy()
            Books(email).start()

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    SignUp().start()
