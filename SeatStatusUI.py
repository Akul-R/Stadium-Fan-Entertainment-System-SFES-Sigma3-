from tkinter import *                                       #importing packages
import tkinter
import customtkinter
import json
customtkinter.set_appearance_mode("dark")

#here is a nice green used in previous projects: #08A045
#and corresponding hover colour: #078E3D

#here is a nice red used in previous projects: #d94d43
#and corresponding hover colour: #c1433b

#here is a nice grey used in previous projects: #656565
#since grey means disabled (usually), no hover colour needed

class StatusUI(customtkinter.CTk):
    def __init__(self):  # all widgets are objects which are children of frame objects
        super().__init__()

        self.title("SFES - SEAT STATUS VIEWER")  # SFES, Stadium Fan Entertainment System (Name is a WIP)
        self.geometry(f"{1200}x{600}")

        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

        #frame to contain the seat status stuff
        self.info_frame = customtkinter.CTkFrame(self)
        self.info_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.info_frame.rowconfigure(0, weight=1)
        self.info_frame.columnconfigure(0, weight=1)

        self.seat_status_frame = tkinter.Canvas(self.info_frame, bg="gray17")
        self.seat_status_frame.grid(row=0, column=0, sticky="nsew")

        self.legend_frame = customtkinter.CTkFrame(self)
        self.legend_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.legend_frame.rowconfigure(0, weight=1)
        for i in range(0, 5):
            self.legend_frame.columnconfigure(i, weight=1)

        self.unoccupied_seat_frame = customtkinter.CTkFrame(self.legend_frame)
        self.unoccupied_seat_frame.grid(row=0, column=0, sticky="nsew")
        self.unoccupied_seat_frame.rowconfigure(0, weight=1)
        self.unoccupied_seat_frame.columnconfigure(0, weight=1)
        self.unoccupied_seat_frame.columnconfigure(1, weight=1)
        self.unoccupied_seat_icon = customtkinter.CTkLabel(self.unoccupied_seat_frame, text="        ", fg_color="#d94d43", corner_radius=4)
        self.unoccupied_seat_icon.grid(row=0, column=0)
        self.unoccupied_seat_text = customtkinter.CTkLabel(self.unoccupied_seat_frame, text="Seat Occupied")
        self.unoccupied_seat_text.grid(row=0, column=1)


        self.menu_frame = customtkinter.CTkFrame(self)
        self.menu_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=20)

        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.rowconfigure(0, weight=1)
        self.menu_frame.rowconfigure(1, weight=1)

        #this dropdown allows you to pick which section to view
        self.seat_section_drop = customtkinter.CTkComboBox(self.menu_frame, command=self.load_grid_from_json)
        self.seat_section_drop.grid(row=0, column=0, sticky="nwe", padx=20, pady=20)

        #reading from seat json to dynamically change how many sections there are in dropdown
        try:
            file = open("Seats.json", "r")
            self.seat_json = json.load(file)
            file.close()

            #sections in stadium, ie section 1, 2...
            self.sections_list = list(self.seat_json.keys())

            #adding word Section in front of each number to make formatting look prettier
            for s in range(0, len(self.sections_list)):
                self.sections_list[s] = (f"Section {self.sections_list[s]}")

            self.seat_section_drop.configure(values=self.sections_list)
            self.seat_section_drop.set("Section 1")

        except:
            print("JSON FILE NOT FOUND")

        self.load_grid_from_json("Section 1")

    def load_grid_from_json(self, choice):
        #initially destroy the status frame to be able to update the grid
        self.seat_status_frame.destroy()
        choice = choice.strip("Section ")

        #info for each section saved in json file as: sectionNum : [rows, columns]
        section_rows = self.seat_json[choice][0]
        section_columns = self.seat_json[choice][1]

        self.seat_status_frame = tkinter.Canvas(self.info_frame, bg="gray17")
        self.seat_status_frame.grid(row=0, column=0, sticky="nsew")

        self.info_frame.update_idletasks()
        self.update()
        canvas_w = self.seat_status_frame.winfo_width()
        canvas_h = self.seat_status_frame.winfo_height()

        axis_padding = 30
        padding = 10
        seat_w = (canvas_w-(axis_padding/2))/(section_columns+1)
        seat_h = (canvas_h-(axis_padding/2))/(section_rows+1)

        for row in range(0, section_rows+1):
            for col in range(0, section_columns+1):
                if(row == 0):
                    #this is very top so just labels (ie, 1, 2, 3...)
                    if(col == 0):
                        #get rid of the 0 at corner of the grid
                        continue
                    x = (col * seat_w) + (seat_w/2)
                    y = axis_padding
                    self.seat_status_frame.create_text(x, y, text=str(col), fill="white", font=("Arial", 10, "bold"), anchor="w")
                    continue

                if(col == 0):
                    #this is the row lables (ie, A, B, C...)
                    letter = chr(ord("A") + (row - 1))
                    x = axis_padding
                    y = (row * seat_h) + (seat_h/2)
                    self.seat_status_frame.create_text(x, y, text=letter, fill="white", font=("Arial", 10, "bold"), anchor="n")
                    continue

                x1 = (col * seat_w) + padding
                y1 = (row * seat_h) + padding

                x2 = x1 + seat_w - padding
                y2 = y1 + seat_h - padding

                letter = chr(ord("A") + (row - 1))
                seat_id = (f"{letter}{col}") #unique seat id
                self.seat_status_frame.create_rectangle(
                    x1, y1, x2, y2,
                    fill="#d94d43",
                    outline="#d94d43",
                    width=1,
                    tags=("seat", seat_id))

        self.seat_status_frame.itemconfig("G7", fill="#08A045", outline="#08A045")




window = StatusUI() #creating a UI object from my class
window.mainloop() #the mainloop of the ui
