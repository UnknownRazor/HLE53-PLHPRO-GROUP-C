import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

import modules.connect4 as c4

array = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         ]


class pveScreen(Tk):
    def __init__(self, username, size):
        self.username = username
        self.size = size
        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("1280x640")
        root.iconbitmap('../assets/logo.ico')
        font_fam = ("Roboto", 18, "bold")
        font_fam2 = ("Roboto", 14, "bold")
        bg = PhotoImage(file="../assets/bg.png")
        # canvas main menu
        # --------------------------------------------------------------------------------------------------------------#
        root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - PvE')
        canvas1 = Canvas(root, width=1280, height=640)
        canvas1.pack(fill="both", expand=True)
        bg_canvas = canvas1.create_image(0, 0, image=bg, anchor="nw")
        self.canvas = canvas1
        Exit_button = tk.Button(root, text='Exit', bd=5, width=3, command=root.destroy, font=font_fam,
                                highlightcolor="black")
        Exit_UI = canvas1.create_window(12, 20, anchor="nw", window=Exit_button)
        canvas1.create_line(82.8, 0, 82.8, 640, fill="black", width=2.5)
        menu_buttons = []
        #c4.findpos(counter-1, array)
        for counter in range(0,size):
            menu_buttons.append(tk.Button(root, text=f'{counter + 1}', bd=0, width=4, command=lambda b_id=counter: [c4.choice(array, 1, b_id, button_array), print(array)], font=font_fam))
        self.create_buttons(menu_buttons, canvas1, 0, 0)
        self.root = root
        play_list = self.create_button_array(size, canvas1, root, font_fam)
        button_array = play_list[1]
        print(button_array)
        root.mainloop()
    def create_button_array(self, size, canvas1, root, font_fam):
        buttons_array = []
        buttons_arrays = []
        y = 10
        while len(buttons_array) < size - 1:
            while len(buttons_arrays) < size:
                button = tk.Button(canvas1, text=str(0), bd=3, width=4, command=lambda: [], font=font_fam)
                buttons_arrays.append(button)
            buttons_array.append(buttons_arrays)
            if len(buttons_arrays) >= size:
                buttons_arrays = []
        for rows in buttons_array:
            x = 0
            y += 55
            button_canvas_array = self.create_buttons(rows, canvas1, x, y, True)
        return [button_canvas_array, buttons_array]

    def create_buttons(self, button_list, canvas1, offsetX, offsetY, half=False):
        x = 92 + offsetX
        y = 10 + offsetY
        button_canvas_array = []
        for button in button_list:
            button_canvas = canvas1.create_window(x, y, anchor="nw", window=button)
            x += 70
            if half:
                x = x
            button_canvas_array.append(button_canvas)
        return button_canvas_array
