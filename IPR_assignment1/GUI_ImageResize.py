import tkinter
import customtkinter
from customtkinter import filedialog
import Resize

customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("500x400")
app.title("Image Resize Tool")

title_label = customtkinter.CTkLabel(app, text="Choose the options", font=("Helvetica", 14, "bold"))
title_label.pack(ipadx=5, ipady=5)

height_var = tkinter.StringVar()
height_label = customtkinter.CTkLabel(app, text="Enter Height:", font=("Helvetica", 12, "bold"))
height_label.pack(padx=5, pady=5)

height_entry = customtkinter.CTkEntry(app, width=80, height=20, border_color="#d6e9ff", textvariable=height_var, placeholder_text="Enter the height:")
height_entry.pack(padx=5, pady=5)

width_var = tkinter.StringVar()
width_label = customtkinter.CTkLabel(app, text="Enter Width:", font=("Helvetica", 12, "bold"))
width_label.pack(padx=5, pady=5)

width_entry = customtkinter.CTkEntry(app, width=80, height=20, border_color="#d6e9ff", textvariable=width_var, placeholder_text="Enter the width:")
width_entry.pack(padx=5, pady=5)

def handle_resize():
    desired_height = int(height_entry.get())
    desired_width = int(width_entry.get())
    path_from_user = filepath
    Resize.image_resize(desired_height, desired_width, path_from_user)

resize_button = customtkinter.CTkButton(master=app, text="Resize Image", command=handle_resize)
resize_button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

def handle_path_input():
    global filepath
    filepath = filedialog.askopenfilename(
        title="Please select an image file",
        filetypes=[
            (("All Images", "*.png;*.jpg;*.jpeg;*.svg;*.bmp;*.gif"))
        ]
    )

select_button = customtkinter.CTkButton(master=app, text="Select Image", command=handle_path_input)
select_button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

app.mainloop()
