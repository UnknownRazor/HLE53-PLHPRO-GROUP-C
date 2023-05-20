import tkinter as tk
from tkinter import *
import modules.gamemode as gm


class PVPScreen:
    def __init__(self, username, username2, root):
        self.image_items = []
        self.username = username
        self.size = 7
        self.username2 = username2
        self.root = root
        font_fam = ("Roboto", 18, "bold")
        bg = PhotoImage(file="../assets/bg.png")
        #
        # --------------------------------------------------------------------------------------------------------------#
        root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - PvP')
        self.canvas = Canvas(root, width=1280, height=640)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        # Exit button creation #
        Exit_button = tk.Button(root, text='Exit', bd=5, width=3, command=root.destroy, font=font_fam,
                                highlightcolor="black")
        exit_ui = self.canvas.create_window(12, 20, anchor="nw", window=Exit_button)
        # ----------- #
        # Line next to exit button #
        self.canvas.create_line(82.8, 0, 82.8, 640, fill="black", width=2.5)
        # ---------- #
        menu_buttons = []
        for counter in range(0, self.size):
            menu_buttons.append(counter)
        column_buttons = self.create_buttons(menu_buttons, 0, 0, False, True)
        self.root = root
        self.create_hover(menu_buttons, column_buttons)
        play_list = self.create_button_array()
        button_array = play_list[1]

        self.canvas.bind("<Button-1>", lambda event: self.on_canvas_click(event, menu_buttons, column_buttons))
        self.canvas.bind("<Motion>", lambda event: self.on_mouse_move(event, menu_buttons, column_buttons))
        # create gamemode instance
        self.pvp_gm = gm.PVPMode(button_array, self.canvas, self.username, self.username2)
        self.root.mainloop()

    def create_hover(self, col_array, coord_list):
        self.images = []  # Keep references to PhotoImage objects
        for button in col_array:
            coord_list_copy = coord_list[button]
            image = tk.PhotoImage(file="../assets/white.png")
            self.images.append(image)  # Store the reference to the PhotoImage
            self.image_items.append(
                self.canvas.create_image(coord_list_copy[0], coord_list_copy[2], image=image, anchor="nw",
                                         state="hidden"))

    def create_button_array(self):
        buttons_array = []
        buttons_arrays = []
        y = 10
        # pil_img = Image.open("white.jpg")
        self.img = PhotoImage(file="../assets/white.png")
        for row in range(0, self.size - 1):
            for col in range(0, self.size):
                button = tk.Label(self.canvas, image=self.img, borderwidth=0, highlightthickness=0)
                buttons_arrays.append(button)
            buttons_array.append(buttons_arrays)
            if len(buttons_arrays) >= self.size:
                buttons_arrays = []
        for rows in buttons_array:
            x = 5
            y += 80
            button_canvas_array = self.create_buttons(rows, x, y, True)
        return [button_canvas_array, buttons_array]

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

    def is_within_button(self, x, y, button_coords):
        button_x1, button_x2, button_y1, button_y2 = button_coords
        if button_x1 <= x <= button_x2 and button_y1 <= y <= button_y2:
            return True
        return False

    def on_canvas_click(self, event, col_array, coord_list):
        x, y = event.x, event.y
        counter = 0
        for button in col_array:
            coord_list_copy = coord_list[counter]
            if self.is_within_button(x, y, coord_list_copy):
                self.button_clicked(button)
            counter += 1
        self.on_mouse_move(event, col_array, coord_list)

    def button_clicked(self, button_id):
        # print(f"Button {button_id} clicked!")
        self.pvp_gm.play(button_id, self.root)
        # c4.choice(array, 1, button_id, button_array)

    def on_mouse_move(self, event, col_array, coord_list):
        x, y = event.x, event.y
        if 90 < x < 680 and 10 < y < 120:
            counter = 0
            # Show the image if the mouse is within the specified bounds
            for button in col_array:
                coord_list_copy = coord_list[counter]
                if self.is_within_button(x, y, coord_list_copy):
                    image_item = self.image_items[counter]
                    if self.pvp_gm.turn == 1:
                        image = self.images[counter]  # Use the stored reference to the PhotoImage
                        image.configure(file="../assets/red.png")  # Update the image
                    elif self.pvp_gm.turn == 2:
                        image = self.images[counter]  # Use the stored reference to the PhotoImage
                        image.configure(file="../assets/yellow.png")  # Update the image
                    self.canvas.itemconfigure(image_item, state="normal", image=image)
                else:
                    image_item = self.image_items[counter]
                    self.canvas.itemconfigure(image_item, state="hidden")

                counter += 1
        else:
            # Hide all the images if the mouse is not within the specified bounds
            for counter in range(len(col_array)):
                image_item = self.image_items[counter]
                self.canvas.itemconfigure(image_item, state="hidden")
