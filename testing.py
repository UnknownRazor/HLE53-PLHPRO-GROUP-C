import tkinter as tk
from PIL import Image, ImageTk, ImageDraw


def on_canvas_click(event):
    x, y = event.x, event.y
    if is_within_button(x, y, button1_coords):
        button_clicked(1)
    elif is_within_button(x, y, button2_coords):
        button_clicked(2)


def button_clicked(button_id):
    print(f"Button {button_id} clicked!")



def is_within_button(x, y, button_coords):
    button_x1, button_y1, button_x2, button_y2 = button_coords
    if button_x1 <= x <= button_x2 and y >= button_y1 and y <= button_y2:
        return True
    return False


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

bg_image = tk.PhotoImage(file="assets/bg.png")
canvas.create_image(0, 0, image=bg_image, anchor="nw")

button1_image = tk.PhotoImage(file="transparent_button.png")
button1_coords = (100, 100, 400, 400)
canvas.create_image(button1_coords[0], button1_coords[1], image=button1_image, anchor="nw")

button2_image = tk.PhotoImage(file="transparent_button.png")
button2_coords = (400, 400, 500, 450)
canvas.create_image(button2_coords[0], button2_coords[1], image=button2_image, anchor="nw")


image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)
draw.rectangle([(0, 0), (99, 99)], fill=(0, 0, 255))
photo_image = ImageTk.PhotoImage(image)


image_id = canvas.create_image(0, 0, image=photo_image, anchor="nw")
canvas.update()
image_width = canvas.bbox(image_id)[2] - canvas.bbox(image_id)[0]
image_height = canvas.bbox(image_id)[3] - canvas.bbox(image_id)[1]
canvas.coords(image_id, 400 - image_width / 2, 300 - image_height / 2)




def on_mouse_move(event):
    x, y = event.x, event.y
    if 60 < x < 480 and 60 < y < 480:
        # Show the image if the mouse is within the specified bounds
        canvas.itemconfig(image_id, state="normal")
        # Move the image to follow the mouse
        canvas.coords(image_id, x, y)
    else:
        # Hide the image if the mouse is not within the specified bounds
        canvas.itemconfig(image_id, state="hidden")


canvas.bind("<Motion>", on_mouse_move)
canvas.bind("<Button-1>", on_canvas_click)

root.mainloop()
