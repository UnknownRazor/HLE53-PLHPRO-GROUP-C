import tkinter as tk
from tkinter import *


class end_screen(Tk):
    def __init__(self, canvas, root, username1, username2=""):
        canvas.destroy()
        self.root = root
        end_canvas = Canvas(self.root, width=1280, height=640)
        bg = PhotoImage(file="../assets/bg.png")
        end_canvas.pack(fill="both", expand=True)
        end_canvas.create_image(0, 0, image=bg, anchor="nw")
        self.root.mainloop()
