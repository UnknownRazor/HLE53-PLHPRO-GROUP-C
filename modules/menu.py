import tkinter as tk
from PIL import Image, ImageTk
from game import *

ROWS = 6
COLUMNS = 7
MAX_ROW = 10
MAX_COL = 10
lbl_font = ("Courier", 24, "bold")
btn_font = ("Courier", 12, "bold")
stats_font = ("Courier", 14, "bold", "underline")
boxes_font = ("Courier", 12, "bold")
blue_bg = "#3061E3"
red_bg = "#da2528"
yellow_bg = "#ffd700"

class Connect4(tk.Tk):
    def __init__(self):
        super().__init__()

        # δημιουργία παραθύρου
        self.title("Connect 4")
        #self.iconbitmap("4.ico")
        self.geometry("600x550")
        self.resizable(width=False, height=False)

        # Δημιουργία Frames (μενού + υπο-μενού)
        self.main_frame = MainFrame(self)   # main menu
        self.size_frame = SizeFrame(self)   # μέγεθος ταμπλό
        self.custom_frame = CustomFrame(self)   # δημιουργία ταμπλό
        self.vs_frame = VsFrame(self)       # pvp - pve
        self.name1_frame = Name1Frame(self) # όνομα παίκτη 1
        self.name2_frame = Name2Frame(self) # όνομα παίκτη 1 & 2
        self.level_frame = LevelFrame(self) # menu επιπέδου δυσκολίας
        self.table_frame = TableFrame(self)  # ταμπλό
        self.rank_frame = RankFrame(self)   # κατάταξη
        self.win_frame = WinFrame(self, 1)  # νικητής

        # Τοποθέτηση των frames στο παράθυρο
        all_frames = (self.main_frame, self.size_frame, self.custom_frame, self.vs_frame, self.name1_frame,
                      self.name2_frame, self.level_frame, self.table_frame, self.rank_frame, self.win_frame)
        for frame in all_frames:
            frame.pack(fill=tk.BOTH, expand=True)

        # εμφάνιση αρχικού frame
        self.show_frame(self.main_frame)


    def show_frame(self, frame):
        # κρύβει όλα τα frames και εμφανίζει αυτό που παίρνει σαν όρισμα
        all_frames = (self.main_frame, self.size_frame, self.custom_frame, self.vs_frame, self.name1_frame,
                      self.name2_frame, self.level_frame, self.table_frame, self.rank_frame, self.win_frame)
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
                                    command=lambda: master.show_frame(master.custom_frame))
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


class CustomFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.custom_label = tk.Label(self, padx=50, pady=40, text="Custom Table")
        self.custom_label.configure(font=lbl_font, background=blue_bg)
        # δημιουργία κουμπιών & πεδίων εισαγωγής γραμμών/στηλών
        self.row_label = tk.Label(self, padx=50, pady=10, text="Rows (5 - 10)")
        self.row_label.configure(font=btn_font, background=red_bg)
        self.column_label = tk.Label(self, padx=35, pady=10, text="Columns (5 - 10)")
        self.column_label.configure(font=btn_font, background=red_bg)
        # self.row_entry = tk.Entry(self, font=btn_font, width=5)
        # self.column_entry = tk.Entry(self, font=btn_font, width=5)
        self.btnR5 = tk.Button(self, padx=10, pady=10, text="5", font=btn_font, background=yellow_bg)

        self.btnR6 = tk.Button(self, padx=10, pady=10, text="6")
        self.btnR6.configure(font=btn_font, background=yellow_bg)
        self.btnR7 = tk.Button(self, padx=10, pady=10, text="7")
        self.btnR7.configure(font=btn_font, background=yellow_bg)
        self.btnR8 = tk.Button(self, padx=10, pady=10, text="8")
        self.btnR8.configure(font=btn_font, background=yellow_bg)
        self.btnR9 = tk.Button(self, padx=10, pady=10, text="9")
        self.btnR9.configure(font=btn_font, background=yellow_bg)
        self.btnR10 = tk.Button(self, padx=10, pady=10, text="10")
        self.btnR10.configure(font=btn_font, background=yellow_bg)

        self.btnC5 = tk.Button(self, padx=10, pady=10, text="5")
        self.btnC5.configure(font=btn_font, background=yellow_bg)
        self.btnC6 = tk.Button(self, padx=10, pady=10, text="6")
        self.btnC6.configure(font=btn_font, background=yellow_bg)
        self.btnC7 = tk.Button(self, padx=10, pady=10, text="7")
        self.btnC7.configure(font=btn_font, background=yellow_bg)
        self.btnC8 = tk.Button(self, padx=10, pady=10, text="8")
        self.btnC8.configure(font=btn_font, background=yellow_bg)
        self.btnC9 = tk.Button(self, padx=10, pady=10, text="9")
        self.btnC9.configure(font=btn_font, background=yellow_bg)
        self.btnC10 = tk.Button(self, padx=10, pady=10, text="10")
        self.btnC10.configure(font=btn_font, background=yellow_bg)

        self.ok_btn = tk.Button(self, padx=40, pady=10, text="OK",
                                command=lambda: master.show_frame(master.vs_frame))
        self.ok_btn.configure(font=btn_font, background=yellow_bg)
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.size_frame))
        self.back_btn.configure(font=btn_font, background=red_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.custom_label.pack()
        self.row_label.pack(side='left')
        self.btnR5.pack(side='left')
        self.btnR6.pack(side='left')
        self.btnR7.pack(side='left')
        self.btnR8.pack(side='left')
        self.btnR9.pack(side='left')
        self.btnR10.pack(side='left')
        # self.row_entry.pack(pady=10)
        self.column_label.pack(side='right')
        self.btnC5.pack(side='right')
        self.btnC6.pack(side='right')
        self.btnC7.pack(side='right')
        self.btnC8.pack(side='right')
        self.btnC9.pack(side='right')
        self.btnC10.pack(side='right')
        # self.column_entry.pack(pady=10)
        self.ok_btn.pack()
        self.back_btn.pack()

    def save_size(self):
        pass

class VsFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.vs_label = tk.Label(self, padx=50, pady=40, text="VS")
        self.vs_label.configure(font=lbl_font, background=blue_bg)
        # δημιουργία κουμπιών μενού
        self.pvp_btn = tk.Button(self, padx=70, pady=10, text="Person VS Person",
                                    command=lambda: master.show_frame(master.name2_frame))
        self.pvp_btn.configure(font=btn_font, background=red_bg)
        self.pve_btn = tk.Button(self, padx=60, pady=10, text="Person VS Computer",
                                    command=lambda: master.show_frame(master.name1_frame))
        self.pve_btn.configure(font=btn_font, background=yellow_bg)
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.main_frame))
        self.back_btn.configure(font=btn_font, background=red_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.vs_label.pack()
        self.pvp_btn.pack()
        self.pve_btn.pack()
        self.back_btn.pack()

class Name1Frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.name1_label = tk.Label(self, padx=50, pady=40, text="Insert Name")
        self.name1_label.configure(font=lbl_font, background=blue_bg)
        # δημιουργία κουμπιών μενού
        self.player_label = tk.Label(self, padx=35, pady=10, text="Player")
        self.player_label.configure(font=btn_font, background=red_bg)
        self.name_entry = tk.Entry(self, font=btn_font, width=10)
        self.ok_btn = tk.Button(self, padx=40, pady=10, text="OK",
                                command=lambda: master.show_frame(master.table_frame))
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

    def save_name(self):
        pass

class Name2Frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.name2_label = tk.Label(self, padx=50, pady=40, text="Insert Names")
        self.name2_label.configure(font=lbl_font, background=blue_bg)
        # δημιουργία κουμπιών μενού
        self.first_label = tk.Label(self, padx=35, pady=10, text="Player 1")
        self.first_label.configure(font=btn_font, background=red_bg)
        self.first_entry = tk.Entry(self, font=btn_font, width=10)
        self.second_label = tk.Label(self, padx=35, pady=10, text="Player 2")
        self.second_label.configure(font=btn_font, background=yellow_bg)
        self.second_entry = tk.Entry(self, font=btn_font, width=10)
        self.ok_btn = tk.Button(self, padx=40, pady=10, text="OK",
                                command=lambda: master.show_frame(master.table_frame))
        self.ok_btn.configure(font=btn_font, background=red_bg)
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.vs_frame))
        self.back_btn.configure(font=btn_font, background=yellow_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.name2_label.pack()
        self.first_label.pack()
        self.first_entry.pack(pady=10)
        self.second_label.pack()
        self.second_entry.pack(pady=10)
        self.ok_btn.pack()
        self.back_btn.pack()

    def save_name(self):
        pass

class LevelFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)

        # δημιουργία κεφαλίδας
        self.level_label = tk.Label(self, padx=50, pady=40, text="Level")
        self.level_label.configure(font=lbl_font, background=blue_bg)

        # δημιουργία κουμπιών
        self.easy_btn = tk.Button(self, padx=100, pady=10, text="easy",
                                  command=lambda: master.show_frame(master.table_frame))
        self.easy_btn.configure(font=btn_font, background=red_bg)
        self.normal_btn = tk.Button(self, padx=100, pady=10, text="Normal",
                                  command=lambda: master.show_frame(master.table_frame))
        self.normal_btn.configure(font=btn_font, background=yellow_bg)
        self.hard_btn = tk.Button(self, padx=100, pady=10, text="Hard",
                                    command=lambda: master.show_frame(master.table_frame))
        self.hard_btn.configure(font=btn_font, background=red_bg)
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                  command=lambda: master.show_frame(master.vs_frame))
        self.back_btn.configure(font=btn_font, background=yellow_bg)

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.level_label.pack()
        self.easy_btn.pack()
        self.normal_btn.pack()
        self.hard_btn.pack()
        self.back_btn.pack()


class TableFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='blue')
        self.row_input = ROWS
        self.col_input = COLUMNS
        self.grid = [[0 for _ in range(self.row_input)] for _ in range(self.col_input)]
        self.turn = 1  # 1: κόκκινο / -1: κίτρινο
        self.new_game = Game()


        # δημιουργία κεφαλίδας
        self.vs_label = tk.Label(self, padx=50, pady=40, text="Table Size")
        self.vs_label.configure(font=lbl_font, background=blue_bg)

        # κενά πιόνια
        self.white = Image.open("../assets/white.png")
        self.white = ImageTk.PhotoImage(self.white)
        # κόκκινα πιόνια
        self.red = Image.open("../assets/red.png")
        self.red = ImageTk.PhotoImage(self.red)
        # κίτρινα πιόνια
        self.yellow = Image.open("../assets/yellow.png")
        self.yellow = ImageTk.PhotoImage(self.yellow)

        # δυναμική δημιουργία κουμπιών στηλών
        # lambda j=i+1 : κρατάει την τιμή του i στο j, σε κάθε Loop
        # χωρίς το j, όλα τα κουμπιά παίρνουν την τιμή του i στο τέλος του loop
        self.col_btn_list = []
        for i in range(self.col_input):
            col_btn = tk.Button(self, text=str(i + 1), padx=16, pady=10,
                                command=lambda k=i + 1: self.click_col(k))
            col_btn.configure(font=btn_font, background=red_bg)
            col_btn.grid(row=0, column=i)
            self.col_btn_list.append(col_btn)

        # λίστα με πλήθος γεμάτων κελιών ανά στήλη
        # θέση = στήλη / τιμή = τρέχουσα κενή γραμμή
        # αρχικοποίηση στην 7η γραμμή (όλες οι θέσεις κενές)
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

    # pvp
    def click_col(self, col):
        # αν δεν είναι γεμάτη η στήλη
        # τοποθετεί το πιόνι στην κατώτερη θέση
        # αλλιώς εμφανίζει ανάλογο μήνυμα
        if self.current_row[col] != 1:
            # οι παίκτες παίζουν εναλλάξ
            if self.turn == 1:
                self.play_red(col)
                self.new_game.player_turn(1, col)
                for row in self.new_game.grid:
                    print(row)
                if self.new_game.game_over():
                    # εμφάνιση νικητή
                    print(self.new_game.game_over())
                    self.master.show_frame(self.master.win_frame)
            else:
                self.play_yellow(col)
                self.new_game.player_turn(2, col)
                for row in self.new_game.grid:
                    print(row)
                if self.new_game.game_over():
                    # εμφάνιση νικητή
                    print(self.new_game.game_over())
                    self.master.show_frame(self.master.win_frame)
            self.turn *= -1
            self.current_row[col] -= 1
        else:  # γεμάτη στήλη, απενεργοποίηση κουμπιού
            self.col_btn_list[col - 1]['state'] = 'disabled'
            message = "Column is FULL!"
            label = tk.Label(self, text=message)
            label.grid(row=11, column=0, columnspan=7)


class WinFrame(tk.Frame):
    def __init__(self, master, winner):
        super().__init__(master, bg=blue_bg)
        self.winner = winner
        message = self.message()

        # δημιουργία κεφαλίδας
        self.win_label = tk.Label(self, padx=50, pady=40, text=message)
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

    # μήνυμα νικητή
    def message(self):
        if self.winner == 1:
            msg = "Player 1 Wins"
        elif self.winner == 2:
            msg = "Player 2 Wins"
        else:
            msg = "Draw"
        return msg

    # κλείνει το παράθυρο και ανοίγει καινούριο
    def play_again(self):
        self.master.destroy()
        Connect4()


class RankFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=blue_bg)
        my_conn = sqlite3.connect('../db/connect4_PythonDB.db')

        self.name = tk.Label(self, padx=25, pady=10, text='Name')
        self.name.configure(font=stats_font, background=blue_bg)
        self.games = tk.Label(self, padx=20, pady=10, text='Games')
        self.games.configure(font=stats_font, background=blue_bg)
        self.wins = tk.Label(self, padx=20, pady=10, text='Wins')
        self.wins.configure(font=stats_font, background=blue_bg)
        self.losses = tk.Label(self, padx=20, pady=10, text='Losses')
        self.losses.configure(font=stats_font, background=blue_bg)
        self.draws = tk.Label(self, padx=20, pady=10, text='Draws')
        self.draws.configure(font=stats_font, background=blue_bg)
        self.elo = tk.Label(self, padx=20, pady=10, text='ELO')
        self.elo.configure(font=stats_font, background=blue_bg)
        self.back_btn = tk.Button(self, padx=20, pady=10, text="BACK",
                                  command=lambda: master.show_frame(master.main_frame))
        self.back_btn.configure(font=btn_font, background=red_bg)


        # ταξινομημένοι παίκτες σύμφωνα με elo (πρώτοι 10)
        top_players = my_conn.execute('''SELECT * from users ORDER BY -elo LIMIT 0,10''')

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
        self.back_btn.grid(row=12, column=5)


app = Connect4()
app.mainloop()