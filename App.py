import customtkinter as ctk
from tkinter import *

class App(ctk.CTk):
    def __init__(self, username : str):
        super().__init__()

        self.username = username
        

        # self settings
        self_size = '1200x800'
        self.title("Main Application")
        self.geometry(self_size)
        self.minsize(1200,800)
        self.maxsize(1200,800)
                
        # -------------------------- Menuframe ----------------------------#
        self.frame_menu = ctk.CTkFrame(self, width= 150, height= 780,)  
        self.frame_menu.place(x=10, y=10)

        # create widgets Menuframe
        self.label1_menu = ctk.CTkLabel(self.frame_menu, text="User:" + str(username))
        self.entry_menu = ctk.CTkEntry(self.frame_menu, placeholder_text="Asset or Workorder nr")
        self.button__menu_search = ctk.CTkButton(self.frame_menu, text = 'Search')
        self.button__menu_advanced_search = ctk.CTkButton(self.frame_menu, text = 'Advanced Search')

        self.button_menu_1 = ctk.CTkButton(self.frame_menu, text = 'Create asset',
                command=lambda: self.frame_mainframe1.tkraise())
        self.button_menu_2 = ctk.CTkButton(self.frame_menu, text = 'Create workorder', 
                command=lambda: self.frame_mainframe2.tkraise())
        self.button_menu_3 = ctk.CTkButton(self.frame_menu, text = 'Statistics',
                command=lambda: self.frame_mainframe3.tkraise())

        # place widgets Menuframe
        self.label1_menu.place(x=0, y=0)
        self.entry_menu.place(x=5, y=30)
        self.button__menu_search.place(x=5, y=60)
        self.button__menu_advanced_search.place(x=5, y=90)
        self.button_menu_1.place(x=5, y=150)
        self.button_menu_2.place(x=5, y=180)
        self.button_menu_3.place(x=5, y=210)

        # -------------------------- Mainframe 1 cr --------------------------#
        self.frame_mainframe1 = ctk.CTkFrame(self, width= 1020, height= 780,)  
        self.frame_mainframe1.place(x=170, y=10)

        # create widgets Mainframe 1
        self.frame_mainframe1_label1 = ctk.CTkLabel(self.frame_mainframe1, text="Create asset here")

        # place widgets Mainframe 1
        self.frame_mainframe1_label1.place(x=500, y=10)

        # -------------------------- Mainframe 2 --------------------------#
        self.frame_mainframe2 = ctk.CTkFrame(self, width= 1020, height= 780,)  
        self.frame_mainframe2.place(x=170, y=10)

        # create widgets Mainframe 2
        self.frame_mainframe2_label1 = ctk.CTkLabel(self.frame_mainframe2, text="Create workorder here")

        # place widgets Mainframe 2
        self.frame_mainframe2_label1.place(x=500, y=10)

        # -------------------------- Mainframe 3 --------------------------#
        self.frame_mainframe3 = ctk.CTkFrame(self, width= 1020, height= 780,)  
        self.frame_mainframe3.place(x=170, y=10)

        # create widgets Mainframe 3
        self.frame_mainframe3_label1 = ctk.CTkLabel(self.frame_mainframe3, text="Show statistics here")

        # place widgets Mainframe 3
        self.frame_mainframe3_label1.place(x=500, y=10)




    
        self.mainloop()
