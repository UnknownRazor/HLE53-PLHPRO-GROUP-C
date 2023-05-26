import tkinter as tk
from PIL import Image, ImageTk
from game import *
from player import Player

ROWS = 6
COLUMNS = 7
MAX_ROW = 10
MAX_COL = 10
lbl_font = ("Courier", 24, "bold")
btn_font = ("Courier", 12, "bold")
stats_font = ("Courier", 12, "bold", "underline")
boxes_font = ("Courier", 10, "bold")
blue_bg = "#3061E3"
red_bg = "#da2528"
yellow_bg = "#ffd700"

class Connect4(tk.Tk):
    def __init__(self):
        super().__init__()

        # δημιουργία παραθύρου
        self.title("Connect 4")
        self.iconbitmap("4.ico")
        self.geometry("490x475")
        self.resizable(width=False, height=False)

        # Δημιουργία Frames (μενού + υπο-μενού)
        self.main_frame = MainFrame(self)   # main menu
        self.size_frame = SizeFrame(self)   # μέγεθος ταμπλό
        # self.custom_frame = CustomFrame(self)   # δημιουργία ταμπλό
        self.vs_frame = VsFrame(self)       # pvp - pve
        self.name_frame1 = NameFrame1(self) # όνομα παίκτη 1
        self.name_frame2 = NameFrame2(self) # όνομα παίκτη 1 & 2
        self.level_frame = LevelFrame(self) # menu επιπέδου δυσκολίας
        self.pvp_frame = PvPFrame(self)  # ταμπλό pvp
        self.pveasy_frame = PvEasyFrame(self)  # ταμπλό pvp easy
        self.pvhard_frame = PvHardFrame(self)  # ταμπλό pvp hard
        self.rank_frame = RankFrame(self)   # κατάταξη
        self.win_frame = WinFrame(self)  # 1ος νικητής
        self.win_frame2 = WinFrame2(self)  # 2ος νικητής
        self.win_frame3 = WinFrame3(self)  # ισοπαλία

        # Τοποθέτηση των frames στο παράθυρο
        all_frames = (self.main_frame, self.size_frame, self.vs_frame, self.name_frame1,
                      self.name_frame2, self.level_frame, self.pvp_frame, self.pveasy_frame, self.pvhard_frame,
                      self.rank_frame, self.win_frame, self.win_frame2, self.win_frame3)
        for frame in all_frames:
            frame.pack(fill=tk.BOTH, expand=True)

        # εμφάνιση αρχικού frame
        self.show_frame(self.main_frame)


    def show_frame(self, frame):
        # κρύβει όλα τα frames και εμφανίζει αυτό που παίρνει σαν όρισμα
        all_frames = (self.main_frame, self.size_frame, self.vs_frame, self.name_frame1,
                      self.name_frame2, self.level_frame, self.pvp_frame, self.pveasy_frame, self.pvhard_frame,
                      self.rank_frame, self.win_frame, self.win_frame2, self.win_frame3)
        for f in all_frames:
            f.pack_forget()
        frame.pack(fill=tk.BOTH, expand=True)


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.main_label = tk.Label(self, padx=50, pady=40, text="Main Menu")
        self.main_label.configure(font=lbl_font, background=blue_bg)

        # δημιουργία κουμπιών
        self.play_btn = tk.Button(self, padx=100, pady=10, text="Play",
                                  command=lambda: master.show_frame(master.size_frame))
        self.play_btn.configure(font=btn_font, background=red_bg)
        self.rank_btn = tk.Button(self, padx=100, pady=10, text="Rank",
                                  command=lambda: master.show_frame(master.rank_frame))
        self.rank_btn.configure(font=btn_font, background=yellow_bg)
        self.exit_btn = tk.Button(self, padx=100, pady=10, text="Exit",
                                  command=self.exit)
        self.exit_btn.configure(font=btn_font, background=red_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.main_label.pack()
        self.play_btn.pack()
        self.rank_btn.pack()
        self.exit_btn.pack()

    def exit(self):
        self.master.destroy()


class SizeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.size_label = tk.Label(self, padx=50, pady=40, text="Table Size")
        self.size_label.configure(font=lbl_font, background=blue_bg)
        # δημιουργία κουμπιών μενού
        self.preset_btn = tk.Button(self, padx=70, pady=10, text="Preset (6x7)",
                                    command=lambda: master.show_frame(master.vs_frame))
        self.preset_btn.configure(font=btn_font, background=red_bg)
        self.custom_btn = tk.Button(self, padx=100, pady=10, text="Custom",
                                    command=lambda: master.show_frame(master.custom_frame), state="disabled")
        self.custom_btn.configure(font=btn_font, background=yellow_bg)
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.main_frame))
        self.back_btn.configure(font=btn_font, background=red_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.size_label.pack()
        self.preset_btn.pack()
        self.custom_btn.pack()
        self.back_btn.pack()

### Δυναμική δημιουργία ταμπλό --------------------------------------------------------------
# class CustomFrame(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master, bg=blue_bg)
#
#         # δημιουργία κεφαλίδας
#         self.custom_label = tk.Label(self, padx=50, pady=40, text="Custom Table")
#         self.custom_label.configure(font=lbl_font, background=blue_bg)
#         # δημιουργία κουμπιών & πεδίων εισαγωγής γραμμών/στηλών
#         self.row_label = tk.Label(self, padx=50, pady=10, text="Rows (5 - 10)")
#         self.row_label.configure(font=btn_font, background=red_bg)
#         self.column_label = tk.Label(self, padx=35, pady=10, text="Columns (5 - 10)")
#         self.column_label.configure(font=btn_font, background=red_bg)
#         self.row_entry = tk.Entry(self, font=btn_font, width=5)
#         self.column_entry = tk.Entry(self, font=btn_font, width=5)
#         self.ok_btn = tk.Button(self, padx=40, pady=10, text="OK", command=self.save_size)
#         # self.ok_btn = tk.Button(self, padx=40, pady=10, text="OK",
#         #                         command=lambda: master.show_frame(master.vs_frame))
#         self.ok_btn.configure(font=btn_font, background=yellow_bg)
#         self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
#                                    command=lambda: master.show_frame(master.size_frame))
#         self.back_btn.configure(font=btn_font, background=red_bg)
#
#         # τοποθέτηση widgets στο παράθυρο
#         self.pack(fill=tk.BOTH, expand=True)
#         self.custom_label.pack()
#         self.row_label.pack()
#         self.row_entry.pack(pady=10)
#         self.column_label.pack()
#         self.column_entry.pack(pady=10)
#         self.ok_btn.pack()
#         self.back_btn.pack()
#
#     def save_size(self):
#         new_game.rows = int(self.row_entry.get())
#         new_game.columns = int(self.column_entry.get())
#         new_game.grid = new_game.create_grid(new_game.rows, new_game.columns)
#         print("Entry 1:", new_game.rows)
#         print("Entry 2:", new_game.columns)
#         self.master.show_frame(self.master.vs_frame)


class VsFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.vs_label = tk.Label(self, padx=50, pady=40, text="VS")
        self.vs_label.configure(font=lbl_font, background=blue_bg)
        # δημιουργία κουμπιών μενού
        self.pve_btn = tk.Button(self, padx=60, pady=10, text="Person VS Computer",
                                 command=lambda: master.show_frame(master.name_frame1))
        self.pve_btn.configure(font=btn_font, background=red_bg)
        self.pvp_btn = tk.Button(self, padx=70, pady=10, text="Person VS Person",
                                    command=lambda: master.show_frame(master.name_frame2))
        self.pvp_btn.configure(font=btn_font, background=yellow_bg)
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.main_frame))
        self.back_btn.configure(font=btn_font, background=red_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.vs_label.pack()
        self.pve_btn.pack()
        self.pvp_btn.pack()
        self.back_btn.pack()


class NameFrame1(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.name1_label = tk.Label(self, padx=50, pady=40, text="Insert Name")
        self.name1_label.configure(font=lbl_font, background=blue_bg)
        # δημιουργία κουμπιών μενού
        self.player_label = tk.Label(self, padx=35, pady=10, text="Player")
        self.player_label.configure(font=btn_font, background=red_bg)
        self.name_entry = tk.Entry(self, font=btn_font, width=10)
        self.ok_btn = tk.Button(self, padx=40, pady=10, text="OK", command=self.save_name)
        self.ok_btn.configure(font=btn_font, background=yellow_bg)
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.vs_frame))
        self.back_btn.configure(font=btn_font, background=red_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.name1_label.pack()
        self.player_label.pack()
        self.name_entry.pack(pady=10)
        self.ok_btn.pack()
        self.back_btn.pack()

    # εισάγει τον παίκτη στο Database εφόσον δεν υπάρχει
    def save_name(self):
        name = self.name_entry.get()
        new_game.player1 = Player(name)
        db.insert_table(new_game.player1)
        self.master.show_frame(self.master.level_frame)


class NameFrame2(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.name2_label = tk.Label(self, padx=50, pady=40, text="Insert Names")
        self.name2_label.configure(font=lbl_font, background=blue_bg)
        # δημιουργία κουμπιών μενού
        self.first_label = tk.Label(self, padx=35, pady=10, text="Player 1")
        self.first_label.configure(font=btn_font, background=red_bg)
        self.name1_entry = tk.Entry(self, font=btn_font, width=10)
        self.second_label = tk.Label(self, padx=35, pady=10, text="Player 2")
        self.second_label.configure(font=btn_font, background=yellow_bg)
        self.name2_entry = tk.Entry(self, font=btn_font, width=10)
        self.ok_btn = tk.Button(self, padx=40, pady=10, text="OK", command=self.save_names)
        self.ok_btn.configure(font=btn_font, background=red_bg)
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.vs_frame))
        self.back_btn.configure(font=btn_font, background=yellow_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.name2_label.pack()
        self.first_label.pack()
        self.name1_entry.pack(pady=10)
        self.second_label.pack()
        self.name2_entry.pack(pady=10)
        self.ok_btn.pack()
        self.back_btn.pack()

    # εισάγει τους παίκτες στο Database εφόσον δεν υπάρχουν
    def save_names(self):
        name1 = self.name1_entry.get()
        new_game.player1 = Player(name1)
        db.insert_table(new_game.player1)
        name2 = self.name2_entry.get()
        new_game.player2 = Player(name2)
        db.insert_table(new_game.player2)
        self.master.show_frame(self.master.pvp_frame)


class LevelFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.level_label = tk.Label(self, padx=50, pady=40, text="Level")
        self.level_label.configure(font=lbl_font, background=blue_bg)

        # δημιουργία κουμπιών
        self.easy_btn = tk.Button(self, padx=100, pady=10, text="Easy",
                                  command=lambda: master.show_frame(master.pveasy_frame))
        self.easy_btn.configure(font=btn_font, background=yellow_bg)
        # self.normal_btn = tk.Button(self, padx=90, pady=10, text="Normal",
        #                           command=lambda: master.show_frame(master.pve_frame))
        # self.normal_btn.configure(font=btn_font, background=yellow_bg)
        self.hard_btn = tk.Button(self, padx=100, pady=10, text="Hard",
                                    command=lambda: master.show_frame(master.pvhard_frame))
        self.hard_btn.configure(font=btn_font, background=red_bg)
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                  command=lambda: master.show_frame(master.vs_frame))
        self.back_btn.configure(font=btn_font, background=yellow_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.level_label.pack()
        self.easy_btn.pack()
        # self.normal_btn.pack()
        self.hard_btn.pack()
        self.back_btn.pack()


class PvPFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='blue')
        self.row_input = new_game.rows
        self.col_input = new_game.columns
        self.grid = [[0 for _ in range(self.row_input)] for _ in range(self.col_input)]
        self.turn = 1  # 1: κόκκινο / -1: κίτρινο

        # κενά πιόνια
        self.white = Image.open("white.jpg")
        self.white = ImageTk.PhotoImage(self.white)
        # κόκκινα πιόνια
        self.red = Image.open("red.jpg")
        self.red = ImageTk.PhotoImage(self.red)
        # κίτρινα πιόνια
        self.yellow = Image.open("yellow.jpg")
        self.yellow = ImageTk.PhotoImage(self.yellow)

        # δυναμική δημιουργία κουμπιών στηλών
        # lambda k=i+1 : κρατάει την τιμή του i στο j, σε κάθε Loop
        # χωρίς το k, όλα τα κουμπιά παίρνουν την τιμή του i στο τέλος του loop
        self.col_btn_list = []
        for i in range(self.col_input):
            col_btn = tk.Button(self, text=str(i + 1), padx=23, pady=10,
                                command=lambda k=i + 1: self.click_col(k))
            col_btn.configure(font=btn_font, background=blue_bg)
            col_btn.grid(row=0, column=i)
            self.col_btn_list.append(col_btn)

        # λίστα με πλήθος γεμάτων κελιών ανά στήλη
        # θέση = στήλη / τιμή = τρέχουσα κενή γραμμή
        # αρχικοποίηση στη 7η γραμμή (όλες οι θέσεις κενές)
        self.current_row = []
        for i in range(self.col_input + 1):
            self.current_row.append(7)

        self.create_grid()

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)

    # δημιουργία κενού ταμπλό
    def create_grid(self):
        for i in range(1, self.row_input + 1):
            for j in range(self.col_input):
                box_label = tk.Label(self, image=self.white, borderwidth=0, highlightthickness=0)
                box_label.grid(row=i, column=j)

    def play_red(self, col):
        box_label = tk.Label(self, image=self.red, borderwidth=0, highlightthickness=0)
        box_label.grid(row=self.current_row[col] - 1, column=col - 1)

    def play_yellow(self, col):
        box_label = tk.Label(self, image=self.yellow, borderwidth=0, highlightthickness=0)
        box_label.grid(row=self.current_row[col] - 1, column=col - 1)

    # Επιλογή στήλης από τους παίκτες εναλλάξ (pvp)
    def click_col(self, col):
        # αν δεν είναι γεμάτη η στήλη
        # τοποθετεί το πιόνι στην κατώτερη θέση
        # αλλιώς εμφανίζει ανάλογο μήνυμα
        if self.current_row[col] != 1:
            # οι παίκτες παίζουν εναλλάξ
            if self.turn == 1:
                self.play_red(col)
                new_game.player_turn(1, col)
                for row in new_game.grid:
                    print(row)
                if new_game.game_over(new_game.grid):
                    # εμφάνιση νικητή
                    print(new_game.message)
                    self.update_db()
                    self.winner_display(new_game.result)
            else:
                self.play_yellow(col)
                new_game.player_turn(2, col)
                for row in new_game.grid:
                    print(row)
                if new_game.game_over(new_game.grid):
                    # εμφάνιση νικητή
                    print(new_game.message)
                    self.update_db()
                    self.winner_display(new_game.result)
            self.turn *= -1
            self.current_row[col] -= 1
        else:  # γεμάτη στήλη, απενεργοποίηση κουμπιού
            self.col_btn_list[col - 1]['state'] = 'disabled'

    # ενημέρωση Database
    def update_db(self):
        new_game.update_stats()
        db.update_table(new_game.player1)
        db.update_table(new_game.player2)

    # εμφανίζει το frame με το αποτέλεσμα
    def winner_display(self, winner):
        if winner == 1:
            self.master.show_frame(self.master.win_frame)
        elif winner == 2:
            self.master.show_frame(self.master.win_frame2)
        else:
            self.master.show_frame(self.master.win_frame3)


class PvEasyFrame(PvPFrame):
    def __init__(self, master):
        super().__init__(master)

    # επιλογή στήλης από παίκτη και υπολογιστή εναλλάξ
    def click_col(self, col):
        # αν δεν είναι γεμάτη η στήλη
        # τοποθετεί το πιόνι στην κατώτερη θέση
        # αλλιώς εμφανίζει ανάλογο μήνυμα
        if self.current_row[col] != 1:
            # παίζει ο παίκτης
            if self.turn == 1:
                self.play_red(col)
                new_game.player_turn(1, col)
                for row in new_game.grid:
                    print(row)
                print(30 * "-")
                if new_game.game_over(new_game.grid):
                    # εμφάνιση νικητή
                    print(new_game.message)
                    self.update_db()
                    self.winner_display(new_game.result)
                self.turn *= -1
                self.current_row[col] -= 1
        else:  # γεμάτη στήλη, απενεργοποίηση κουμπιού
            self.col_btn_list[col - 1]['state'] = 'disabled'

        if self.turn == -1:
            # παίζει το bot
            col = new_game.computer_turn("1")
            self.play_yellow(col + 1)
            for row in new_game.grid:
                print(row)
            print(30 * "-")
            if new_game.game_over(new_game.grid):
                # εμφάνιση νικητή
                print(new_game.message)
                self.update_db()
                self.winner_display(new_game.result)
            self.turn *= -1
            self.current_row[col + 1] -= 1
        print(self.current_row)


class PvHardFrame(PvPFrame):
    def __init__(self, master):
        super().__init__(master)
            
    # επιλογή στήλης από παίκτη και υπολογιστή εναλλάξ
    def click_col(self, col):
        # αν δεν είναι γεμάτη η στήλη
        # τοποθετεί το πιόνι στην κατώτερη θέση
        # αλλιώς εμφανίζει ανάλογο μήνυμα
        if self.current_row[col] != 1:
            # παίζει ο παίκτης
            if self.turn == 1:
                self.play_red(col)
                new_game.player_turn(1, col)
                for row in new_game.grid:
                    print(row)
                print(30 * "-")
                if new_game.game_over(new_game.grid):
                    # εμφάνιση νικητή
                    print(new_game.message)
                    self.update_db()
                    self.winner_display(new_game.result)
                self.turn *= -1
                self.current_row[col] -= 1
        else:  # γεμάτη στήλη, απενεργοποίηση κουμπιού
            self.col_btn_list[col - 1]['state'] = 'disabled'

        if self.turn == -1:
            # παίζει το bot
            col = new_game.computer_turn("3")
            self.play_yellow(col+1)
            for row in new_game.grid:
                print(row)
            print(30*"-")
            if new_game.game_over(new_game.grid):
                # εμφάνιση νικητή
                print(new_game.message)
                self.update_db()
                self.winner_display(new_game.result)
            self.turn *= -1
            self.current_row[col+1] -= 1
        print(self.current_row)


class WinFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.win_label = tk.Label(self, padx=50, pady=40, text="Player 1 Wins")
        self.win_label.configure(font=lbl_font, background=blue_bg)

        # δημιουργία κουμπιών
        self.mm_btn = tk.Button(self, padx=50, pady=10, text="Main Menu",
                                  command=self.play_again)
        self.mm_btn.configure(font=btn_font, background=yellow_bg)
        self.exit_btn = tk.Button(self, padx=50, pady=10, text="Exit",
                                  command=self.master.destroy)
        self.exit_btn.configure(font=btn_font, background=red_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.win_label.pack()
        self.mm_btn.pack()
        self.exit_btn.pack()

    # κλείνει το παράθυρο και ανοίγει καινούριο
    def play_again(self):
        global new_game
        new_game = Game()
        self.master.destroy()
        Connect4()

class WinFrame2(WinFrame):
    def __init__(self, master):
        super().__init__(master)
        self.win_label.configure(text="Player 2 Wins")

class WinFrame3(WinFrame):
    def __init__(self, master):
        super().__init__(master)
        self.win_label.configure(text="Draw")


class RankFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        self.name = tk.Label(self, padx=20, pady=10, text='Name')
        self.name.configure(font=stats_font, background=blue_bg)
        self.games = tk.Label(self, padx=15, pady=10, text='Games')
        self.games.configure(font=stats_font, background=blue_bg)
        self.wins = tk.Label(self, padx=15, pady=10, text='Wins')
        self.wins.configure(font=stats_font, background=blue_bg)
        self.losses = tk.Label(self, padx=15, pady=10, text='Losses')
        self.losses.configure(font=stats_font, background=blue_bg)
        self.draws = tk.Label(self, padx=15, pady=10, text='Draws')
        self.draws.configure(font=stats_font, background=blue_bg)
        self.elo = tk.Label(self, padx=15, pady=10, text='ELO')
        self.elo.configure(font=stats_font, background=blue_bg)
        self.back_btn = tk.Button(self, padx=30, pady=10, text="BACK",
                                  command=lambda: master.show_frame(master.main_frame))
        self.back_btn.configure(font=btn_font, background=red_bg)

        # ταξινομημένοι παίκτες σύμφωνα με elo (πρώτοι 10)
        top_players = db.top_10()

        # τοποθέτηση widgets στο παράθυρο
        i = 1
        for pl in top_players:
            for j in range(len(pl)):
                box = tk.Label(self, padx=15, pady=10, text=pl[j])
                box.configure(font=boxes_font, background=blue_bg)
                box.grid(row=i, column=j)
            i = i + 1

        self.pack(fill=tk.BOTH, expand=True)
        self.name.grid(row=0, column=0)
        self.games.grid(row=0, column=1)
        self.wins.grid(row=0, column=2)
        self.losses.grid(row=0, column=3)
        self.draws.grid(row=0, column=4)
        self.elo.grid(row=0, column=5)
        self.back_btn.grid(row=12, column=4, columnspan=2)


db = DataBase()
new_game = Game()
app = Connect4()
app.mainloop()
db.close_db()