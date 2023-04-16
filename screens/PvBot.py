import tkinter as tk
from tkinter import *

class pveScreen(Tk):
    def __init__(self, username):
        self.username = username
        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("1280x640")
        root.iconbitmap('../assets/logo.ico')
        font_fam = ("Roboto", 18, "bold")
        font_fam2 = ("Roboto", 14, "bold")
        bg = PhotoImage(file="../assets/bg.png")
        # canvas main menu
        # --------------------------------------------------------------------------------------------------------------#
        root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - PvE')
        canvas1 = Canvas(root, width=1280, height=640)
        canvas1.pack(fill="both", expand=True)
        button =  tk.Button(root, text='', bd=3, width=2, command=lambda: [], font=font_fam)
        button1 = tk.Button(root, text='', bd=3, width=2, command=lambda: [], font=font_fam)
        button2 = tk.Button(root, text='', bd=3, width=2, command=root.destroy, font=font_fam)
        button3 = tk.Button(root, text='', bd=3, width=2, command=root.destroy, font=font_fam)
        button4 = tk.Button(root, text='', bd=3, width=2, command=root.destroy, font=font_fam)
        menu_buttons = (button, button1, button2, button3, button4)

        self.create_buttons(menu_buttons, canvas1)

        canvas1.create_image(0, 0, image=bg, anchor="nw")



    def create_buttons(self, button_list, canvas1):
        x = 252
        y = 180
        for button in button_list:
            button_canvas = canvas1.create_window(x, y, anchor="nw", window=button)
            x += 70