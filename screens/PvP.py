import tkinter as tk
from tkinter import *
import modules.gamemode as gm


class PVPScreen:
    def __init__(self, username, username2, root):
        self.username = username
        self.size = 7
        self.username2 = username2
        self.root = root
        font_fam = ("Roboto", 18, "bold")
        font_fam2 = ("Roboto", 14, "bold")
        bg = PhotoImage(file="../assets/bg.png")
        #
        # --------------------------------------------------------------------------------------------------------------#
        root.title('Connect 4 App - ΠΛΗΠΡΟ/ΗΛΕ53 - PvP')
        canvas1 = Canvas(root, width=1280, height=640)
        canvas1.pack(fill="both", expand=True)
        bg_canvas = canvas1.create_image(0, 0, image=bg, anchor="nw")
        self.canvas = canvas1
        # Exit button creation #
        Exit_button = tk.Button(root, text='Exit', bd=5, width=3, command=root.destroy, font=font_fam,
                                highlightcolor="black")
        Exit_UI = canvas1.create_window(12, 20, anchor="nw", window=Exit_button)
        # ----------- #
        # Line next to exit button #
        canvas1.create_line(82.8, 0, 82.8, 640, fill="black", width=2.5)
        # ---------- #
        menu_buttons = []
        #c4.findpos(counter-1, array)
        #for counter in range(0,size):
            #menu_buttons.append(tk.Button(root, text=f'{counter + 1}', bd=0, width=4, command=lambda button_id=counter: [c4.choice(array, 1, button_id, button_array), print(array)], font=font_fam))
        for counter in range(0, self.size):
            menu_buttons.append(counter)
        column_buttons = self.create_buttons(menu_buttons, canvas1, 0, 0, False, True)
        self.root = root
        play_list = self.create_button_array(self.size, canvas1, font_fam)
        button_array = play_list[1]
        #photo_image = PhotoImage(file="../assets/pawn.png")
        #image_id = canvas1.create_image(0, 0, image=photo_image, anchor="nw")
        #canvas1.coords(image_id, 400 - 380 / 2, 300 - 270 / 2)
        canvas1.bind("<Button-1>", lambda event: self.on_canvas_click(event, menu_buttons, column_buttons))
        #canvas1.bind("<Motion>", lambda event: self.on_mouse_move(event, canvas1, None, menu_buttons, column_buttons, button_array))
        # create gamemode instance
        self.pvp_gm = gm.PVPMode(button_array, canvas1, self.username, self.username2)
        self.root.mainloop()

    def create_button_array(self, size, canvas1, font_fam):
        buttons_array = []
        buttons_arrays = []
        y = 10
        #pil_img = Image.open("white.jpg")
        self.img = PhotoImage(file="../assets/white.png")
        for row in range(0, size-1):
            for col in range(0, size):
                button = tk.Label(canvas1, image=self.img, borderwidth=0, highlightthickness=0)
                buttons_arrays.append(button)
            buttons_array.append(buttons_arrays)
            if len(buttons_arrays) >= size:
                buttons_arrays = []
        for rows in buttons_array:
            x = 0
            y += 55
            button_canvas_array = self.create_buttons(rows, canvas1, x, y, True)
        return [button_canvas_array, buttons_array]

    def create_buttons(self, button_list, canvas1, offsetX, offsetY, half=False, button_coord = False):
        x = 92 + offsetX
        y = 10 + offsetY
        button_canvas_array = []
        button_coords = []
        button_coords_list = []
        if button_coord == True:
            for button in button_list:
                button_coords = []
                button_coords.append(x)
                button_coords.append(x+70)
                button_coords.append(y)
                button_coords.append(y+60)
                button_coords_list.append(button_coords)
                x += 70
            return button_coords_list
        for button in button_list:
            button_canvas = canvas1.create_window(x, y, anchor="nw", window=button)
            x += 70
            button_coords.append(x)
            button_coords.append(y)
            if half:
                x = x
            button_canvas_array.append(button_canvas)
        return button_canvas_array

    def is_within_button(self,x, y, button_coords):
        button_x1, button_x2, button_y1, button_y2 = button_coords
        if button_x1 <= x <= button_x2 and y >= button_y1 and y <= button_y2:
            return True
        return False

    def on_canvas_click(self,event, col_array, coord_list):
        x, y = event.x, event.y
        counter = 0
        for button in col_array:
            coord_list_copy = coord_list[counter]
            if self.is_within_button(x, y, coord_list_copy):
                self.button_clicked(button)
            counter += 1

    def button_clicked(self,button_id):
        #print(f"Button {button_id} clicked!")
        self.pvp_gm.play(button_id, self.root)
        #c4.choice(array, 1, button_id, button_array)


    def on_mouse_move(self,event, canvas1, image_id, col_array, coord_list, button_array):
        x, y = event.x, event.y
        if 90 < x < 580 and 10 < y < 60:
            counter = 0
            # Show the image if the mouse is within the specified bounds
            for button in col_array:
                coord_list_copy = coord_list[counter]
                if self.is_within_button(x, y, coord_list_copy):
                    self.button_hover(button)
                else:
                    self.button_hover_leave(button)
                counter += 1
            #canvas1.itemconfig(image_id, state="normal")
            # Move the image to follow the mouse
            #canvas1.coords(image_id, x/4, y/4)
        else:
            # Hide the image if the mouse is not within the specified bounds
            #canvas1.itemconfig(image_id, state="hidden")
            pass
    def button_hover(self, button):
        button["bg"] = "red"
        print(button)
    def button_hover_leave(self, button):
        button["bg"] = "white"
        print(button)