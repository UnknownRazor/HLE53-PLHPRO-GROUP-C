import tkinter as tk
from PIL import Image, ImageTk
from connect41 import App
from ranking import Rank

MAX_ROW = 10
MAX_COL = 10
lbl_font = ("Courier", 20, "bold")
btn_font = ("Courier", 12, "bold")

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.row_input = 6
        self.col_input = 7
        self.grid = [[0 for _ in range(self.row_input)] for _ in range(self.col_input)]
        self.turn = 1  # 1: κόκκινο / -1: κίτρινο
        # δημιουργία παραθύρου
        self.title("Connect 4")
        self.iconbitmap("4.ico")
        self.geometry("500x400")
        self.resizable(width=False, height=False)

        # Δημιουργία Frames (μενού + υπο-μενού)
        self.main_frame = MainFrame(self)   # main menu
        self.size_frame = SizeFrame(self)   # μέγεθος ταμπλό
        self.custom_frame = CustomFrame(self)   # δημιουργία ταμπλό
        self.vs_frame = VsFrame(self)       # pvp - pve
        self.table_frame = TableFrame(self, self.row_input, self.col_input)  # ταμπλό
        self.rank_frame = RankFrame(self)   # κατάταξη

        # Τοποθέτηση των frames στο παράθυρο
        all_frames = (self.main_frame, self.size_frame, self.custom_frame, self.vs_frame, self.table_frame, self.rank_frame)
        for frame in all_frames:
            frame.pack(fill=tk.BOTH, expand=True)

        # εμφάνιση αρχικού frame
        self.show_frame(self.main_frame)


    def show_frame(self, frame):
        # κρύβει όλα τα frames και εμφανίζει αυτό που παίρνει σαν όρισμα
        all_frames = (self.main_frame, self.size_frame, self.custom_frame, self.vs_frame, self.table_frame, self.rank_frame)
        for f in all_frames:
            f.pack_forget()
        frame.pack(fill=tk.BOTH, expand=True)


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='#ffd966')

        # δημιουργία κεφαλίδας
        self.main_label = tk.Label(self, padx=50, pady=40, text="Main Menu")
        self.main_label.configure(font=lbl_font, background="#ffd966")

        # δημιουργία κουμπιών
        self.play_btn = tk.Button(self, padx=100, pady=10, text="Play",
                                  command=lambda: master.show_frame(master.size_frame))
        self.play_btn.configure(font=btn_font, background="#f44336")
        self.rank_btn = tk.Button(self, padx=100, pady=10, text="Rank",
                                  command=lambda: master.show_frame(master.rank_frame))
        self.rank_btn.configure(font=btn_font, background="#f44336")
        self.exit_btn = tk.Button(self, padx=100, pady=10, text="Exit",
                                  command=self.exit)
        self.exit_btn.configure(font=btn_font, background="#f44336")

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
        super().__init__(master, bg='#ffd966')

        # δημιουργία κεφαλίδας
        self.size_label = tk.Label(self, padx=50, pady=40, text="Table Size")
        self.size_label.configure(font=lbl_font, background="#ffd966")
        # δημιουργία κουμπιών μενού
        self.preset_btn = tk.Button(self, padx=70, pady=10, text="Preset (6x7)",
                                    command=lambda: master.show_frame(master.vs_frame))
        self.preset_btn.configure(font=btn_font, background="#f44336")
        self.custom_btn = tk.Button(self, padx=100, pady=10, text="Custom",
                                    command=lambda: master.show_frame(master.custom_frame))
        self.custom_btn.configure(font=btn_font, background="#f44336")
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.main_frame))
        self.back_btn.configure(font=btn_font, background="#f44336")

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.size_label.pack()
        self.preset_btn.pack()
        self.custom_btn.pack()
        self.back_btn.pack()


class CustomFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='#ffd966')

        # δημιουργία κεφαλίδας
        self.custom_label = tk.Label(self, padx=50, pady=40, text="Custom Table")
        self.custom_label.configure(font=lbl_font, background="#ffd966")
        # δημιουργία κουμπιών & πεδίων εισαγωγής γραμμών/στηλών
        self.row_label = tk.Label(self, padx=50, pady=10, text="Rows (5 - 10)")
        self.row_label.configure(font=btn_font, background="#f44336")
        self.column_label = tk.Label(self, padx=35, pady=10, text="Columns (5 - 10)")
        self.column_label.configure(font=btn_font, background="#f44336")
        self.row_entry = tk.Entry(self, font=btn_font, width=5)
        self.column_entry = tk.Entry(self,font=btn_font, width=5)
        self.ok_btn = tk.Button(self, padx=50, pady=10, text="OK", command=self.save_size)
        self.ok_btn.configure(font=btn_font, background="#f44336")
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.size_frame))
        self.back_btn.configure(font=btn_font, background="#f44336")

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.custom_label.pack()
        self.row_label.pack()
        self.row_entry.pack(pady=10)
        self.column_label.pack()
        self.column_entry.pack(pady=10)
        self.ok_btn.pack()
        self.back_btn.pack()

    def save_size(self):
        pass

class VsFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='#ffd966')

        # δημιουργία κεφαλίδας
        self.vs_label = tk.Label(self, padx=50, pady=40, text="Table Size")
        self.vs_label.configure(font=lbl_font, background="#ffd966")
        # δημιουργία κουμπιών μενού
        self.pvp_btn = tk.Button(self, padx=70, pady=10, text="Person VS Person",
                                    command=lambda: master.show_frame(master.table_frame))
        self.pvp_btn.configure(font=btn_font, background="#f44336")
        self.pve_btn = tk.Button(self, padx=60, pady=10, text="Person VS Computer",
                                    command=lambda: master.show_frame(master.table_frame))
        self.pve_btn.configure(font=btn_font, background="#f44336")
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.main_frame))
        self.back_btn.configure(font=btn_font, background="#f44336")

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.vs_label.pack()
        self.pvp_btn.pack()
        self.pve_btn.pack()
        self.back_btn.pack()


class TableFrame(tk.Frame):
    def __init__(self, master, rows, columns):
        super().__init__(master, bg='#ffd966')

        self.rows = rows
        self.columns = columns

        # δημιουργία κεφαλίδας
        self.vs_label = tk.Label(self, padx=50, pady=40, text="Table Size")
        self.vs_label.configure(font=lbl_font, background="#ffd966")

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
        # lambda j=i+1 : κρατάει την τιμή του i στο j, σε κάθε Loop
        # χωρίς το j, όλα τα κουμπιά παίρνουν την τιμή του i στο τέλος του loop
        self.col_btn_list = []
        for i in range(self.columns):
            col_btn = tk.Button(self, text=str(i + 1), padx=16, pady=10,
                                command=lambda k=i + 1: self.click_col(k))
            col_btn.configure(font=btn_font, background="#f44336")
            col_btn.grid(row=0, column=i)
            self.col_btn_list.append(col_btn)

        # λίστα με πλήθος γεμάτων κελιών ανά στήλη
        # θέση = στήλη / τιμή = τρέχουσα κενή γραμμή
        # αρχικοποίηση στην 7η γραμμή (όλες οι θέσεις κενές)
        self.current_row = []
        for i in range(self.columns + 1):
            self.current_row.append(7)

        self.create_grid()

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        # self.size_label.pack()
        # self.preset_btn.pack()
        # self.custom_btn.pack()
        # self.back_btn.pack()

    # δημιουργία κενού ταμπλό
    def create_grid(self):
        for i in range(1, self.rows + 1):
            for j in range(self.columns):
                box_label = tk.Label(self, image=self.white)
                box_label.grid(row=i, column=j)

    def play_red(self, col):
        box_label = tk.Label(self, image=self.red)
        box_label.grid(row=self.current_row[col] - 1, column=col - 1)

    def play_yellow(self, col):
        box_label = tk.Label(self, image=self.yellow)
        box_label.grid(row=self.current_row[col] - 1, column=col - 1)


class RankFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='#ffd966')

        # δημιουργία κεφαλίδας
        self.rank_label = tk.Label(self, padx=50, pady=40, text="Rank")
        self.rank_label.configure(font=lbl_font, background="#ffd966")
        # δημιουργία κουμπιών μενού
        self.back_btn = tk.Button(self, padx=50, pady=10, text="BACK",
                                   command=lambda: master.show_frame(master.main_frame))
        self.back_btn.configure(font=btn_font, background="#f44336")

        # τοποθέτηση widgets στο παράθυρο
        self.pack(fill=tk.BOTH, expand=True)
        self.rank_label.pack()
        self.back_btn.pack()


# class Menu:
#     def __init__(self):
#
#         self.row_input = 6
#         self.col_input = 7
#         self.grid = [[0 for _ in range(self.row_input)] for _ in range(self.col_input)]
#         self.turn = 1    # 1: κόκκινο / -1: κίτρινο
#         # δημιουργία παραθύρου
#         self.root = tk.Tk()
#         self.root.title("Connect 4")
#         self.root.iconbitmap("4.ico")
#         self.root.geometry("500x400")
#         self.root.resizable(width=False, height=False)
#
#
#         # size menu
#         # δημιουργία frame
#         self.size_frame = tk.LabelFrame(self.root)
#         self.size_frame.configure(background="#ffd966")
#         # δημιουργία κεφαλίδας
#         self.size_label = tk.Label(self.size_frame, padx=50, pady=40, text="Table Size")
#         self.size_label.configure(font=("Courier", 20, "bold"), background="#ffd966")
#         # δημιουργία κουμπιών μενού
#         self.preset_btn = tk.Button(self.size_frame, padx=70, pady=10, text="Preset (6x7)", command=self.play)
#         self.preset_btn.configure(font=("Courier", 12, "bold"), background="#f44336")
#         self.custom_btn = tk.Button(self.size_frame, padx=100, pady=10, text="Custom", command=self.size)
#         self.custom_btn.configure(font=("Courier", 12, "bold"), background="#f44336")
#         self.back_btn1 = tk.Button(self.size_frame, padx=50, pady=10, text="BACK", command=self.back_to_menu)
#         self.back_btn1.configure(font=("Courier", 12, "bold"), background="#f44336")
#
#         # menu εισαγωγής διαστάσεων
#         # δημιουργία frame
#         self.custom_frame = tk.LabelFrame(self.root)
#         self.custom_frame.configure(background="#ffd966")
#         # δημιουργία κεφαλίδας
#         self.custom_label = tk.Label(self.custom_frame, padx=50, pady=40, text="Custom Table")
#         self.custom_label.configure(font=("Courier", 20, "bold"), background="#ffd966")
#         # δημιουργία κουμπιών μενού
#         self.row_label = tk.Label(self.custom_frame, padx=50, pady=10, text="Rows (5 - 10)")
#         self.row_label.configure(font=("Courier", 12, "bold"), background="#f44336")
#         self.column_label = tk.Label(self.custom_frame, padx=35, pady=10, text="Columns (5 - 10)")
#         self.column_label.configure(font=("Courier", 12, "bold"), background="#f44336")
#         self.row_entry = tk.Entry(self.custom_frame, font=("Courier", 12, "bold"), width=5)
#         self.column_entry = tk.Entry(self.custom_frame,font=("Courier", 12, "bold"), width=5)
#         self.ok_btn = tk.Button(self.custom_frame, padx=50, pady=10, text="OK", command=self.save_size)
#         self.ok_btn.configure(font=("Courier", 12, "bold"), background="#f44336")
#
#         # Play menu
#         # δημιουργία frame
#         self.play_frame = tk.LabelFrame(self.root)
#         self.play_frame.configure(background="#ffd966")
#         # δημιουργία κεφαλίδας
#         self.play_label = tk.Label(self.play_frame, padx=50, pady=40, text="Play")
#         self.play_label.configure(font=("Courier", 20, "bold"), background="#ffd966")
#         # δημιουργία κουμπιών μενού
#         self.pvp_btn = tk.Button(self.play_frame, padx=85, pady=10, text="PLAYER VS PLAYER", command=self.pvp)
#         self.pvp_btn.configure(font=("Courier", 12, "bold"), background="#f44336")
#         self.pve_btn = tk.Button(self.play_frame, padx=100, pady=10, text="PLAYER VS BOT")
#         self.pve_btn.configure(font=("Courier", 12, "bold"), background="#f44336")
#         self.back_btn2 = tk.Button(self.play_frame, padx=50, pady=10, text="BACK", command=self.back_to_menu)
#         self.back_btn2.configure(font=("Courier", 12, "bold"), background="#f44336")
#
#         # κενά πιόνια
#         self.white = Image.open("white.jpg")
#         self.white = ImageTk.PhotoImage(self.white)
#         # κόκκινα πιόνια
#         self.red = Image.open("red.jpg")
#         self.red = ImageTk.PhotoImage(self.red)
#         # κίτρινα πιόνια
#         self.yellow = Image.open("yellow.jpg")
#         self.yellow = ImageTk.PhotoImage(self.yellow)
#
#         # Ταμπλό παιχνιδιού
#         # δημιουργία frame
#         self.table_frame = tk.LabelFrame(self.root)
#         self.table_frame.configure(background="blue")
#         # δυναμική δημιουργία κουμπιών στηλών
#         # lambda j=i+1 : κρατάει την τιμή του i στο j, σε κάθε Loop
#         # χωρίς το j, όλα τα κουμπιά παίρνουν την τιμή του i στο τέλος του loop
#         self.col_btn_list = []
#         for i in range(self.col_input):
#             col_btn = tk.Button(self.table_frame, text=str(i + 1), padx=16, pady=10, command=lambda k=i + 1: self.click_col(k))
#             col_btn.configure(font=("Courier", 12, "bold"), background="#f44336")
#             col_btn.grid(row=0, column=i)
#             self.col_btn_list.append(col_btn)
#
#         # λίστα με πλήθος γεμάτων κελιών ανά στήλη
#         # θέση = στήλη / τιμή = τρέχουσα κενή γραμμή
#         # αρχικοποίηση στην 7η γραμμή (όλες οι θέσεις κενές)
#         self.current_row = []
#         for i in range(self.col_input + 1):
#             self.current_row.append(7)
#
#         self.create_grid()
#
#         self.root.mainloop()
#
#
#     def table_size(self):
#         self.main_frame.destroy()
#         # τοποθέτηση frame size menu
#         self.size_frame.pack(fill=tk.BOTH, expand=True)
#         self.size_label.pack()
#         self.preset_btn.pack()
#         self.custom_btn.pack()
#         self.back_btn1.pack()
#
#     def play(self):
#         self.size_frame.destroy()
#         # τοποθέτηση frame size menu
#         self.play_frame.pack(fill=tk.BOTH, expand=True)
#         self.play_label.pack()
#         self.pvp_btn.pack()
#         self.pve_btn.pack()
#         self.back_btn2.pack()
#
#
#     def size(self):
#         self.size_frame.destroy()
#         # τοποθέτηση frame custom menu
#         self.custom_frame.pack(fill=tk.BOTH, expand=True)
#         self.custom_label.pack()
#         self.row_label.pack()
#         self.row_entry.pack(pady=10)
#         self.column_label.pack()
#         self.column_entry.pack(pady=10)
#         self.ok_btn.pack()
#
#     def save_size(self):
#         self.row_input = self.row_entry.get()
#         self.col_input = self.column_entry.get()
#         print(self.row_input)
#         print(self.col_input)
#
#
#     def back_to_menu(self):
#         self.play_frame.pack_forget()
#         self.main_frame.pack(fill=tk.BOTH, expand=True)
#         self.label.pack()
#         self.play_btn.pack()
#         self.rank_btn.pack()
#         self.exit_btn.pack()

    def pvp(self):
        self.play_frame.destroy()
        self.table_frame.pack(fill=tk.BOTH, expand=True)

    # δημιουργία κενού ταμπλό
    def create_grid(self):
        for i in range(1, self.row_input + 1):
            for j in range(self.col_input):
                box_label = tk.Label(self.table_frame, image=self.white)
                box_label.grid(row=i, column=j)

    def play_red(self, col):
        box_label = tk.Label(self.table_frame, image=self.red)
        box_label.grid(row=self.current_row[col] - 1, column=col - 1)

    def play_yellow(self, col):
        box_label = tk.Label(self.table_frame, image=self.yellow)
        box_label.grid(row=self.current_row[col] - 1, column=col - 1)

    # Εύρεση κατώτερης κενής θέσης
    def find_position(self, selected_column):
        # αναζήτηση στις γραμμές για την κατώτερη κενή θέση(0)
        for row in range(len(self.grid)):
            # αν βρεθεί γεμάτη θέση επιστρέφει την προηγούμενη γραμμή(κενή)
            # αν ολόκληρη η στήλη είναι γεμάτη, επιστρέφει -1
            if self.grid[row][selected_column] != 0:
                return row - 1
        # αν ολόκληρη η στήλη είναι κενή επιστρέφει την τελευταία γραμμή
        return 5

    # Επιλογή θέσης από τον παίκτη και τοποθέτηση του πιονιού
    def player_turn(self, player, player_column):
        player_column -= 1
        # εύρεση κενής θέσης (γραμμής)
        player_row = self.find_position(player_column)
        # αν η στήλη είναι γεμάτη, διαλέγει άλλη στήλη
        while player_row == -1:
            print("This Column is Full!")
            player_column = player_column
            player_row = self.find_position(player_column)
        # ο παίκτης καταλαμβάνει την κενή θέση
        self.grid[player_row][player_column] = player
        return

    # len(grid)    : αριθμός γραμμών
    # len(grid[0]) : αριθμός στηλών

    # Ελέγχει αν υπάρχουν 4 όμοιες θέσεις οριζόντια
    def horizontal_four(self):
        # για κάθε γραμμή (0 έως και την τελευταία)
        # ελέγχει τις θέσεις των στηλών (0 έως 3),(1 έως 4),(2 έως 5),(3 έως 6),...
        for row in range(len(self.grid)):
            #  η αρχική στήλη της τετράδας column
            for column in range(len(self.grid[0]) - 3):
                # αν 4 διαδοχικές θέσεις μιας γραμμής είναι ίδιες
                four_same = (self.grid[row][column] == self.grid[row][column + 1]) and \
                            (self.grid[row][column + 1] == self.grid[row][column + 2]) and \
                            (self.grid[row][column + 2] == self.grid[row][column + 3])
                # αν οι 4 θέσεις δεν είναι κενές
                if four_same and self.grid[row][column] != 0:
                    # επιστρέφει το νικητή
                    winner = self.grid[row][column]
                    return winner
        return None  # δε βρέθηκε νικητής

    # Ελέγχει αν υπάρχουν 4 όμοιες θέσεις κάθετα
    def vertical_four(self):
        # για κάθε στήλη (0 έως και την τελευταία)
        # ελέγχει τις θέσεις των γραμμών (0 έως 3),(1 έως 4),(2 έως 5),...
        for column in range(len(self.grid[0])):
            # η αρχική γραμμή της τετράδας row
            for row in range(len(self.grid) - 3):
                # αν 4 διαδοχικές θέσεις μιας στήλης είναι ίδιες
                four_same = (self.grid[row][column] == self.grid[row + 1][column]) and \
                            (self.grid[row + 1][column] == self.grid[row + 2][column]) and \
                            (self.grid[row + 2][column] == self.grid[row + 3][column])
                # αν οι 4 θέσεις δεν είναι κενές
                if four_same and self.grid[row][column] != 0:
                    # επιστρέφει το νικητή
                    winner = self.grid[row][column]
                    return winner
        return None  # δε βρέθηκε νικητής

    # Ελέγχει αν υπάρχουν 4 όμοιες θέσεις στις κυρίως διαγώνιους
    def diagonal_four(self):
        # για κάθε γραμμή που μπορεί να ξεκινήσει διαγώνιος (0 έως και 3 πριν το τέλος)
        # ελέγχει τις διαδοχικές διαγώνιες θέσεις
        for row in range(len(self.grid) - 3):
            for column in range(len(self.grid[0]) - 3):
                # αν 4 διαδοχικές διαγώνιες θέσεις είναι ίδιες
                four_same = (self.grid[row][column] == self.grid[row + 1][column + 1]) and \
                            (self.grid[row + 1][column + 1] == self.grid[row + 2][column + 2]) and \
                            (self.grid[row + 2][column + 2] == self.grid[row + 3][column + 3])
                # αν οι 4 θέσεις δεν είναι κενές
                if four_same and self.grid[row][column] != 0:
                    # επιστρέφει το νικητή
                    winner = self.grid[row][column]
                    return winner
        return None  # δε βρέθηκε νικητής

    # Αντιστρέφει το ταμπλό (ως προς τις στήλες)
    # η τελευταία στήλη γίνεται πρώτη, η προτελευταία δεύτερη κτλ.
    # Ελέγχει αν υπάρχουν 4 όμοιες θέσεις στις κυρίως διαγώνιους
    # def anti_diagonal_four(self):
    #     anti_grid = [[self.grid[row][column] for column in range(len(self.grid[0]) - 1, -1, -1)] for row in range(len(self.grid))]
    #     return anti_grid.diagonal_four()

    # Ελέγχει αν υπάρχει νικητής και τον επιστρέφει
    def check_winner(self):
        # οριζόντια
        winner = self.horizontal_four()
        if winner:
            return winner
        # κάθετα
        winner = self.vertical_four()
        if winner:
            return winner
        # διαγώνια
        winner = self.diagonal_four()
        if winner:
            return winner
        # # αντιδιαγώνια
        # winner = anti_diagonal_four(grid)
        # if winner:
        #     return winner

    # Ελέγχει αν έχουμε ισοπαλία(γεμάτο ταμπλό) και επιστρέφει True/False
    def is_draw(self):
        # ελέγχει αν υπάρχουν κενές θέσης την πάνω γραμμή
        for column in range(7):
            # εφόσον υπάρχει μία κενή θέση το πλέγμα δεν έχει γεμίσει
            if self.grid[0][column] == 0:
                return False
        # έχει γεμίσει και η πάνω γραμμή, άρα ολόκληρο το πλέγμα
        # δεν υπήρξε νικητής, Ισοπαλία
        print("---Draw---")
        print("---Game Over---")
        return True

    # Παίρνει ως όρισμα το ταμπλό και τους παίκτες
    # Ελέγχει αν υπάρχει νικητής/ισοπαλία και επιστρέφει True/False
    def game_over(self):
        winner = self.check_winner()

        if winner == 1:  # κέρδισε ο παίκτης 1
            return winner
        elif winner == 2:  # κέρδισε ο παίκτης 2
            return winner
        elif self.is_draw():  # ισοπαλία
            return 0
        # δεν υπάρχει νικητής/ισοπαλία
        return False

    # Εμφάνιση νικητή
    def print_winner(self):

        if self.game_over() == 1:
            message = "---1 Wins---"
        elif self.game_over() == 2:
            message = "---2 Wins---"
        else: # self.game_over() == 0:
            message = "---Draw---"
        print(message)
        label = tk.Label(self.play_frame, text=message)
        label.grid(row=11, column=0, columnspan=7)

    def click_col(self, col):
        # αν δεν είναι γεμάτη η στήλη
        # τοποθετεί το πιόνι στην κατώτερη θέση
        # αλλιώς εμφανίζει ανάλογο μήνυμα
        if self.current_row[col] != 1:
            # οι παίκτες παίζουν εναλλάξ
            if self.turn == 1:
                self.play_red(col)
                self.player_turn(1, col)
                if self.game_over():
                    self.print_winner()
                    self.root.destroy()
            else:
                self.play_yellow(col)
                self.player_turn(2, col)
                if self.game_over():
                    self.print_winner()
                    self.root.destroy()
            self.turn *= -1
            self.current_row[col] -= 1
            # message = f"Clicked button {col}"
        else:  # γεμάτη στήλη, απενεργοποίηση κουμπιού
            self.col_btn_list[col - 1]['state'] = 'disabled'
            message = "Column is FULL!"
            label = tk.Label(self.root, text=message)
            label.grid(row=11, column=0, columnspan=7)

        for row in self.grid:
            print(row)
        print("-" * 10)



    #
    # # def again(self):
    # #     new6 = MainMenu()
    #
    # def rank(self):
    #     self.root.destroy()
    #     new1 = Rank()
    #
    # def options(self):
    #     self.root.destroy()
    #
    # def exit(self):
    #     self.root.destroy()


mm = MyApp()
mm.mainloop()