from tkinter import *

class Books:
    
    def __init__(self):
        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Books")
        self.root.geometry("470x520")

        self.book_title = Label(self.root, text = "Enter Book Title")
        self.book_title.place(x = 20, y = 40)
        self.book_title_input_area = Entry(self.root, width = 30)
        self.book_title_input_area.place(x = 180,y = 40)

        self.author_name = Label(self.root, text = "Enter author name")
        self.author_name.place(x = 20, y = 80)
        self.author_name_input_area = Entry(self.root, width = 30)
        self.author_name_input_area.place(x = 180,y = 80)

        self.add_book_btn = Button(self.root, text="Add Book").place(x=200,y=120)

        self.books_frame = LabelFrame(self.root, text="Books")
        self.books_list = Listbox(self.books_frame, width=70, height=12)
        self.scrollbar = Scrollbar(self.books_frame)
        self.books_list.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.books_list.yview)
        self.books_frame.place(x=10, y=160)
        self.books_list.grid(row=5,column=3, columnspan=4)
        self.scrollbar.grid(sticky=W)

        self.add_hlt_btn = Button(self.root, text="Add Highlights").place(x=180,y=440)
        self.del_book_btn = Button(self.root, text="Delete Book").place(x=185,y=480)
    
    def start(self):
        self.root.mainloop()

    def fetch_books(self):
        pass


