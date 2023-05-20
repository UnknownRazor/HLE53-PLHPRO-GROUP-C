import tkinter as tk
from tkinter import *
import os
import sys
sys.path.append('../modules')
sys.path.append('../screens')
from data import DataBase
from game import Game
from main_menu import MainMenu

class end_screen(Tk):
    def __init__(self, canvas, root, username1, winner):
        canvas.destroy()
        self.root = root
        self.root.geometry("1280x640")
        font_fam = ("Roboto", 80, "bold")
        font_fam_small = ("Roboto", 60, "bold")
        self.canvas = Canvas(self.root, width=1280, height=640)
        bg = PhotoImage(file="../assets/bg.png")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.username = username1
        if winner == 3:
            self.canvas.create_text(632, 250, text=f"Draw", font=font_fam,
                                   anchor="center", fill="black")
        elif winner == "Computer":
            self.canvas.create_text(632, 250, text=f"You Lose!", font=font_fam,
                                   anchor="center", fill="black")
        else:
            self.canvas.create_text(632, 220, text=f"Winner:", font=font_fam,
                                   anchor="center", fill="black")
            self.canvas.create_text(632, 320, text=f"{username1}", font=font_fam_small,
                                   anchor="center", fill="black")
        main_button = tk.Button(self.root, text='Main menu', width=12,
                                 command=lambda: [self.main_menu()], font=("Roboto", 18, "bold"))
        # self.remember_me = tk.Checkbutton(self.root, text='Python',variable=self.remem, onvalue=1, offvalue=0, command=print_selection)
        self.canvas.create_window(552, 380, anchor="nw", window=main_button)
        exit_button = tk.Button(self.root, text='Exit', width=12,
                                command=lambda: [self.exit()], font=("Roboto", 18, "bold"))
        # self.remember_me = tk.Checkbutton(self.root, text='Python',variable=self.remem, onvalue=1, offvalue=0, command=print_selection)
        self.canvas.create_window(552, 440, anchor="nw", window=exit_button)
        self.root.mainloop()

    def main_menu(self):
        self.root.destroy()
        x = MainMenu(self.username)
        db = DataBase()
        game = Game()
    def exit(self):
        file_path = "last_user.json"
        if os.path.exists(file_path):
            os.remove(file_path)
        self.root.destroy()