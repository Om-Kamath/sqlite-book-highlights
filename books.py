from tkinter import *
from db.database import *
from highlights import Highlights
from properties import BACKGROUND_COLOR, BUTTON_COLOR, BUTTON_FONT, ERROR_FONT, HEADER, LABEL_FONT, LISTBOX_FONT, UNDERLINE_COLOR
from validate import validateAuthorName, validateBookTitle
import main


class Books:
    def __init__(self, email):
        self.db = BookHighlightsDB()

        self.user_email = email
        self.user_name = self.db.getUserName(self.user_email)
        self.user_id = self.db.getUserID(self.user_email)

        self.root = Tk()
        self.root.title("Resonotes - Books")
        self.root.geometry("484x650+550+100")
        self.root.resizable(0, 0)
        self.root.after(1, lambda: self.root.focus_force())
        self.root.iconphoto(False, PhotoImage(file='icons/logo.png'))
        self.root.config(bg=BACKGROUND_COLOR)

        Frame(self.root, bg="white", width=433, height=580).place(x=25, y=25)

        self.header_frame = Frame(self.root, bg="white", width=433, height=50)
        self.header_frame.place(x=25, y=25)

        self.h1 = Label(self.header_frame, text=f"{self.user_name}'s RESONOTES",
                        font=HEADER, bg="white")
        self.h1.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.book_title = Label(
            self.root, text="Enter Book Title", bg="white", font=LABEL_FONT)
        self.book_title.place(x=65, y=95)
        self.book_title_input_area = Entry(
            self.root, width=26, borderwidth=5, font=LABEL_FONT, relief=FLAT)
        self.book_title_input_area.place(x=225, y=90)
        self.book_title_input_area.focus()

        self.author_name = Label(
            self.root, text="Enter author name", bg="white", font=LABEL_FONT)
        self.author_name.place(x=65, y=135)
        self.author_name_input_area = Entry(
            self.root, width=26, borderwidth=5, font=LABEL_FONT, relief=FLAT)
        self.author_name_input_area.place(x=225, y=130)

        self.error_label = Label(
            self.root, font=ERROR_FONT, fg="red", bg="white")
        self.error_label.place(x=-20, y=170)

        self.add_book_btn = Button(
            self.root, text="Add Book", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white",  relief=FLAT, padx=12, command=self.addBook)
        self.add_book_btn.place(x=200, y=200)
        self.root.bind('<Return>', self.callback)

        self.books_frame = LabelFrame(
            self.root, text="Books", bg="white", relief=FLAT, font=LABEL_FONT)
        self.books_list = Listbox(
            self.books_frame, width=50, height=12, font=LISTBOX_FONT, borderwidth=5, relief=FLAT)
        self.scrollbar = Scrollbar(self.books_frame, bg="white", relief=FLAT)
        self.books_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.books_list.yview)
        self.books_frame.place(x=25, y=250)
        self.books_list.grid(row=1, column=1)
        self.scrollbar.grid(row=1, column=2, sticky=NS)
        Frame(self.root, width=215, height=2,
              bg=UNDERLINE_COLOR).place(x=225, y=115)
        Frame(self.root, width=215, height=2,
              bg=UNDERLINE_COLOR).place(x=225, y=155)

        self.fetchBooks()

        self.see_hlt_btn = Button(self.root, font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white",  relief=FLAT, padx=12, text="See Highlights",
                                  command=lambda: self.seeHighlights(self.books_list.curselection()))
        self.see_hlt_btn.place(x=180, y=500)

        self.del_book_btn = Button(self.root, text="Delete Book", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white",  relief=FLAT, padx=22, command=lambda: self.deleteSelectedBook(
            self.books_list.curselection()))
        self.del_book_btn.place(x=180, y=550)

        self.menu_bar = Menu(self.root)
        self.option_list = Menu(self.menu_bar, tearoff=0)
        self.option_list.add_command(label="Log Out", command=self.logout)
        self.option_list.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(
            label="Options", menu=self.option_list, font=LABEL_FONT)
        self.root.config(menu=self.menu_bar)

    def logout(self):
        self.root.destroy()
        main.Home().start()

    def seeHighlights(self, selected):
        if selected:
            # Starting Highlights window and passing it book ID
            Highlights(self.books[selected[0]][0]).start()

    def fetchBooks(self):
        self.books_list.delete(0, END)
        self.books = self.db.getBooks(self.user_id)
        for index, book in enumerate(self.books):
            self.books_list.insert(
                END, str(index + 1) + ". " + book[1] + " - " + book[2])

    def addBook(self):
        author = self.author_name_input_area.get().strip().title()
        title = self.book_title_input_area.get().strip()

        if author == '':
            author = 'Anonymous'

        if not validateBookTitle(title):
            self.error_label.config(text="Invalid Title!")
            self.error_label.place(x=215)
        elif not validateAuthorName(author):
            self.error_label.config(text="Invalid author name!")
            self.error_label.place(x=190)
        else:
            self.error_label.config(text="")
            self.db.addBook(title, author, self.user_id)
            self.book_title_input_area.delete(0, END)
            self.author_name_input_area.delete(0, END)
            self.fetchBooks()
            self.book_title_input_area.focus()

    def callback(self, event):
        self.addBook()

    def start(self):
        self.root.mainloop()

    def deleteSelectedBook(self, selected):
        if selected:
            self.db.deleteBook(self.books[selected[0]][0])
            self.fetchBooks()
