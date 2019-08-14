from tkinter import *


class tkwindow:
    def __init__(self, pos_x, pos_y):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.iconbitmap(r'C:\Python37\DLLs\py.ico')
        self.root.title("MyChess")
        self.root.lift()

        self.w = 250    # window width
        self.h = 800    # window height

        # set coordinates of tkwindow
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, pos_x, pos_y))

        self.loop_active = True

        self.label = Label(self.root, text="MyChess v0.7-beta")
        self.label.pack(side="top")

        self.lb = Listbox(self.root, width=200, height=750, borderwidth=2)

    def set_text(self, message, color):
        self.lb.insert(END, message)
        self.lb.itemconfig(END, bg=color)
        self.lb.see("end")
        self.lb.pack(side="left", fill="both", expand=1)
        self.root.update()

    def clear_text(self):
        self.lb.delete(0, 'end')
        self.root.update()
