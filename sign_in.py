from tkinter import *
from tkinter import font
from db.database import BookHighlightsDB
from books import *
import sign_up
from properties import BUTTON_FONT, ERROR_FONT, HEADER, LABEL_FONT, LINK_FONT


class SignIn:
    def __init__(self):
        self.db = BookHighlightsDB()

        self.root = Tk()
       
        self.root.title("Resonotes - Sign In")
        self.root.geometry("340x340+550+200")
        self.root.resizable(0, 0)
        self.root.after(1, lambda: self.root.focus_force())
        self.root.iconphoto(False, PhotoImage(file='icons/logo.png'))
        self.root.config(bg="#EFC888")

        self.white_frame = Frame(self.root,bg="white",width=290,height=290).place(x=25,y=25)
        self.h1 = Label(self.root, text="RESONOTES",
                        font=HEADER, bg="white")
        self.h1.place(x=100, y=30)

        self.email = Label(self.root, text="Enter Email", font=LABEL_FONT, bg="white")
        self.email.place(x=27, y=105)

        self.email_input_area = Entry(self.root, width=20, borderwidth=5, font=LABEL_FONT,relief=FLAT)
        self.email_input_area.place(x=140, y=100)
        # auto-focus the email input
        self.email_input_area.focus()

        self.user_pass = Label(
            self.root, text="Enter Password", font=LABEL_FONT, bg="white")
        self.user_pass.place(x=27, y=145)
        self.user_pass_input_area = Entry(self.root, width=20, borderwidth=5, font=LABEL_FONT,relief=FLAT,show="\u25CF")
        self.user_pass_input_area.place(x=140, y=140)

        self.error_label = Label(self.root, font= ERROR_FONT, fg="red", bg="white")
        self.error_label.place(x = 100,y=185)

        self.signin_btn = Button(
            self.root, text="Sign In",font=BUTTON_FONT,bg="#CF5C36",fg="white", relief=FLAT, padx=12,command=self.signInSubmit)
        self.signin_btn.place(x=120, y=230)

        self.sign_up_instead = Label(self.root, text="Looking to sign up?", fg="blue",
                                     bg="white", cursor="hand2", font=LINK_FONT)
        self.sign_up_instead.place(x=113, y=280)
        self.sign_up_instead.bind("<Button-1>", lambda e: self.signUpInstead())

                
        Frame(self.root,width=165,height=2,bg='#141414').place(x=140,y=125)
        Frame(self.root,width=165,height=2,bg='#141414').place(x=140,y=165)

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
