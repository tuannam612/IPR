import tkinter
import customtkinter
from tkinter import messagebox

import Binary

customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()
app.geometry("500x300")
app.title("Image Transfer To Binary Tool")

title_label = customtkinter.CTkLabel(app, text="Enter a threshold value between 0 and 255", font=("Helvetica", 12, "bold"))
title_label.pack(pady=10)

threshold_from_user = tkinter.StringVar()
threshold_entry = customtkinter.CTkEntry(app, width=80, height=30, border_color="#d6e9ff", textvariable=threshold_from_user)
threshold_entry.pack(pady=10)

def handle_threshold_value():
    input_threshold = int(threshold_entry.get())

    if input_threshold < 0:
        messagebox.showerror('Error', "Threshold value cannot be executed!")

    elif input_threshold > 255:
        messagebox.showerror('Error', "Threshold value is larger than 255")

    else:
        Binary.make_photo_binary(input_threshold, filepath)

def handle_path_input():
    from customtkinter import filedialog
    global filepath
    filepath = filedialog.askopenfilename(
        title="Please select an image file",
        filetypes=[
            (("All Images", "*.png;*.jpg;*.jpeg;*.svg;*.bmp;*.gif"))
        ]
    )

display_button = customtkinter.CTkButton(app, text="Display Binary Image", command=handle_threshold_value)
display_button.pack(pady=10)

select_button = customtkinter.CTkButton(app, text="Select Image", command=handle_path_input)
select_button.pack(pady=10)

app.mainloop()