from tkinter import *
from tkinter import font
from properties import BACKGROUND_COLOR, BUTTON_COLOR, BUTTON_FONT, ERROR_FONT, HEADER, LABEL_FONT, LINK_FONT, UNDERLINE_COLOR
from validate import validateFirstName, validateEmail, validatePassword
from db.database import BookHighlightsDB
import sign_in
import books


class SignUp:
    def __init__(self):
        self.db = BookHighlightsDB()

        self.root = Tk()

        self.root.title("Resonotes - Sign Up")
        self.root.geometry("380x410+550+200")
        self.root.resizable(0, 0)
        self.root.after(1, lambda: self.root.focus_force())
        self.root.iconphoto(False, PhotoImage(file='icons/logo.png'))
        self.root.config(bg=BACKGROUND_COLOR)

        self.white_frame = Frame(
            self.root, bg="white", width=330, height=360).place(x=25, y=25)

        self.h1 = Label(self.root, text="RESONOTES",
                        font=HEADER, bg="white")
        self.h1.place(x=100, y=30)

        self.name = Label(self.root, text="Enter First Name",
                          bg="white", font=LABEL_FONT)
        self.name.place(x=30, y=105)
        self.name_input_area = Entry(
            self.root, width=21, borderwidth=5, font=LABEL_FONT, relief=FLAT)
        self.name_input_area.place(x=170, y=100)
        self.name_input_area.focus()

        self.email = Label(self.root, text="Enter Email",
                           bg="white", font=LABEL_FONT)
        self.email.place(x=30, y=145)
        self.email_input_area = Entry(
            self.root, width=21, borderwidth=5, font=LABEL_FONT, relief=FLAT)
        self.email_input_area.place(x=170, y=140)

        self.user_pass = Label(
            self.root, text="Enter Password", bg="white", font=LABEL_FONT)
        self.user_pass.place(x=30, y=185)
        self.user_pass_input_area = Entry(
            self.root, width=21, borderwidth=5, show="\u25CF", font=LABEL_FONT, relief=FLAT)
        self.user_pass_input_area.place(x=170, y=180)

        self.user_repass = Label(
            self.root, text="Re-Enter Password", bg="white", font=LABEL_FONT)
        self.user_repass.place(x=30, y=225)
        self.user_repass_input_area = Entry(
            self.root, width=21, show="\u25CF", borderwidth=5, font=LABEL_FONT, relief=FLAT)
        self.user_repass_input_area.place(x=170, y=220)

        self.error_label = Label(
            self.root, text="", font=ERROR_FONT, fg="red", bg="white", wraplength=300)
        self.error_label.place(x=100, y=260)

        self.signin_btn = Button(
            self.root, text="Sign Up", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white",  relief=FLAT, padx=12, command=self.signUpSubmit)
        self.signin_btn.place(x=130, y=310)

        self.sign_in_instead = Label(self.root, text="Looking to sign in?", fg="blue",
                                     bg="white", cursor="hand2", font=LINK_FONT)

        self.root.bind('<Return>',self.callback)

        Frame(self.root, width=170, height=2,
              bg=UNDERLINE_COLOR).place(x=175, y=125)
        Frame(self.root, width=170, height=2,
              bg=UNDERLINE_COLOR).place(x=175, y=165)
        Frame(self.root, width=170, height=2,
              bg=UNDERLINE_COLOR).place(x=175, y=205)
        Frame(self.root, width=170, height=2,
              bg=UNDERLINE_COLOR).place(x=175, y=245)

        self.sign_in_instead.place(x=125, y=360)
        self.sign_in_instead.bind("<Button-1>", lambda e: self.signInInstead())

    def signInInstead(self):
        self.root.destroy()
        sign_in.SignIn().start()

    def callback(self,event):
            self.signUpSubmit()

    def signUpSubmit(self):
        name = self.name_input_area.get().strip()
        email = self.email_input_area.get().strip()
        password = self.user_pass_input_area.get().strip()
        re_password = self.user_repass_input_area.get().strip()

        if self.db.userExists(email):
            self.error_label.config(
                text="An account with this email already exists!")
            self.error_label.place(x=58)
        elif not validateFirstName(name):
            self.error_label.config(
                text="Name must be min. 2 characters long and must contain alphabets only")
            self.error_label.place(x=42)
        elif not validateEmail(email):
            self.error_label.config(text="Invalid email!")
            self.error_label.place(x=140)
        elif not validatePassword(password):
            self.error_label.config(text="Weak password!")
            self.error_label.place(x=130)
        elif password != re_password:
            self.error_label.config(text="Passwords don't match!")
            self.error_label.place(x=106)
        else:
            self.db.addUser(name, email, password)
            email = self.email_input_area.get()
            self.root.destroy()
            books.Books(email).start()

    def start(self):
        self.root.mainloop()
