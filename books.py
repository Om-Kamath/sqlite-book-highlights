from tkinter import *
from db.database import *


class Books:
    def __init__(self, email):
        self.db = BookHighlightsDB()

        self.user_email = email
        self.user_id = self.db.getUserID(self.user_email)

        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Books")
        self.root.geometry("470x600+550+100")
        self.root.resizable(0, 0)
        self.root.after(1, lambda: self.root.focus_force())

        self.h1 = Label(self.root, text="HighlightR",
                        font=('Arial', 18, 'bold'), bg="light grey")
        self.h1.place(x=170, y=30)

        self.book_title = Label(
            self.root, text="Enter Book Title", bg="light grey")
        self.book_title.place(x=65, y=90)
        self.book_title_input_area = Entry(self.root, width=30)
        self.book_title_input_area.place(x=225, y=90)
        self.book_title_input_area.focus()

        self.author_name = Label(
            self.root, text="Enter author name", bg="light grey")
        self.author_name.place(x=65, y=130)
        self.author_name_input_area = Entry(self.root, width=30)
        self.author_name_input_area.place(x=225, y=130)

        self.add_book_btn = Button(
            self.root, text="Add Book", command=self.add_book)
        self.add_book_btn.place(x=200, y=190)

        self.books_frame = LabelFrame(self.root, text="Books")
        self.books_list = Listbox(self.books_frame, width=70, height=12)
        self.scrollbar = Scrollbar(self.books_frame)
        self.books_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.books_list.yview)
        self.books_frame.place(x=10, y=230)
        self.books_list.grid(row=1, column=1)
        self.scrollbar.grid(row=1, column=2, sticky=NS)

        self.fetch_books()

        self.see_hlt_btn = Button(self.root, text="See Highlights")
        self.see_hlt_btn.place(x=180, y=510)

        self.del_book_btn = Button(self.root, text="Delete Book")
        self.del_book_btn.place(x=187, y=550)

    def fetch_books(self):
        self.books_list.delete(0, END)
        self.books = self.db.getBooks(self.user_id)
        for index, book in enumerate(self.books):
            self.books_list.insert(END, str(index + 1) + ". " + book[0] + " - " + book[1])
    
    # The 'T' in Tkinter stands for Trash

    def add_book(self):
        author = self.author_name_input_area.get()
        title = self.book_title_input_area.get()
        self.db.addBook(title, author, self.user_id)
        self.book_title_input_area.delete(0, END)
        self.author_name_input_area.delete(0, END)
        self.fetch_books()

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    Books('javeri.rushabh45@gmail.com').start()
