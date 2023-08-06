import customtkinter 

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
	

class App(customtkinter.CTk):
	def __init__(self, title, size):
        
		# main setup
		super().__init__()	
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0],size[1])
		# self.maxsize(size[0],size[1])
		
		# main grid layout 5x5
		self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
		self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
		
		# modules
		self.menu = MenuFrame(self)
		self.mainScreen = MainFrame(self)    

        # run 
		self.mainloop()  
                
        

class MenuFrame(customtkinter.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent)
		
		# place frame on maingrid
		self.grid(row=0, column=0, rowspan=10, sticky="nsw")
		
		# modules on menu
		self.create_widgets()

	def create_widgets(self):
		
		# create the widgets 
		menu_entry = customtkinter.CTkEntry(self)
		menu_button_search = customtkinter.CTkButton(self, text = 'Search')
		menu_button2 = customtkinter.CTkButton(self, text = 'Button 2')
		menu_button3 = customtkinter.CTkButton(self, text = 'Button 3')


		# place the widgets
		menu_entry.pack(padx=20, pady=(70,4))
		menu_button_search.pack(padx=20, pady=(0, 30))
		menu_button2.pack(padx=20, pady=4)
		menu_button3.pack(padx=20, pady=4)

class MainFrame(customtkinter.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent)
		
		# place frame on maingrid
		
		self.grid(row=1, column=1, rowspan=8, columnspan=8, sticky="nsew")
		
		# modules on menu
		# self.create_widgets()

	# def create_widgets(self):
		
		# create the widgets 
		
		# place the widgets
		
App('Main application', (1280, 720))
		
              
       
