import tkinter as tk
from tkinter import *
from modules.data import DataBase
import PvBot
import PvP
from modules.game import Game
from modules.player import Player


size1 = 7
font_fam = ("Roboto", 18, "bold")
font_fam2 = ("Roboto", 16, "bold")


class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.iconbitmap('../assets/logo.ico')
        self.name_field = None
        self.username = None
        self.create_login_menu()
        # --------------------------------------------------------------------------------------------------------------#
        self.root.mainloop()

    def create_login_menu(self):
        bg = PhotoImage(file="../assets/bg.png")
        canvas_login = Canvas(self.root, width=1280, height=640)
        self.root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Login/Register')
        canvas_login.pack(fill="both", expand=True)
        canvas_login.create_image(0, 0, image=bg, anchor="nw")
        self.name_field = Entry(self.root, bd=3, width=18, font=font_fam2)
        login_button = tk.Button(self.root, text='Login', width=10,
                                 command=lambda: [self.login(bg, canvas_login)], font=font_fam)
        canvas_login.create_window(552, 320, anchor="nw", window=login_button)
        canvas_login.create_window(522, 250, anchor="nw", window=self.name_field)

    def login(self, bg, canvas_login):
        if self.name_field.get():
            self.username = self.name_field.get()
            # change self.root title to main menu!
            self.root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Main Menu')
            # get username for the database from the class attribute
            self.signup_login()
            # after login in make the main menu and pass in the canvases
            self.create_main_menu(bg, canvas_login)

    def create_main_menu(self, bg, canvas):
        font_fam_small = ("Roboto", 13, "bold")
        font_fam_small_2 = ("Roboto", 11, "bold")
        font_fam_small_3 = ("Roboto", 9, "bold")
        rank_canvas = Canvas(self.root, width=1280, height=640)
        rank_canvas.pack(fill="both", expand=True)
        canvas.delete("all")
        canvas.destroy()
        pvp_btn = tk.Button(self.root, text='PvP', bd=3, width=10, command=lambda: [self.pvp_clicked()],
                           font=font_fam)
        pve_btn = tk.Button(self.root, text='PvE', bd=3, width=10,
                            command=lambda: [self.pve_clicked(rank_canvas, size1)], font=font_fam)
        exit_btn = tk.Button(self.root, text='Exit', bd=3, width=10, command=self.root.destroy, font=font_fam)
        button_list = (pvp_btn, pve_btn, exit_btn)
        # Πίνακας Κατάταξης
        user = db.get_user(self.username)
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

        top_players = db.ranking()
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

    def pvp_clicked(self):
        self.root.destroy()
        user = self.username
        pvp_screen = PvP.PVPScreen(user, 7, True)
        self.root = pvp_screen.get_root()

    def pve_clicked(self, rank_canvas, size):
        rank_canvas.delete("all")
        rank_canvas.destroy()
        pve_canvas = Canvas(self.root, width=1280, height=640)
        pve_canvas.pack(fill="both", expand=True)

        bg = PhotoImage(file="../assets/bg.png")
        x = 552
        y = 180
        pve_canvas.create_image(0, 0, image=bg, anchor="nw")
        easy_btn = tk.Button(self.root, text='Easy', bd=3, width=10, command=lambda: [self.create_pve(size)], font=font_fam)
        hard_btn = tk.Button(self.root, text='Hard', bd=3, width=10, command=lambda: [self.create_pve(size)], font=font_fam)
        back_btn = tk.Button(self.root, text='Back', bd=3, width=10, command=lambda: [self.create_main_menu(bg, pve_canvas)], font=font_fam)
        exit_btn = tk.Button(self.root, text='Exit', bd=3, width=10, command=lambda: [self.root.destroy()], font=font_fam)

        button_list = (easy_btn, hard_btn)
        for button in button_list:
            pve_canvas.create_window(x, y, anchor="nw", window=button)
            y += 80
        pve_canvas.create_window(x, y + 70, anchor="nw", window=back_btn)
        pve_canvas.create_window(x, y + 140, anchor="nw", window=exit_btn)
        self.root.mainloop()

    def create_pve(self, size, difficulty=False):
        if difficulty:
            self.root.destroy()
            user = self.username
            pve_screen = PvBot.PVEScreen(user, size, True)
            self.root = pve_screen.get_root()
        else:
            self.root.destroy()
            user = self.username
            pve_screen = PvBot.PVEScreen(user, size)
            self.root = pve_screen.get_root()

    def signup_login(self):# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
        username_is = self.username
        new_user = Player(username_is)
        db.insert_table(new_user)

if __name__ == "__main__":
    db = DataBase()
    game = Game()
    Main_Menu = MainMenu()

