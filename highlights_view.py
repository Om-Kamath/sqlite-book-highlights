from tkinter import *


class HighlightsView:
    def __init__(self, highlight) -> None:
        self.root = Tk()
        self.root.title((highlight[1][:20] + '...')
                        if len(highlight[1]) > 20 else highlight[1])
        self.root.config(bg="light grey")
        self.root.geometry('320x325+550+250')
        self.root.resizable(0, 0)
        self.root.after(1, lambda: self.root.focus_force())

        self.hlt = Text(self.root, width=35, height=19, padx=10, pady=10)
        self.hlt.grid(row=1, column=1,sticky=NSEW)
        self.hlt.config(wrap=WORD)
        self.hlt.insert(END, highlight[1])
        self.hlt.config(state=DISABLED)

        scrollbar = Scrollbar(self.root)
        scrollbar.grid(row=1, column=2, sticky=NS)
        self.hlt.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.hlt.yview)

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    HighlightsView((1, '''Nullam nec tempor ipsum. Etiam suscipit mollis porttitor. Phasellus turpis nulla, ultrices a lectus non, condimentum lobortis mi. Aliquam vel neque a felis faucibus bibendum a ut nibh. Praesent scelerisque fringilla tortor eget hendrerit. Proin aliquam convallis sapien, quis eleifend orci sodales a. Nam eleifend vestibulum magna, quis pellentesque nibh sagittis eu. Curabitur sagittis maximus magna, sit amet euismod urna efficitur ut. Curabitur porttitor, lorem vel condimentum euismod, diam nisi ultricies tortor, et laoreet ipsum purus ac neque. Suspendisse id sem in felis porta vehicula et in magna. Suspendisse eget euismod dui, eget malesuada libero. Donec non arcu lorem. Nam venenatis vehicula mi. Duis vitae fringilla mi, in pulvinar ante.

Ut iaculis pellentesque purus vel luctus. Phasellus laoreet nisi et ante vulputate tempus. Nunc feugiat vestibulum eros. Curabitur ornare, tortor at ultrices posuere, velit metus aliquet ligula, eu bibendum dolor purus in orci. Suspendisse tempor, risus ut efficitur laoreet, nibh erat pretium arcu, quis elementum nibh ipsum et orci. Aenean non volutpat enim. Morbi aliquet, felis non pellentesque porta, sem lacus rutrum odio, venenatis pharetra ex erat eget orci. Curabitur at tincidunt libero. Aliquam pharetra fermentum tortor, sed viverra tortor maximus id. Ut at lorem vel risus sollicitudin feugiat porttitor quis nunc. Etiam egestas ac dui et aliquam. Aliquam sodales, ex vitae congue faucibus, augue dui rhoncus sapien, vitae lacinia risus enim vel est.

Cras eget lectus nec risus tristique efficitur. Praesent dapibus enim ac erat dictum, ac malesuada diam venenatis. Nulla congue eu nulla in interdum. Quisque eu pharetra lacus. Cras accumsan semper elit id porta. Sed commodo elit sit amet ligula vestibulum, nec accumsan dui congue. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Proin suscipit tempor velit ut efficitur.''', 20)).start()
