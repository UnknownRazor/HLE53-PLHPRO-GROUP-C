import tkinter as tk
from tkinter import *
import modules.gamemode as gm

font_fam = ("Roboto", 18, "bold")


class PVEScreen:
    def __init__(self, username, size, root, difficulty=False):
        self.username = username
        self.size = size
        self.difficulty = difficulty
        self.root = root
        self.root.geometry("1280x640")
        self.root.iconbitmap('../assets/logo.ico')
        bg = PhotoImage(file="../assets/bg.png")
        self.white = PhotoImage(file="../assets/white.png")
        # --------------------------------------------------------------------------------------------------------------#
        self.root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - PvE')
        self.canvas = Canvas(self.root, width=1280, height=640)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        # Exit button creation #
        exit_btn = tk.Button(self.root, text='Exit', bd=5, width=3, command=self.root.destroy, font=font_fam,
                             highlightcolor="black")
        self.canvas.create_window(12, 20, anchor="nw", window=exit_btn)
        # ----------- #
        # Line next to exit button #
        self.canvas.create_line(82.8, 0, 82.8, 640, fill="black", width=2.5)
        # ---------- #
        menu_buttons = []
        for counter in range(0, size):
            menu_buttons.append(counter)
        column_buttons = self.create_buttons(menu_buttons, 0, 0, False, True)
        play_list = self.create_button_array(size)
        self.button_array = play_list[1]
        self.canvas.bind("<Button-1>",
                         lambda event: self.on_canvas_click(event, menu_buttons, column_buttons, self.button_array))
        # create gamemode instance
        self.game = gm.PVEMode(self.button_array, self.canvas, self.username,difficulty)
        self.root.mainloop()

    def create_button_array(self, size):
        buttons_array = []
        buttons_arrays = []
        y = 10

        for row in range(0, size - 1):
            for col in range(0, size):
                button = tk.Label(self.canvas, image=self.white, borderwidth=0, highlightthickness=0)
                buttons_arrays.append(button)
            buttons_array.append(buttons_arrays)
            if len(buttons_arrays) >= size:
                buttons_arrays = []
        for rows in buttons_array:
            x = 0
            y += 55
            button_canvas_array = self.create_buttons(rows, x, y, True)
        return [button_canvas_array, buttons_array]

    def create_buttons(self, button_list, offsetX, offsetY, half=False, button_coord=False):
        x = 92 + offsetX
        y = 10 + offsetY
        button_canvas_array = []
        button_coords = []
        button_coords_list = []
        if button_coord == True:
            for button in button_list:
                button_coords = []
                button_coords.append(x)
                button_coords.append(x + 70)
                button_coords.append(y)
                button_coords.append(y + 60)
                button_coords_list.append(button_coords)
                x += 70
            return button_coords_list
        for button in button_list:
            button_canvas = self.canvas.create_window(x, y, anchor="nw", window=button)
            x += 70
            button_coords.append(x)
            button_coords.append(y)
            if half:
                x = x
            button_canvas_array.append(button_canvas)
        return button_canvas_array

    def is_within_button(self, x, y, button_coords):
        button_x1, button_x2, button_y1, button_y2 = button_coords
        if x in range(button_x1, button_x2 + 1) and y in range(button_y1, button_y2 + 1):
            return True
        return False

    def on_canvas_click(self, event, col_array, coord_list, button_array):
        x, y = event.x, event.y
        counter = 0
        for button in col_array:
            coord_list_copy = coord_list[counter]
            if self.is_within_button(x, y, coord_list_copy):
                self.button_clicked(button)
            counter += 1

    def button_clicked(self, button_id):
        self.game.play(button_id, self.root)

    # Εμφανίζει την εικόνα όταν είναι εντός ορίων
    # και ακολουθεί το ποντίκι
    def on_mouse_move(self, event, image_id):
        x, y = event.x, event.y
        if 90 < x < 580 and 10 < y < 60:
            self.canvas.itemconfig(image_id, state="normal")
            self.canvas.coords(image_id, x / 4, y / 4)
        else:
            self.canvas.itemconfig(image_id, state="hidden")

    def get_canvas(self):
        return self.canvas
