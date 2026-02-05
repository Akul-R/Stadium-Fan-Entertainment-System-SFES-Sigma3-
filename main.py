from tkinter import *                                       #importing packages
import tkinter
import customtkinter
customtkinter.set_appearance_mode("dark")

class UI(customtkinter.CTk):
    def __init__(self):  # all widgets are objects which are children of frame objects
        super().__init__()

        self.title("SFES V1.0")  # SFES, Stadium Fan Entertainment System (Name is a WIP)
        self.geometry(f"{1200}x{600}")  # Size of Window by default BEANS system deployed

        for i in range(0, 6):
            self.rowconfigure(i, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=2)

        self.info_frame = customtkinter.CTkFrame(self)
        self.info_frame.grid(row=0, column=0, rowspan=4, columnspan=3, sticky="nsew", padx=20, pady=20)

        self.info_frame.rowconfigure(0, weight=1)
        self.info_frame.columnconfigure(0, weight=1)


        for i in range(1, 51):
            self.info_frame.columnconfigure(i, weight=1)
            label = customtkinter.CTkLabel(self.info_frame, text=str(i), anchor="center")
            label.grid(row=0, column=i, sticky="nsew", padx=2, pady=2)

        for i in range(1, 11):
            letter = chr(ord("A") + (i-1))
            self.info_frame.rowconfigure(i, weight=1)
            label = customtkinter.CTkLabel(self.info_frame, text=letter, anchor="center")
            label.grid(row=i, column=0, sticky="nsew", padx=2, pady=2)



        self.seat_section_drop = customtkinter.CTkComboBox(self, values=["SECTION 1", "SECTION 2"])
        self.seat_section_drop.grid(row=4, column=0, sticky="nwe", padx=20)
poopymcbuthole


window = UI() #creating a UI object from my class
window.mainloop() #the mainloop of the ui
