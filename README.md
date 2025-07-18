# 🖼️ Photo Tinder

This is a Python-based tool that helps you quickly sort through a folder of images using your keyboard, similar to the swipe-left/right mechanic in Tinder.

## 🔧 Features

- ▶️ **Right Arrow** – Keep the image (moves it to the `keep/` folder)
- ◀️ **Left Arrow** – Delete the image (moves it to the `delete/` folder)
- ⏪ **Spacebar** – Undo the last action

## 📁 Folder Structure
```
project_folder/
├── images/ # Place all images to sort here
├── keep/ # Images you want to keep
├── delete/ # Images you want to discard
├── image_sorter.py
└── README.md
```
## 🐍 Requirements

- Python 3.7+
- [Pillow](https://python-pillow.org/)

Install Pillow via pip:
```bash
pip install pillow
```

## ▶️ How to Run
1) Place all your images in the images/ folder.

2) Run the script:
```bash
python image_sorter.py
```
3) Use the arrow keys and spacebar to sort images.

🔙 Undo Feature
Pressing spacebar will move the most recently moved image back to the images/ folder and rewind the index.

📌 Notes
Supports .jpg, .jpeg, and .png files by default.

You can expand this to support more formats by editing the valid_exts tuple in the script.

🧼 Final Cleanup
Once you’re done sorting, you can:

Back up or process the contents of the keep/ folder.

Manually delete everything inside the delete/ folder.
