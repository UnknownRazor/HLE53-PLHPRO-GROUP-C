import tkinter as tk
from PIL import Image, ImageTk

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


mm = MyApp()
mm.mainloop()
