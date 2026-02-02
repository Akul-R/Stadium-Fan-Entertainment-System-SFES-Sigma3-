from tkinter import *                                       #importing packages
import tkinter
import customtkinter

class UI(customtkinter.CTk):
    def __init__(self):  # all widgets are objects which are children of frame objects
        super().__init__()

        self.title("SFES V1.0")  # SFES, Stadium Fan Entertainment System (Name is a WIP)
        self.geometry(f"{1200}x{600}")  # Size of Window by default

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.options = customtkinter.CTkTabview(self)
        self.options.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        #options for the tabmenu
        self.options.add("Control Panel")
        self.control_panel_frame = customtkinter.CTkFrame(self.options.tab("Control Panel"))
        self.control_panel_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.control_panel_frame.columnconfigure(0, weight=1)
        self.control_panel_frame.columnconfigure(1, weight=2)

        self.cp_title = customtkinter.CTkLabel(self.control_panel_frame, text="Control Panel")
        self.cp_title.grid(row=0, column=0, padx=20, pady=20)

        self.cp_title2 = customtkinter.CTkLabel(self.control_panel_frame, text="Hello")
        self.cp_title2.grid(row=0, column=1, padx=20, pady=20)

        self.options.add("Occupancy info")
        self.options.add("Orders")


window = UI() #creating a UI object from my class
window.mainloop() #the mainloop of the ui
