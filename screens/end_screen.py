import tkinter as tk
from tkinter import *
class end_screen(Tk):
    def __init__(self, canvas, root):
        canvas.destroy()
        end_canvas = tk.Canvas(root)
        bg = PhotoImage(file="../assets/bg.png")