import tkinter as tk
from tkinter import *
import sqlite3

class MainMenu(Tk):
    def pvp_clicked(self):
        print("Hello")
        print(self.username)
        pass

    def __init__(self):
        self.username = None
        root = tk.Tk()
        root.resizable(False, False)
        logo = PhotoImage(file="../assets/logo.png")
        font_fam = ("Roboto", 18, "bold")
        font_fam2 = ("Roboto", 16, "bold")
        bg = PhotoImage(file="../assets/bg.png")
        # canvas main menu
        # --------------------------------------------------------------------------------------------------------------#
        root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Main Menu')
        canvas1 = Canvas(root, width=1280, height=640)
        button = tk.Button(root, text='PvP', width=10, command=lambda:[self.pvp_clicked()], font=font_fam)
        button2 = tk.Button(root, text='Exit', width=10, command=root.destroy, font=font_fam)
        menu_buttons = (button,button2)
        # --------------------------------------------------------------------------------------------------------------#

        # canvas login menu
        # --------------------------------------------------------------------------------------------------------------#
        def login(self, canvas1, bg, menu_buttons, canvas_login):
            global sqliteConnection
            if(name_field.get()):
                self.username = name_field.get()
                canvas1.pack(fill="both", expand=True),
                root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Main Menu'),
                self.create_main_menu(canvas1, bg, menu_buttons, canvas_login)
                username_is = self.username
                try:
                    sqliteConnection = sqlite3.connect('..\\db\\connect4_PythonDB.db')
                    cursor = sqliteConnection.cursor()
                    print("Database created and Successfully Connected to SQLite")

                    create_db_scheme_query = '''    CREATE TABLE IF NOT EXISTS users (
                                                    username TEXT PRIMARY KEY NOT NULL,
                                                    wins INTEGER DEFAULT 0,
                                                    draws INTEGER DEFAULT 0,
                                                    losses INTEGER DEFAULT 0
                                                    )
                                                '''

                    cursor.execute(create_db_scheme_query)
                    cursor.execute("SELECT * FROM users WHERE username=?", (username_is,))
                    user = cursor.fetchone()
                    if user:
                        print("User has beeen found")
                    else:
                        cursor.execute("INSERT INTO users (username, wins, draws, losses) VALUES (?, ?, ?, ?)",(username_is, 0, 0, 0))
                        sqliteConnection.commit()
                    cursor.close()

                except sqlite3.Error as error:
                    print("Error while connecting to sqlite", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")




        canvas_login = Canvas(root, width=1280, height=640)
        root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Login/Register')
        canvas_login.pack(fill="both", expand=True)
        canvas_login.create_image(0, 0, image=bg, anchor="nw")
        name_field = Entry(root, bd=3, width=18, font=font_fam2)
        login_button = tk.Button(root, text='Login', width=10,
                                 command=lambda: [login(self,canvas1, bg, menu_buttons, canvas_login)]
                                 , font=font_fam)
        login_button_canvas = canvas_login.create_window(552, 320, anchor="nw", window=login_button)
        username_field = canvas_login.create_window(522, 250, anchor="nw", window=name_field)
        # --------------------------------------------------------------------------------------------------------------#
        root.mainloop()


    def create_main_menu(self, canvas1, bg, button_list, canvas):
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        button_canvas = canvas1.create_window(552, 250, anchor="nw", window=button_list[0])
        button2_canvas = canvas1.create_window(552, 320, anchor="nw", window=button_list[1])
        canvas.destroy()

    def pve_clicked(self):
        pass





if __name__ == "__main__":
    Main_Menu = MainMenu()
