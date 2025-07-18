# photo tinder main script
import os
import shutil
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

# CONFIGURATION
IMAGE_DIR = "photos for 2425 video"  # folder containing all images
KEEP_DIR = "keep" # folder for kept images
DELETE_DIR = "delete" # folder for deletion images

# Ensure directories exist
os.makedirs(KEEP_DIR, exist_ok=True)
os.makedirs(DELETE_DIR, exist_ok=True)

# Get all image files
valid_exts = (".jpg", ".jpeg", ".png")
image_files = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(valid_exts)]
image_index = 0

# initialize "history" list (option to undo last action)
history = []  # (action, filename)

# GUI Setup
root = tk.Tk()
root.title("Photo Tinder")
label = Label(root)
label.pack()

# Load and display image
def show_image():
    if 0 <= image_index < len(image_files):
        path = os.path.join(IMAGE_DIR, image_files[image_index])
        img = Image.open(path)
        img.thumbnail((800, 800))
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo
        root.title(f"Viewing {image_files[image_index]}")
    else:
        label.config(text="No more images")
        label.image = None

# Keypresses function 
def on_key(event):
    global image_index
    if event.keysym == "Right":
        move_image(KEEP_DIR)
    elif event.keysym == "Left":
        move_image(DELETE_DIR)
    elif event.keysym == "space":
        undo_action()
    show_image()

def move_image(destination):
    global image_index
    filename = image_files[image_index]
    src = os.path.join(IMAGE_DIR, filename)
    dst = os.path.join(destination, filename)
    shutil.move(src, dst)
    history.append((destination, filename))
    image_index += 1

def undo_action():
    global image_index
    if not history:
        return
    destination, filename = history.pop()
    src = os.path.join(destination, filename)
    dst = os.path.join(IMAGE_DIR, filename)
    shutil.move(src, dst)
    image_index = max(0, image_index - 1)

# Bind keys and start
root.bind("<Key>", on_key)
show_image()
root.mainloop()
