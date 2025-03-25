import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

greeting = tk.StringVar()

image = Image.open("test_image.png").resize((64, 64))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, text="Purple square", image=photo, padding=5, compound="right")
label.pack()
greeting_label = ttk.Label(root, textvariable=greeting, padding=10)
greeting_label.pack()

greeting.set("Hello there!")

root.mainloop()