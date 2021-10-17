from tkinter import *
from db.database import *
from highlights_view import HighlightsView


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

        self.h1 = Label(self.root, text="HighlightR",
                        font=('Arial', 18, 'bold'), bg="light grey")
        self.h1.place(x=170, y=30)

        self.book_highlight = Label(
            self.root, text="Enter Highlight", bg="light grey")
        self.book_highlight.place(x=80, y=90)
        self.book_highlight_input_area = Entry(self.root, width=30)
        self.book_highlight_input_area.place(x=220, y=90)

        self.page_no = Label(
            self.root, text="Enter Page number", bg="light grey")
        self.page_no.place(x=80, y=130)
        self.page_no_input_area = Entry(self.root, width=10)
        self.page_no_input_area.place(x=220, y=130)

        self.add_hlt_btn = Button(
            self.root, text="Add Highlight").place(x=180, y=190)

        self.hlts_frame = LabelFrame(self.root, text="Highlights")
        self.hlts_list = Listbox(self.hlts_frame, width=70, height=12)
        self.scrollbar = Scrollbar(self.hlts_frame)
        self.hlts_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.hlts_list.yview)
        self.hlts_frame.place(x=10, y=230)
        self.hlts_list.grid(row=1, column=1)
        self.scrollbar.grid(row=1, column=2, sticky=NS)

        self.fetchHighlights()

        self.button_frame = Frame(self.root)
        self.button_frame.config(bg="light grey")
        self.button_frame.place(x=170, y=470)

        self.view_hlt_btn = Button(self.button_frame, text='View', padx=10,
                                   command=lambda: self.highlightPopup(self.hlts_list.curselection()))
        self.view_hlt_btn.grid(row=1, column=1)

        Label(self.button_frame, text="    ",
              bg="light grey").grid(row=1, column=2)

        self.del_hlt_btn = Button(self.button_frame, text="Delete", padx=10)
        self.del_hlt_btn.grid(row=1, column=3)

    def fetchHighlights(self):
        self.hlts_list.delete(0, END)
        for index, highlight in enumerate(self.highlights):
            hlt = highlight[1]

            if len(hlt) > 30:
                hlt = hlt[:30] + '...'

            self.hlts_list.insert(
                END, str(index + 1) + '. ' + hlt + ' @ pg. ' + str(highlight[2]))

    def highlightPopup(self, selected):
        if selected:
            HighlightsView(self.highlights[selected[0]]).start()

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    Highlights(2).start()
