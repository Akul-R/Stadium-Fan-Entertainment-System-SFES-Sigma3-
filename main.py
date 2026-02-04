from tkinter import *                                       #importing packages
import tkinter
import customtkinter

class UI(customtkinter.CTk):
    def __init__(self):  # all widgets are objects which are children of frame objects
        super().__init__()

        self.title("SFES V1.0")  # SFES, Stadium Fan Entertainment System (Name is a WIP)
        self.geometry(f"{1200}x{600}")  # Size of Window by default

        for i in range(0, 6):
            self.rowconfigure(i, weight=1)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=2)

        self.seat_frame = customtkinter.CTkFrame(self)
        self.seat_frame.grid(row=0, column=0, rowspan=4, sticky="nsew", padx=20, pady=20)

        self.seat_section_drop = customtkinter.CTkComboBox(self, values=["SECTION 1", "SECTION 2"])
        self.seat_section_drop.grid(row=4, column=0, sticky="nw", padx=20, pady=20)



window = UI() #creating a UI object from my class
window.mainloop() #the mainloop of the ui
