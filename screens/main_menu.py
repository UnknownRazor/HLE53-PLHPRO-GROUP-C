import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import json
import sys
sys.path.append('../modules')
sys.path.append('../screens')
from data import DataBase
import PvBot
import PvP
from player import Player

size1 = 7
font_fam = ("Roboto", 18, "bold")
font_fam2 = ("Roboto", 16, "bold")
file_path = "last_user.json"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

class MainMenu:
    def __init__(self, user=None):
        self.winner = None
        self.canvas = None
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.iconbitmap('../assets/logo.ico')
        self.name_field = None
        self.username = None
        self.username2 = None
        self.db = DataBase()
        self.remem = tk.BooleanVar()
        if os.path.exists(file_path):
            temp_user = data.get("username")
            self.username = temp_user
            bg = PhotoImage(file="../assets/bg.png")
            self.signup_login()
            self.create_main_menu(bg)
        elif user is not None:
            self.username = user
            bg = PhotoImage(file="../assets/bg.png")
            self.signup_login()
            self.create_main_menu(bg)
        else:
            self.create_login_menu()
        # --------------------------------------------------------------------------------------------------------------#
        self.root.mainloop()
    def create_login_menu(self):
        bg = PhotoImage(file="../assets/bg.png")
        canvas_login = Canvas(self.root, width=1280, height=640)
        self.root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Login/Register')
        canvas_login.pack(fill="both", expand=True)
        canvas_login.create_image(0, 0, image=bg, anchor="nw")
        self.canvas = canvas_login
        self.name_field = Entry(self.root, bd=3, width=18, font=font_fam2)
        login_button = tk.Button(self.root, text='Login', width=10,
                                 command=lambda: [self.login(bg)], font=font_fam)
        self.remember_me = tk.Checkbutton(self.root, text='Remember Me', variable=self.remem, onvalue=True, offvalue=False, font=font_fam)
        exit_btn = tk.Button(self.root, text='Exit', bd=3, width=10, command=lambda: [self.root.destroy()],
                             font=font_fam)
        canvas_login.create_window(552, 320, anchor="nw", window=login_button)
        canvas_login.create_window(522, 250, anchor="nw", window=self.name_field)
        canvas_login.create_window(532, 390, anchor="nw", window=self.remember_me)
        canvas_login.create_window(552, 460, anchor="nw", window=exit_btn)
    def login(self, bg):
        if self.name_field.get():
            self.username = self.name_field.get()
            if self.remem.get() == True:
                if not os.path.exists(file_path):
                    with open("last_user.json", "w") as outfile:
                        user = { "username" : self.username}
                        json.dump(user, outfile)
            # change self.root title to main menu!
            self.root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Main Menu')
            # get username for the database from the class attribute
            self.signup_login()
            # after login in make the main menu and pass in the canvases
            self.create_main_menu(bg)
    def logout(self):
        self.canvas.destroy()
        self.create_login_menu()
        if os.path.exists(file_path):
            os.remove(file_path)


    def create_main_menu(self, bg):
        font_fam_small = ("Roboto", 13, "bold")
        font_fam_small_2 = ("Roboto", 11, "bold")
        font_fam_small_3 = ("Roboto", 9, "bold")
        rank_canvas = Canvas(self.root, width=1280, height=640)
        rank_canvas.pack(fill="both", expand=True)
        if self.canvas:
            self.canvas.delete("all")
            self.canvas.destroy()
        pvp_btn = tk.Button(self.root, text='PvP', bd=3, width=10, command=lambda: [self.pvp_clicked()],
                            font=font_fam)
        pve_btn = tk.Button(self.root, text='PvE', bd=3, width=10,
                            command=lambda: [self.pve_clicked(size1)], font=font_fam)
        exit_btn = tk.Button(self.root, text='Exit', bd=3, width=10, command=self.root.destroy, font=font_fam)
        button_list = (pvp_btn, pve_btn, exit_btn)
        # Πίνακας Κατάταξης
        user = self.db.get_user(self.username)
        x = 552
        y = 180
        rect_start = 950
        rank_canvas.create_image(0, 0, image=bg, anchor="nw")
        # ------------------------------------Στοιχεία Παίκτη----------------------------------------------------------
        rank_canvas.create_rectangle(rect_start, 120, rect_start + 330, 430, fill="white")
        rank_canvas.create_text(rect_start + 60, 133, text="Player:", font=font_fam)
        rank_canvas.create_text(rect_start + 170, 133, text=user[0], font=font_fam_small, anchor="center")
        rank_canvas.create_text(rect_start + 40, 175, text=f"Games: {user[1]}", font=font_fam_small_2, anchor="center")
        rank_canvas.create_text(rect_start + 118, 175, text=f"Wins: {user[2]}", font=font_fam_small_2, anchor="center")
        rank_canvas.create_text(rect_start + 195, 175, text=f"Losses: {user[3]}", font=font_fam_small_2,
                                anchor="center")
        rank_canvas.create_text(rect_start + 275, 175, text=f"Draws: {user[4]}", font=font_fam_small_2,
                                anchor="center")
        rank_canvas.create_text(rect_start + 269, 200, text=f"ELO: {user[5]}", font=font_fam_small_2,
                                anchor="center")
        # ---------------------------------------------TOP 10-----------------------------------------------------------
        rank_canvas.create_line(rect_start, 190, rect_start + 330, 225, fill="black", width=2.5)
        rank_canvas.create_text(rect_start + 100, 230, text="Top 10 Leaderboard", font=font_fam_small, anchor="center")
        rank_canvas.create_line(rect_start, 250, rect_start + 330, 250, fill="black", width=2.5)
        rank_canvas.create_text(rect_start + 55, 260, text="Player", font=font_fam_small_2, anchor="center")
        rank_canvas.create_text(rect_start + 225, 260, text="Games / Wins / Losses / Draws / ELO",
                                font=font_fam_small_3, anchor="center")
        rank_canvas.create_line(rect_start + 115, 250, rect_start + 115, 430, fill="black", width=1.7)
        logout_btn = tk.Button(self.root, text='Logout', bd=3, width=10, command=lambda: self.logout(), font=font_fam)
        rank_canvas.create_window(x-450, y-150, anchor="nw", window=logout_btn)
        top_players = self.db.top_10()
        dropdown = 270
        for user in top_players:
            stats = f"{user[1]:>3}{user[2]:>10}{user[3]:>10}{user[4]:>11}{user[5]:>9}"
            rank_canvas.create_text(rect_start + 55, dropdown + 7, text=user[0], font=font_fam_small_3, anchor="center")
            rank_canvas.create_text(rect_start + 225, dropdown + 7, text=stats, font=font_fam_small_2, anchor="center")
            dropdown += 16
        # -------------------------------------------------------------------------------------------------------------

        for button in button_list:
            rank_canvas.create_window(x, y, anchor="nw", window=button)
            y += 70
        self.canvas = rank_canvas

    def pvp_clicked(self):
        self.canvas.destroy()
        bg = PhotoImage(file="../assets/bg.png")
        self.root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - PvP-Player 2 Login')
        pvp_canvas = Canvas(self.root, width=1280, height=640)
        pvp_canvas.pack(fill="both", expand=True)
        pvp_canvas.create_image(0, 0, image=bg, anchor="nw")
        self.name_field = Entry(self.root, bd=3, width=18, font=font_fam2)
        login_button = tk.Button(self.root, text='Play', width=10,
                                 command=lambda: [self.create_pvp()], font=font_fam)
        back_btn = tk.Button(self.root, text='Back', bd=3, width=10, command=lambda: [self.create_main_menu(bg)],
                             font=font_fam)
        exit_btn = tk.Button(self.root, text='Exit', bd=3, width=10, command=lambda: [self.root.destroy()],
                             font=font_fam)
        pvp_canvas.create_text(632, 130, text="Player 2 Login", font=font_fam,
                                anchor="center", fill="black")
        self.canvas = pvp_canvas
        pvp_canvas.create_window(552, 320, anchor="nw", window=login_button)
        pvp_canvas.create_window(522, 250, anchor="nw", window=self.name_field)
        pvp_canvas.create_window(552, 320 + 70, anchor="nw", window=back_btn)
        pvp_canvas.create_window(552, 320 + 140, anchor="nw", window=exit_btn)
        self.root.mainloop()

    def create_pvp(self):
        if self.name_field.get() and self.name_field.get() != self.username:
            self.canvas.destroy()
            self.username2 = self.name_field.get()
            pvp_screen = PvP.PVPScreen(self.username, self.username2, self.root)
        elif self.name_field.get() == "":
            messagebox.showerror('Username Error', 'Error: Username field can not be empty!')
        else:
            messagebox.showerror('Username Error', 'Error: You can not login as the same user!')

    def pve_clicked(self, size):
        self.canvas.delete("all")
        self.canvas.destroy()
        pve_canvas = Canvas(self.root, width=1280, height=640)
        pve_canvas.pack(fill="both", expand=True)
        self.canvas = pve_canvas
        bg = PhotoImage(file="../assets/bg.png")
        x = 552
        y = 180
        pve_canvas.create_image(0, 0, image=bg, anchor="nw")
        easy_btn = tk.Button(self.root, text='Easy', bd=3, width=10, command=lambda: [self.create_pve(size)],
                             font=font_fam)
        hard_btn = tk.Button(self.root, text='Hard', bd=3, width=10, command=lambda: [self.create_pve(size, True)],
                             font=font_fam)
        back_btn = tk.Button(self.root, text='Back', bd=3, width=10, command=lambda: [self.create_main_menu(bg)],
                             font=font_fam)
        exit_btn = tk.Button(self.root, text='Exit', bd=3, width=10, command=lambda: [self.root.destroy()],
                             font=font_fam)

        button_list = (easy_btn, hard_btn)
        for button in button_list:
            pve_canvas.create_window(x, y, anchor="nw", window=button)
            y += 80
        pve_canvas.create_window(x, y + 70, anchor="nw", window=back_btn)
        pve_canvas.create_window(x, y + 140, anchor="nw", window=exit_btn)
        self.root.mainloop()

    def create_pve(self, size, difficulty=False):
        if difficulty:
            self.canvas.destroy()
            pve_screen = PvBot.PVEScreen(self.username, size, self.root, True)
        else:
            self.canvas.destroy()
            pve_screen = PvBot.PVEScreen(self.username, size, self.root)

    def signup_login(self):  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!
        username_is = self.username
        new_user = Player(username_is)
        self.db.insert_table(new_user)


if __name__ == "__main__":
    Main_Menu = MainMenu()
