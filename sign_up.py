from tkinter import *
from tkinter import font
from properties import BUTTON_FONT, ERROR_FONT, HEADER, LABEL_FONT, LINK_FONT
from validate import validateName, validateEmail, validatePassword
from db.database import BookHighlightsDB
import sign_in
from books import Books


class SignUp:
    def __init__(self):
        self.db = BookHighlightsDB()

        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Resonotes - Sign Up")
        self.root.geometry("380x400+550+200")
        self.root.resizable(0, 0)
        self.root.after(1, lambda: self.root.focus_force())
        self.root.iconphoto(False, PhotoImage(file='icons/logo.png'))

        self.h1 = Label(self.root, text="RESONOTES",
                        font=HEADER, bg="light grey")
        self.h1.place(x=100, y=30)

        self.name = Label(self.root, text="Enter Name", bg="light grey",font=LABEL_FONT)
        self.name.place(x=20, y=105)
        self.name_input_area = Entry(self.root, width=23, borderwidth=5,relief=FLAT,font=LABEL_FONT)
        self.name_input_area.place(x=160, y=100)
        self.name_input_area.focus()

        self.email = Label(self.root, text="Enter Email", bg="light grey",font = LABEL_FONT)
        self.email.place(x=20, y=145)
        self.email_input_area = Entry(self.root, width=23, borderwidth=5,relief=FLAT,font = LABEL_FONT)
        self.email_input_area.place(x=160, y=140)

        self.user_pass = Label(
            self.root, text="Enter Password", bg="light grey",font=LABEL_FONT)
        self.user_pass.place(x=20, y=185)
        self.user_pass_input_area = Entry(self.root, width=23, borderwidth=5,relief=FLAT, show='*',font=LABEL_FONT)
        self.user_pass_input_area.place(x=160, y=180)

        self.user_repass = Label(
            self.root, text="Re-Enter Password", bg="light grey",font=LABEL_FONT)
        self.user_repass.place(x=20, y=225)
        self.user_repass_input_area = Entry(self.root, width=23, show='*', borderwidth=5,relief=FLAT,font=LABEL_FONT)
        self.user_repass_input_area.place(x=160, y=220)

        self.error_label = Label(self.root, text="", font=ERROR_FONT, fg="red", bg="light grey", wraplength=300)
        self.error_label.place(y=260)

        self.signin_btn = Button(
            self.root, text="Sign Up",font= BUTTON_FONT, padx= 8, command=self.signUpSubmit)
        self.signin_btn.place(x=145, y=320)

        self.sign_in_instead = Label(self.root, text="Looking to sign in?", fg="blue",
                                     bg="light grey", cursor="hand2", font=LINK_FONT)
        self.sign_in_instead.place(x=125, y=360)
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
            self.error_label.place(x=40)
        elif not validateEmail(email):
            self.error_label.config(text="Invalid email!")
            self.error_label.place(x=140)
        elif not validatePassword(password):
            self.error_label.config(text="Weak password!")
            self.error_label.place(x=130)
        elif password != re_password:
            self.error_label.config(text="Passwords don't match")
            self.error_label.place(x=105)
        else:
            self.db.addUser(name, email, password)
            email = self.email_input_area.get()
            self.root.destroy()
            Books(email).start()

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    SignUp().start()
