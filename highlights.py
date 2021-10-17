from tkinter import *
from db.database import *


class Highlights:
    def __init__(self, book):
        self.db = BookHighlightsDB()

        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Highlights")
        self.root.geometry("470x520")
        self.root.resizable(0, 0)

        self.book = book
        self.highlights = self.db.getHighlights(book)

        self.book_highlight = Label(self.root, text="Enter Highlight")
        self.book_highlight.place(x=20, y=40)
        self.book_highlight_input_area = Entry(self.root, width=30)
        self.book_highlight_input_area.place(x=180, y=40)

        self.page_no = Label(self.root, text="Enter Page number")
        self.page_no.place(x=20, y=80)
        self.page_no_input_area = Entry(self.root, width=10)
        self.page_no_input_area.place(x=180, y=80)

        self.add_hlt_btn = Button(
            self.root, text="Add Highlight").place(x=180, y=120)

        self.hlts_frame = LabelFrame(self.root, text="Highlights")
        self.hlts_list = Listbox(self.hlts_frame, width=70, height=12)
        self.scrollbar = Scrollbar(self.hlts_frame)
        self.hlts_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.hlts_list.yview)
        self.hlts_frame.place(x=10, y=160)
        self.hlts_list.grid(row=1, column=1)
        self.scrollbar.grid(row=1, column=2, sticky=NS)

        self.del_hlt_btn = Button(self.root, text="Delete Highlight")
        self.del_hlt_btn.place(x=180, y=440)

    def start(self):
        print(self.book)
        print(self.highlights)
        self.root.mainloop()


if __name__ == '__main__':
    Highlights(2).start()
