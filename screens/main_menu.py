import tkinter as tk
from tkinter import *
import sqlite3
import PvBot
import sys

# Insert the path of modules folder
sys.path.insert(0, "..\\modules")

import connect4 as c4

size1 = 7

class MainMenu(Tk):
    global size1
    def __init__(self):
        self.username = None
        root = tk.Tk()
        root.resizable(False, False)
        root.iconbitmap('../assets/logo.ico')
        font_fam = ("Roboto", 18, "bold")
        font_fam2 = ("Roboto", 16, "bold")
        bg = PhotoImage(file="../assets/bg.png")
        last_obj = None
        # canvas main menu
        # --------------------------------------------------------------------------------------------------------------#
        root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Main Menu')
        canvas1 = Canvas(root, width=1280, height=640)
        button = tk.Button(root, text='PvP', bd=3, width=10, command=lambda: [self.pvp_clicked()], font=font_fam)
        button1 = tk.Button(root, text='PvE', bd=3, width=10, command=lambda: [self.pve_clicked(canvas1, root, size1)], font=font_fam)
        button2 = tk.Button(root, text='Exit', bd=3, width=10, command=root.destroy, font=font_fam)
        menu_buttons = (button, button1, button2)

        # --------------------------------------------------------------------------------------------------------------#

        # canvas login menu
        # --------------------------------------------------------------------------------------------------------------#
        def login(self, canvas1, bg, menu_buttons, canvas_login):
            if (name_field.get()):
                self.username = name_field.get()
                canvas1.pack(fill="both", expand=True),
                root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Main Menu'),
                username_is = self.username
                try:
                    sqliteConnection = sqlite3.connect('..\\db\\connect4_PythonDB.db')
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
                        print("User has beeen found")
                    else:
                        cursor.execute("INSERT INTO users (username, wins, draws, losses) VALUES (?, ?, ?, ?)",
                                       (username_is, 0, 0, 0))
                        sqliteConnection.commit()
                    cursor.close()

                except sqlite3.Error as error:
                    print("Error while connecting to sqlite", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")
                self.create_main_menu(canvas1, bg, menu_buttons, canvas_login)

        canvas_login = Canvas(root, width=1280, height=640)
        root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Login/Register')
        canvas_login.pack(fill="both", expand=True)
        canvas_login.create_image(0, 0, image=bg, anchor="nw")
        name_field = Entry(root, bd=3, width=18, font=font_fam2)
        login_button = tk.Button(root, text='Login', width=10,
                                 command=lambda: [login(self, canvas1, bg, menu_buttons, canvas_login)]
                                 , font=font_fam)
        login_button_canvas = canvas_login.create_window(552, 320, anchor="nw", window=login_button)
        username_field = canvas_login.create_window(522, 250, anchor="nw", window=name_field)
        #--------------------------------------------------------------------------------------------------------------#
        root.mainloop()

    def create_main_menu(self, canvas1, bg, button_list, canvas):
        canvas.delete("all")
        canvas.destroy()
        user = self.get_user()
        font_fam = ("Roboto", 18, "bold")
        font_fam_small = ("Roboto", 13, "bold")
        font_fam_small_2 = ("Roboto", 11, "bold")
        font_fam_small_3 = ("Roboto", 9, "bold")
        x = 552
        y = 180
        rect_start = 1052
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        #--------------------------------------------------------------------------------------------------------------#
        #Leaderboard
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
        canvas1.create_text(rect_start+100, 230, text="Top 10 Leaderboard", font=font_fam_small, anchor="center")
        canvas1.create_line(rect_start, 250, 1252, 250, fill="black", width=2.5)
        canvas1.create_text(rect_start+40, 260, text="Username", font=font_fam_small_2, anchor="center")
        canvas1.create_text(rect_start+140, 260, text="Wins/Losses/Draws", font=font_fam_small_3, anchor="center")
        canvas1.create_line(rect_start+79, 250, rect_start+79, 430, fill="black", width=1.7)
        users = self.ranking_table()
        dropdown = 270
        count = 0
        for user in users:
            if count<10:
                w_l_d_string = str(user[0][1]), "/", str(user[0][3]), "/", str(user[0][2])
                canvas1.create_text(rect_start+39, dropdown+7, text=user[0][0], font=font_fam_small_3, anchor="center")
                canvas1.create_text(rect_start + 119, dropdown+7, text=w_l_d_string, font=font_fam_small_2, anchor="center")
                dropdown += 16
                count+=1
        #--------------------------------------------------------------------------------------------------------------#

        for button in button_list:
            button_canvas = canvas1.create_window(x, y, anchor="nw", window=button)
            y+=70

    def pve_clicked(self, canvas1, root, size):
        canvas1.delete("all")
        root.destroy()
        user = self.username
        pve_screen = PvBot.pveScreen(user, size)
        bg = PhotoImage(file="../assets/bg.png")
        bg_canvas = pve_screen.canvas.create_image(0, 0, image=bg, anchor="nw")

    def ranking_table(self):
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
    def pvp_clicked(self):
        print("Hello")
        print(self.username)
        pass
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
    if user:
        player = c4.Player(user[0],user[1],user[2],user[3])