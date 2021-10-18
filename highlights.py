from enum import Flag
from tkinter import *
from tkinter import font
from db.database import *
from highlights_view import HighlightsView
from properties import BUTTON_FONT, ERROR_FONT, HEADER, LABEL_FONT, LISTBOX_FONT


class Highlights:
    def __init__(self, book):
        self.db = BookHighlightsDB()

        self.root = Tk()
        self.root.configure(background="light grey")
        self.root.title("Resonotes - Highlights")
        self.root.geometry("470x570+570+200")
        self.root.resizable(0, 0)
        self.root.after(1, lambda: self.root.focus_force())
        # self.root.iconphoto(False, PhotoImage(file='icons/logo.png'))

        self.book = book
        self.highlights = self.db.getHighlights(book)

        self.h1 = Label(self.root, text="RESONOTES",
                        font=HEADER, bg="light grey")
        self.h1.place(x=160, y=30)

        self.book_highlight = Label(
            self.root, text="Enter Highlight", bg="light grey", font=LABEL_FONT)
        self.book_highlight.place(x=70, y=90)
        self.book_highlight_input_area = Text(self.root, width=25, height=4, pady=5,padx=5,relief=FLAT,wrap=WORD ,font=LABEL_FONT)
        self.book_highlight_input_area.place(x=210, y=90)

        self.page_no = Label(
            self.root, text="Enter Page number", bg="light grey", font=LABEL_FONT)
        self.page_no.place(x=70, y=180)
        self.page_no_input_area = Entry(self.root, width=10, borderwidth=5,relief=FLAT, font=LABEL_FONT)
        self.page_no_input_area.place(x=210, y=180)

        self.error_label = Label(self.root, font=ERROR_FONT, fg="red", bg="light grey")
        self.error_label.place(y=210)

        self.add_hlt_btn = Button(
            self.root, text="Add Highlight",padx=8, command=self.addHighlight).place(x=180, y=240)

        self.hlts_frame = LabelFrame(self.root, text="Highlights")
        self.hlts_list = Listbox(self.hlts_frame, width=53,font=LISTBOX_FONT , height=12,borderwidth=5,relief=FLAT)
        self.scrollbar = Scrollbar(self.hlts_frame)
        self.hlts_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.hlts_list.yview)
        self.hlts_frame.place(x=10, y=280)
        self.hlts_list.grid(row=1, column=1)
        self.scrollbar.grid(row=1, column=2, sticky=NS)

        self.fetchHighlights()

        self.button_frame = Frame(self.root)
        self.button_frame.config(bg="light grey")
        self.button_frame.place(x=170, y=520)

        self.view_hlt_btn = Button(self.button_frame, text='View', padx=10, font = BUTTON_FONT,
                                   command=lambda: self.highlightPopup(self.hlts_list.curselection()))
        self.view_hlt_btn.grid(row=1, column=1)

        Label(self.button_frame, text="    ",
              bg="light grey").grid(row=1, column=2)

        self.del_hlt_btn = Button(self.button_frame, text="Delete", padx=10, font = BUTTON_FONT,
                                  command=lambda: self.deleteHighlight(self.hlts_list.curselection()))
        self.del_hlt_btn.grid(row=1, column=3)

    def fetchHighlights(self):
        self.hlts_list.delete(0, END)
        self.highlights = self.db.getHighlights(self.book)
        for index, highlight in enumerate(self.highlights):
            hlt = highlight[1]

            if len(hlt) > 30:
                hlt = hlt[:30] + '...'

            self.hlts_list.insert(
                END, str(index + 1) + '. ' + hlt + ' @ pg. ' + str(highlight[2]))

    def highlightPopup(self, selected):
        if selected:
            HighlightsView(self.highlights[selected[0]]).start()

    def addHighlight(self):
        highlight = self.book_highlight_input_area.get('1.0', END).strip()
        page_no = self.page_no_input_area.get().strip()

        if highlight == '' or page_no == '':
            self.error_label.config(text="Both fields compulsory!")
            self.error_label.place(x=150)
        elif not page_no.isdigit():
            self.error_label.config(text="Page number must be a number!")
            self.error_label.place(x=135)
        else:
            self.db.addHighlight(highlight=highlight,
                                 page=page_no, book=self.book)
            self.fetchHighlights()

    def deleteHighlight(self, selected):
        if selected:
            self.db.deleteHighlight(self.highlights[selected[0]][0])
            self.fetchHighlights()

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    Highlights(2).start()
