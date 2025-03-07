from tkinter import filedialog
import requests
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style

def display_image():
    category = entry.get()

    if category:
        url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=TdgBbb6wv6I-CFKTuVWQ6rSafKjXZgv7j_8GMabMVOU"
        data = requests.get(url).json()
        img_data = requests.get(data["urls"]["regular"]).content

        image = Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
        display_image.image = image

def save_image():
    image = display_image.image

    if image:
        filename = filedialog.asksaveasfilename(defaultextension='.jpg')
        if filename:
            image.save(filename)

root = tk.Tk()
root.title("Getter image")
root.geometry("700x500")
root.config(bg="white")
root.resizable(False,False)
style = Style(theme="sandstone")

entry = ttk.Entry(root)
entry.grid(row=0, column=0, padx=10, pady=10, sticky='nsew') 

generate_button = ttk.Button(text="Generate image", command=display_image)
generate_button.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

save_button = ttk.Button(text="Save Image", command=save_image)
save_button.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

label = tk.Label(root, background='white')
label.grid(row=1, column=0, columnspan=3,padx=10, pady=10, sticky='nsew')

root.columnconfigure([0, 1, 2], weight=1)
root.rowconfigure(1, weight=1)
root.mainloop()