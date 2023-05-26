import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import os
import json
from game import Game
from data import *

font_fam = ("Roboto", 18, "bold")
font_fam1 = ("Roboto", 22, "bold")
font_fam2 = ("Roboto", 16, "bold")
font_fam3 = ("Roboto", 80, "bold")
font_fam4 = ("Roboto", 60, "bold")
font_fam_small = ("Roboto", 13, "bold")
font_fam_small2 = ("Roboto", 11, "bold")
font_fam_small3 = ("Roboto", 9, "bold")



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.size = 7
        self.winner = None
        self.canvas = None
        self.resizable(False, False)
        self.iconbitmap('logo.ico')
        self.bg = PhotoImage(file="bg.png")
        self.name_field = None
        self.username = None
        self.username2 = None
        self.db = DataBase()
        self.game = Game(self.username, self.username2)
        self.remember_me = None
        self.remem = tk.BooleanVar()
        self.file_path = "last_user.json"
        self.user_logged_in()

        # --------------pve - pvp  ------------------------
        self.button_array = []
        self.img = PhotoImage(file="white.png")
        self.game_mode = None
        self.images = []
        self.difficulty = False
        self.image_items = []

        # ---------------- game mode -------------------------
        self.turn = 1
        self.can_play = True
        self.white = PhotoImage(file="white.png")
        self.red = PhotoImage(file="red.png")
        self.yellow = PhotoImage(file="yellow.png")
        self.img_array = [self.white, self.red, self.yellow]
        self.won = False
        self.thread = None
    # -------------------------------------------------------------------------------------------------------------

    # έλεγχος αν ο χρήστης παραμένει συνδεμένος
    def user_logged_in(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
            self.username = data.get("username")
            self.game.player1 = Player(self.username)
            self.db.insert_table(self.game.player1)
            self.create_main_menu()
        else:
            self.create_login_menu()

    # δημιουργία Login Menu, με επιλογή Remember me ώστε να παραμένει συνδεμένος
    def create_login_menu(self):
        self.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Login/Register')
        self.canvas = Canvas(self, width=1280, height=640)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        # self.canvas = canvas_login
        self.name_field = Entry(self, bd=3, width=18, font=font_fam2)
        login_button = tk.Button(self, text='Login', width=10, command=self.login, font=font_fam)
        self.remember_me = tk.Checkbutton(self, text='Remember Me', variable=self.remem, onvalue=True, offvalue=False,
                                          font=font_fam)
        exit_btn = tk.Button(self, text='Exit', bd=3, width=10, command=self.exit, font=font_fam)
        self.canvas.create_window(552, 320, anchor="nw", window=login_button)
        self.canvas.create_window(522, 250, anchor="nw", window=self.name_field)
        self.canvas.create_window(532, 390, anchor="nw", window=self.remember_me)
        self.canvas.create_window(552, 460, anchor="nw", window=exit_btn)

    # σύνδεση χρήστη και εισαγωγή στο Database
    def login(self):
        if self.name_field.get():
            self.username = self.name_field.get()
            if self.remem.get():
                if not os.path.exists(self.file_path):
                    with open("last_user.json", "w") as outfile:
                        user = { "username" : self.username}
                        json.dump(user, outfile)
            self.game.player1 = Player(self.username)
            self.db.insert_table(self.game.player1)
            self.create_main_menu()

    # αποσύνδεση χρήση
    def logout(self):
        self.canvas.destroy()
        self.create_login_menu()
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    # δημιουργία Main Menu. Επιλογή PvP / PvE και εμφάνιση στοιχείων συνδεμένου παίκτη και Top 10
    def create_main_menu(self):
        self.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - Main Menu')
        if self.canvas:
            self.canvas.delete("all")
            self.canvas.destroy()
        self.canvas = Canvas(self, width=1280, height=640)
        self.canvas.pack(fill="both", expand=True)
        # if self.canvas:
        #     self.canvas.delete("all")
        #     self.canvas.destroy()
        # self.canvas = rank_canvas
        pvp_btn = tk.Button(self, text='PvP', bd=3, width=10, command=self.pvp_clicked, font=font_fam)
        pve_btn = tk.Button(self, text='PvE', bd=3, width=10, command=self.pve_clicked, font=font_fam)
        exit_btn = tk.Button(self, text='Exit', bd=3, width=10, command=self.exit, font=font_fam)
        button_list = (pvp_btn, pve_btn, exit_btn)
        # Πίνακας Κατάταξης
        user = self.db.get_user(self.username)
        x = 552
        y = 180
        rect_start = 950
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        # ------------------------------------Στοιχεία Παίκτη----------------------------------------------------------
        self.canvas.create_rectangle(rect_start, 120, rect_start + 330, 430, fill="white")
        self.canvas.create_text(rect_start + 60, 133, text="Player:", font=font_fam)
        self.canvas.create_text(rect_start + 170, 133, text=user[0], font=font_fam_small, anchor="center")
        self.canvas.create_text(rect_start + 40, 175, text=f"Games: {user[1]}", font=font_fam_small2, anchor="center")
        self.canvas.create_text(rect_start + 118, 175, text=f"Wins: {user[2]}", font=font_fam_small2, anchor="center")
        self.canvas.create_text(rect_start + 195, 175, text=f"Losses: {user[3]}", font=font_fam_small2, anchor="center")
        self.canvas.create_text(rect_start + 275, 175, text=f"Draws: {user[4]}", font=font_fam_small2, anchor="center")
        self.canvas.create_text(rect_start + 269, 200, text=f"ELO: {user[5]}", font=font_fam_small2, anchor="center")
        # ---------------------------------------------TOP 10-----------------------------------------------------------
        self.canvas.create_line(rect_start, 190, rect_start + 330, 225, fill="black", width=2.5)
        self.canvas.create_text(rect_start + 100, 230, text="Top 10 Leaderboard", font=font_fam_small, anchor="center")
        self.canvas.create_line(rect_start, 250, rect_start + 330, 250, fill="black", width=2.5)
        self.canvas.create_text(rect_start + 55, 260, text="Player", font=font_fam_small2, anchor="center")
        self.canvas.create_text(rect_start + 225, 260, text="Games / Wins / Losses / Draws / ELO",
                                font=font_fam_small3, anchor="center")
        self.canvas.create_line(rect_start + 115, 250, rect_start + 115, 430, fill="black", width=1.7)
        logout_btn = tk.Button(self, text='Logout', bd=3, width=10, command=self.logout, font=font_fam)
        self.canvas.create_window(x-450, y-150, anchor="nw", window=logout_btn)
        top_players = self.db.top_10()
        dropdown = 270
        for user in top_players:
            stats = f"{user[1]:>3}{user[2]:>10}{user[3]:>10}{user[4]:>11}{user[5]:>9}"
            self.canvas.create_text(rect_start + 55, dropdown + 7, text=user[0], font=font_fam_small3, anchor="center")
            self.canvas.create_text(rect_start + 225, dropdown + 7, text=stats, font=font_fam_small2, anchor="center")
            dropdown += 16

        for button in button_list:
            self.canvas.create_window(x, y, anchor="nw", window=button)
            y += 70

    # PvP - σύνδεση δεύτερου παίκτη
    def pvp_clicked(self):
        self.canvas.delete("all")
        self.canvas.destroy()
        self.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - PvP-Player 2 Login')
        self.canvas = Canvas(self, width=1280, height=640)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        self.name_field = Entry(self, bd=3, width=18, font=font_fam2)
        login_button = tk.Button(self, text='Play', width=10, command=self.create_pvp, font=font_fam)
        back_btn = tk.Button(self, text='Back', bd=3, width=10, command=self.create_main_menu, font=font_fam)
        exit_btn = tk.Button(self, text='Exit', bd=3, width=10, command=self.exit, font=font_fam)
        self.canvas.create_text(632, 175, text="Player 2 Login", font=font_fam1, anchor="center", fill="black")
        # self.canvas = pvp_canvas
        self.canvas.create_window(552, 320, anchor="nw", window=login_button)
        self.canvas.create_window(522, 250, anchor="nw", window=self.name_field)
        self.canvas.create_window(552, 320 + 70, anchor="nw", window=back_btn)
        self.canvas.create_window(552, 320 + 140, anchor="nw", window=exit_btn)

    # εισαγωγή ονόματος δεύτερου παίκτη
    def create_pvp(self):
        if self.name_field.get() and self.name_field.get() != self.username:
            self.username2 = self.name_field.get()
            self.game.player2 = Player(self.username2)
            self.db.insert_table(self.game.player2)
            self.pvp_screen()
        else:
            messagebox.showerror('Username Error', 'Error: You can not login as the same user!')

    # επιλογή βαθμού δυσκολίας PvE (easy/hard)
    def pve_clicked(self):
        self.canvas.delete("all")
        self.canvas.destroy()
        self.canvas = Canvas(self, width=1280, height=640)
        self.canvas.pack(fill="both", expand=True)
        # self.canvas = pve_canvas
        x = 552
        y = 180
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        easy_btn = tk.Button(self, text='Easy', bd=3, width=10, command=self.create_pve, font=font_fam)
        hard_btn = tk.Button(self, text='Hard', bd=3, width=10, command=lambda: self.create_pve(True), font=font_fam)
        back_btn = tk.Button(self, text='Back', bd=3, width=10, command=self.create_main_menu, font=font_fam)
        exit_btn = tk.Button(self, text='Exit', bd=3, width=10, command=self.exit, font=font_fam)

        button_list = (easy_btn, hard_btn)
        for button in button_list:
            self.canvas.create_window(x, y, anchor="nw", window=button)
            y += 80
        self.canvas.create_window(x, y + 70, anchor="nw", window=back_btn)
        self.canvas.create_window(x, y + 140, anchor="nw", window=exit_btn)

    # μεταφορά σε ταμπλό PvE
    def create_pve(self, difficulty=False):
        if difficulty:
            self.canvas.destroy()
            self.difficulty = True
            self.pve_screen()
        else:
            self.canvas.destroy()
            self.difficulty = False
            self.pve_screen()

# ----------------------------------------------------------------------------------------------------------------
    # δημιουργία ταμπλό PvP
    def pvp_screen(self):
        self.canvas.destroy()
        self.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - PvP')
        self.canvas = Canvas(width=1280, height=640)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        exit_button = tk.Button(text='Exit', bd=5, width=3, command = self.exit, font=font_fam, highlightcolor="black")
        self.canvas.create_window(12, 20, anchor="nw", window=exit_button)
        self.canvas.create_line(82.8, 0, 82.8, 640, fill="black", width=2.5)

        menu_buttons = []
        for counter in range(0, self.size):
            menu_buttons.append(counter)
        column_buttons = self.create_buttons(menu_buttons, 0, 0, False, True)

        self.create_hover(menu_buttons, column_buttons)
        play_list = self.create_button_array()
        self.button_array = play_list[1]

        self.canvas.bind("<Button-1>", lambda event: self.on_canvas_click(event, menu_buttons, column_buttons))
        self.canvas.bind("<Motion>", lambda event: self.on_mouse_move(event, menu_buttons, column_buttons))
        self.game_mode = "pvp"

    # δημιουργία ταμπλό PvE
    def pve_screen(self):
        self.canvas.destroy()
        self.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - PvE')
        self.canvas = Canvas(self, width=1280, height=640)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        exit_btn = tk.Button(self, text='Exit', bd=5, width=3, command=self.exit, font=font_fam, highlightcolor="black")
        self.canvas.create_window(12, 20, anchor="nw", window=exit_btn)
        self.canvas.create_line(82.8, 0, 82.8, 640, fill="black", width=2.5)

        menu_buttons = []
        for counter in range(0, self.size):
            menu_buttons.append(counter)
        column_buttons = self.create_buttons(menu_buttons, 0, 0, False, True)
        self.img = PhotoImage(file="white.png")
        play_list = self.create_button_array()
        self.button_array = play_list[1]
        self.images = []
        self.create_hover(menu_buttons, column_buttons)
        self.canvas.bind("<Button-1>", lambda event: self.on_canvas_click(event, menu_buttons, column_buttons))
        self.canvas.bind("<Motion>", lambda event: self.on_mouse_move(event, menu_buttons, column_buttons))
        self.game_mode = "pve"

    # εμφάνιση / απόκρυψη κουμπιών στήλης σύμφωνα με τη θέση του ποντικιού
    def create_hover(self, col_array, coord_list):
        for button in col_array:
            coord_list_copy = coord_list[button]
            image = tk.PhotoImage(file="white.png")
            self.images.append(image)
            self.image_items.append(
            self.canvas.create_image(coord_list_copy[0], coord_list_copy[2], image=image, anchor="nw", state="hidden"))

    # δημιουργία ταμπλό (γραμμές x στήλες)
    def create_button_array(self):
        button_canvas_array = []
        buttons_grid = []
        button_row = []
        y = 10
        for row in range(0, self.size - 1):
            for col in range(0, self.size):
                button = tk.Label(self.canvas, image=self.img, borderwidth=0, highlightthickness=0)
                button_row.append(button)
            buttons_grid.append(button_row)
            if len(button_row) >= self.size:
                button_row = []
            x = 5
            y += 80
            button_canvas_array = self.create_buttons(buttons_grid[row], x, y, True)
        return [button_canvas_array, buttons_grid]

    # δημιουργεί τα κουμπιά των στηλών (πάνω από το ταμπλό)
    def create_buttons(self, button_list, offsetX, offsetY, half=False, button_coord=False):
        x = 92 + offsetX
        y = 10 + offsetY
        button_canvas_array = []
        button_coords = []
        button_coords_list = []
        if button_coord:
            for button in button_list:
                button_coords = [x, x + 80, y, y + 65]
                button_coords_list.append(button_coords)
                x += 80
            return button_coords_list
        for button in button_list:
            button_canvas = self.canvas.create_window(x, y, anchor="nw", window=button)
            x += 80
            button_coords.append(x)
            button_coords.append(y)
            if half:
                x = x
            button_canvas_array.append(button_canvas)
        return button_canvas_array

    # έλεγχος αν το ποντίκι είναι πάνω από ένα κουμπί
    def is_within_button(self, x, y, button_coords):
        button_x1, button_x2, button_y1, button_y2 = button_coords
        if button_x1 <= x <= button_x2 and button_y1 <= y <= button_y2:
            return True
        return False

    # ελέγχει τη θέση που έγινε click
    def on_canvas_click(self, event, col_array, coord_list):
        x, y = event.x, event.y
        counter = 0
        for button in col_array:
            coord_list_copy = coord_list[counter]
            if self.is_within_button(x, y, coord_list_copy):
                if self.game_mode == "pvp":
                    self.pvp_button_clicked(button)
                elif self.game_mode == "pve":
                    self.pve_button_clicked(button)
            counter += 1
        self.on_mouse_move(event, col_array, coord_list)

    # click σε pvp
    def pvp_button_clicked(self, button_id):
        self.play_pvp(button_id)

    # click σε pve
    def pve_button_clicked(self, button_id):
        self.play_pve(button_id)

    # εμφανίζει το ποντίκι όταν βρίσκεται πάνω στα κουμπιά στηλών
    # αν βρίσκεται μέσα σε συγκεκριμένες συντεταγμένες εμφανίζεται η εικόνα
    # αλλιώς εξαφανίζεται
    def on_mouse_move(self, event, col_array, coord_list):
        x, y = event.x, event.y
        if 90 < x < 680 and 10 < y < 120:
            counter = 0
            for button in col_array:
                coord_list_copy = coord_list[counter]
                if self.is_within_button(x, y, coord_list_copy):
                    image_item = self.image_items[counter]
                    if self.turn == 1:
                        image = self.images[counter]
                        image.configure(file="red.png")
                        self.canvas.itemconfigure(image_item, state="normal", image=image)
                    elif self.turn == 2:
                        image = self.images[counter]
                        image.configure(file="yellow.png")
                        self.canvas.itemconfigure(image_item, state="normal", image=image)
                else:
                    image_item = self.image_items[counter]
                    self.canvas.itemconfigure(image_item, state="hidden")
                counter += 1
        else:
            for counter in range(len(col_array)):
                image_item = self.image_items[counter]
                self.canvas.itemconfigure(image_item, state="hidden")

#------------------------------------------Game Mode ------------------------------------------------------------------
    # παίζει ο παίκτης και γίνεται έλεγχος για νικητή
    def play_pvp(self, user_choice):
        if self.can_play:
            self.can_play = False
            row = self.game.player_turn(self.turn, user_choice)
            if row != -1:
                self.animate(row, user_choice)
                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
            else:
                self.can_play = True
            self.check_won()
            self.can_play = True

    # παίζει ο παίκτης, ο υπολογιστής και γίνεται έλεγχος για νικητή
    def play_pve(self, user_choice):
        if self.can_play:
            self.can_play = False
            row = self.game.player_turn(self.turn, user_choice)
            if row != -1:
                self.animate(row, user_choice)
                self.turn = 2
            else:
                self.can_play = True
            self.check_won()
            # επιλογή υπολογιστή
            self.make_bot_turn()
            self.check_won()

    # έλεγχος για νικητή ή ισοπαλία
    def check_won(self):
        self.won = self.game.game_over()
        if self.won:
            self.upd_db()
            self.end_screen()

     # κίνηση υπολογιστή
    def make_bot_turn(self):
        if not self.can_play:
            if self.difficulty:
                bot_row, bot_col = self.game.computer_turn("3")
            else:
                bot_row, bot_col = self.game.computer_turn("1")
            self.animate(bot_row, bot_col)
            self.turn = 1
            self.can_play = True

    # ενημέρωση DataBase
    def upd_db(self):
        self.game.update_stats()
        self.db.update_table(self.game.player1)
        if self.username2 is not None:
            self.db.update_table(self.game.player2)

    # εφέ κύλισης για τα πιόνια που τοποθετούνται
    # αλλάζει διαδοχικά τις εικόνες απο λευκό σε κόκκινο ή κίτρινο
    # και πάλι σε λευκό, μέχρι να φτάσει στη θέση του
    def animate(self, row, col):
        if row != 0:
            for buttons in range(0, row - 1):
                button = self.button_array[buttons][col]
                if self.turn == 1:
                    button.config(image=self.img_array[1])
                else:
                    button.config(image=self.img_array[2])
                self.tksleep(0.15)
                button.config(image=self.img_array[0])
            for buttons in range(0, row - 1):
                button = self.button_array[buttons][col]
                if self.game.grid[buttons][col] == self.turn:
                    if self.turn == 1:
                        button.config(image=self.img_array[1])
                    else:
                        button.config(image=self.img_array[2])
        button = self.button_array[row][col]
        if self.turn == 1:
            button.config(image=self.img_array[1])
        else:
            button.config(image=self.img_array[2])

    # χρονοκαθυστέρηση για την εναλλαγή των εικόνων
    # (παύση στην εκτέλεση του προγράμματος)
    def tksleep(self, t):
        ms = int(t * 1000)
        root = tk._get_default_root()
        var = tk.IntVar(root)
        root.after(ms, lambda: var.set(1))
        root.wait_variable(var)

# ------------------------------------end screen -----------------------------------------------------------------
    # εμφάνιση νικητή ή ισοπαλίας και επιλογή επιστροφής στο Main Menu
    def end_screen(self):
        self.canvas.delete("all")
        self.canvas.destroy()
        self.canvas = Canvas(self, width=1280, height=640)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        if self.won == 3:
            self.canvas.create_text(632, 250, text=f"Draw", font=font_fam3, anchor="center", fill="black")
        elif self.won == 2:
            if self.username2 is None:
                self.canvas.create_text(632, 250, text=f"You Lose!", font=font_fam3, anchor="center", fill="black")
            else:
                self.canvas.create_text(632, 220, text=f"Winner:", font=font_fam3, anchor="center", fill="black")
                self.canvas.create_text(632, 320, text=f"{self.username2}", font=font_fam4, anchor="center", fill="black")
        else:
            self.canvas.create_text(632, 220, text=f"Winner:", font=font_fam3, anchor="center", fill="black")
            self.canvas.create_text(632, 320, text=f"{self.username}", font=font_fam4, anchor="center", fill="black")

        main_button = tk.Button(self, text='Main Menu', width=12, command=self.main_menu, font=font_fam)
        self.canvas.create_window(552, 380, anchor="nw", window=main_button)
        exit_button = tk.Button(self, text='Exit', width=12, command=self.exit, font=font_fam)
        self.canvas.create_window(552, 440, anchor="nw", window=exit_button)
        self.mainloop()

    # κλείνει το παράθυρο και ανοίγει νέο
    # (επιστροφή στο main menu)
    def main_menu(self):
        self.destroy()
        App()

    # έξοδος από την εφαρμογή
    def exit(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.db.close_db()
        self.destroy()


if __name__ == "__main__":
    new_app = App()
    new_app.mainloop()
