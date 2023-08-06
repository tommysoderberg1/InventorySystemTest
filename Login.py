import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


class Login(customtkinter.CTk):
	def __init__(self, title, size):
		super().__init__()

		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0],size[1])
		
		# modules
		self.loginFrame = LoginFrame(self)

		# run
		self.mainloop()  

class LoginFrame(customtkinter.CTkFrame):
		def __init__(self, parent):
			super().__init__(parent)
			
			# place frame
			self.pack(pady=20, padx=60, fill="both", expand=True)

			# modules on loginframe 
			self.create_widgets()
			self.usernamePass()

		def usernamePass(self):
				
				print("Ping")
				

		def create_widgets(self):
			
			# create the widgets 
			
			label = customtkinter.CTkLabel(self, text = "Inventory System", font=("Roboto", 24))
			entry1 = customtkinter.CTkEntry(self, placeholder_text="Username")
			entry2 = customtkinter.CTkEntry(self, placeholder_text="Password", show="*")
			loginButton = customtkinter.CTkButton(self, text= "Login", command = self.usernamePass)
			registerButton = customtkinter.CTkButton(self, text= "Register")
			forgotPwButton = customtkinter.CTkButton(self, text= "Forgot password")
			checkbox = customtkinter.CTkCheckBox(self, text="Remember me")
			

			# place widgets

			label.pack(pady=12, padx=10)
			entry1.pack(pady=12, padx=10)
			entry2.pack(pady=12, padx=10)
			loginButton.pack(pady=10, padx=10)
			registerButton.pack(pady=10, padx=10)
			forgotPwButton.pack(pady=10, padx=10)
			checkbox.pack(padx=12, pady=10)
		


Login('Login', (854,480))