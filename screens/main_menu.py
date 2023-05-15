import tkinter as tk
from sqlite3 import Connection
from tkinter import *
import sqlite3
import PvBot
import sys

# Insert the path of modules folder
sys.path.insert(0, "..\\modules")

import modules.connect4 as c4

size1 = 7
font_fam = ("Roboto", 18, "bold")
font_fam2 = ("Roboto", 16, "bold")


def ranking_table():
    users = []
    try:
        sqliteConnection = sqlite3.connect('..\\db\\connect4_PythonDB.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute("SELECT * FROM users")
        user = cursor.fetchall()
        for _user in user:
            elo = _user[1] - _user[3]
            user_info = [_user, elo]
            users.append(user_info)
        users.sort(key=lambda user: user[1], reverse=True)
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return users


class MainMenu(Tk):
    global size1
    global font_fam
    global font_fam2

    def __init__(self):
        self.username = None
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.iconbitmap('../assets/logo.ico')
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
                                 command=lambda: [self.login(bg, canvas_login)]
                                 , font=font_fam)
        login_button_canvas = canvas_login.create_window(552, 320, anchor="nw", window=login_button)
        username_field = canvas_login.create_window(522, 250, anchor="nw", window=self.name_field)
    def login(self, bg, canvas_login):
        if (self.name_field.get()):
            self.username = self.name_field.get()
            # change self.root title to main menu!
            self.root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Main Menu')
            # get username for the database from the class attribute
            self.signup_login()
            # after login in make the main menu and pass in the canvases
            self.create_main_menu(bg, canvas_login)

    def create_main_menu(self, bg, canvas):
        font_fam = ("Roboto", 18, "bold")
        font_fam_small = ("Roboto", 13, "bold")
        font_fam_small_2 = ("Roboto", 11, "bold")
        font_fam_small_3 = ("Roboto", 9, "bold")
        canvas1 = Canvas(self.root, width=1280, height=640)
        canvas1.pack(fill="both", expand=True)
        canvas.delete("all")
        canvas.destroy()
        button = tk.Button(self.root, text='PvP', bd=3, width=10, command=lambda: [self.pvp_clicked()],
                           font=font_fam)
        button1 = tk.Button(self.root, text='PvE', bd=3, width=10,
                            command=lambda: [self.pve_clicked(canvas1, size1)], font=font_fam)
        button2 = tk.Button(self.root, text='Exit', bd=3, width=10, command=self.root.destroy, font=font_fam)
        button_list = (button, button1, button2)
        user = self.get_user()
        x = 552
        y = 180
        rect_start = 1052
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        # --------------------------------------------------------------------------------------------------------------#
        # Leaderboard
        canvas1.create_rectangle(rect_start, 120, rect_start + 200, 430, fill="white")
        canvas1.create_text(rect_start + 100, 133, text="User", font=font_fam)
        canvas1.create_text(rect_start + 55, 155, text=user[0], font=font_fam_small, anchor="center")
        canvas1.create_text(rect_start + 35, 175, text="Wins: " + str(user[1]), font=font_fam_small_2, anchor="center")
        canvas1.create_text(rect_start + 95, 175, text="Draws: " + str(user[2]), font=font_fam_small_2, anchor="center")
        canvas1.create_text(rect_start + 163, 175, text="Losses: " + str(user[3]), font=font_fam_small_2,
                            anchor="center")
        canvas1.create_text(rect_start + 163, 190, text="Elo: " + str(user[1] - user[3]), font=font_fam_small_2,
                            anchor="center")
        canvas1.create_line(rect_start, 190, rect_start + 200, 210, fill="black", width=2.5)
        canvas1.create_text(rect_start + 100, 230, text="Top 10 Leaderboard", font=font_fam_small, anchor="center")
        canvas1.create_line(rect_start, 250, 1252, 250, fill="black", width=2.5)
        canvas1.create_text(rect_start + 40, 260, text="Username", font=font_fam_small_2, anchor="center")
        canvas1.create_text(rect_start + 140, 260, text="Wins/Losses/Draws", font=font_fam_small_3, anchor="center")
        canvas1.create_line(rect_start + 79, 250, rect_start + 79, 430, fill="black", width=1.7)
        users = ranking_table()
        dropdown = 270
        count = 0
        for user in users:
            if count < 10:
                win_loss_draw_string = str(user[0][1]), "/", str(user[0][3]), "/", str(user[0][2])
                canvas1.create_text(rect_start + 39, dropdown + 7, text=user[0][0], font=font_fam_small_3,
                                    anchor="center")
                canvas1.create_text(rect_start + 119, dropdown + 7, text=win_loss_draw_string, font=font_fam_small_2,
                                    anchor="center")
                dropdown += 16
                count += 1
        # --------------------------------------------------------------------------------------------------------------#

        for button in button_list:
            button_canvas = canvas1.create_window(x, y, anchor="nw", window=button)
            y += 70

    def pvp_clicked(self):
        pass

    def pve_clicked(self, canvas1, size):
        canvas1.delete("all")
        canvas1.destroy()
        pve_canvas = Canvas(self.root, width=1280, height=640)
        pve_canvas.pack(fill="both", expand=True)

        bg = PhotoImage(file="../assets/bg.png")
        x = 552
        y = 180
        pve_canvas.create_image(0, 0, image=bg, anchor="nw")
        button = tk.Button(self.root, text='Easy', bd=3, width=10, command=lambda: [self.create_pve(size)], font=font_fam)
        button1 = tk.Button(self.root, text='Hard', bd=3, width=10, command=lambda: [self.create_pve(size)], font=font_fam)
        button2 = tk.Button(self.root, text='Back', bd=3, width=10, command=lambda: [self.create_main_menu(bg, pve_canvas)], font=font_fam)
        button3 = tk.Button(self.root, text='Exit', bd=3, width=10, command=lambda: [self.root.destroy()], font=font_fam)

        button_list = (button, button1, button2, button3)
        for button in button_list:
            button_canvas = pve_canvas.create_window(x, y, anchor="nw", window=button)
            y += 70
        self.root.mainloop()
    def create_pve(self, size, difficulty=False):
        if difficulty:
            self.root.destroy()
            user = self.username
            pve_screen = PvBot.pveScreen(user, size, True)
            self.root = pve_screen.get_root()
        else:
            self.root.destroy()
            user = self.username
            pve_screen = PvBot.pveScreen(user, size)
            self.root = pve_screen.get_root()

    def signup_login(self):
        username_is = self.username
        try:
            # make sqlite connection
            sqliteConnection: Connection = sqlite3.connect('..\\db\\connect4_PythonDB.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")

            create_db_scheme_query = '''CREATE TABLE IF NOT EXISTS users (
                                        username TEXT PRIMARY KEY NOT NULL,
                                        wins INTEGER DEFAULT 0,
                                        draws INTEGER DEFAULT 0,
                                        losses INTEGER DEFAULT 0)'''

            cursor.execute(create_db_scheme_query)
            cursor.execute("SELECT * FROM users WHERE username=?", (username_is,))
            user = cursor.fetchone()
            if user:
                # print("User has beeen found")
                pass
            else:
                cursor.execute("INSERT INTO users (username, wins, draws, losses) VALUES (?, ?, ?, ?)",
                               (username_is, 0, 0, 0))
                sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            tk.messagebox.showerror('Python Error', f'Error while connecting to sqlite {error}')
        finally:
            if sqliteConnection:
                # even if errors occured close the connection
                sqliteConnection.close()

    def get_user(self):
        try:
            sqliteConnection = sqlite3.connect('..\\db\\connect4_PythonDB.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            username_is = self.username
            cursor.execute("SELECT * FROM users WHERE username=?", (username_is,))
            user = cursor.fetchone()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        return user


if __name__ == "__main__":
    Main_Menu = MainMenu()
    user = Main_Menu.get_user()
