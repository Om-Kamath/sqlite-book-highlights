from tkinter import *
from db.database import BookHighlightsDB
from properties import HIGHLIGHT_FONT


class HighlightsView:
    def __init__(self, highlight, update_highlights) -> None:
        self.root = Toplevel()
        self.root.title((highlight[1][:20] + '...')
                        if len(highlight[1]) > 20 else highlight[1])
        self.root.config(bg="light grey")
        self.root.geometry('320x323+550+250')
        self.root.resizable(0, 0)
        self.root.after(1, lambda: self.root.focus_force())
        self.root.protocol("WM_DELETE_WINDOW", self.setHighlight)
        self.root.iconphoto(False, PhotoImage(file='icons/logo.png'))

        self.update_highlights = update_highlights
        self.db = BookHighlightsDB()
        self.highlight_id = highlight[0]

        self.hlt = Text(self.root, width=35, height=13,
                        padx=10, pady=10, font=HIGHLIGHT_FONT)
        self.hlt.grid(row=1, column=1, sticky=NSEW)
        self.hlt.config(wrap=WORD)
        self.hlt.insert(END, highlight[1])
        # self.hlt.config(state=DISABLED)

        scrollbar = Scrollbar(self.root)
        scrollbar.grid(row=1, column=2, sticky=NS)
        self.hlt.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.hlt.yview)

    def setHighlight(self):
        value = self.hlt.get('1.0', END).strip()
        self.db.updateHighlight(value, self.highlight_id)
        self.update_highlights()
        self.root.destroy()

    def start(self):
        self.root.mainloop()
