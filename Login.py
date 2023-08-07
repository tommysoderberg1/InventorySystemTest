import customtkinter
import sqlite3



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
			# create the widgets 
			
			self.label = customtkinter.CTkLabel(self, text = "Inventory System", font=("Roboto", 24))
			self.usernameEntry = customtkinter.CTkEntry(self, placeholder_text="Username")
			self.passwordEntry = customtkinter.CTkEntry(self, placeholder_text="Password", show="*")
			self.loginButton = customtkinter.CTkButton(self, text= "Login", command = self.loginCommand)
			self.registerButton = customtkinter.CTkButton(self, text= "Register", command = self.registerCommand)
			self.forgotPwButton = customtkinter.CTkButton(self, text= "Forgot password")
			self.checkbox = customtkinter.CTkCheckBox(self, text="Remember me")
			
			# place widgets

			self.label.pack(pady=12, padx=10)
			self.usernameEntry.pack(pady=12, padx=10)
			self.passwordEntry.pack(pady=12, padx=10)
			self.loginButton.pack(pady=10, padx=10)
			self.registerButton.pack(pady=10, padx=10)
			self.forgotPwButton.pack(pady=10, padx=10)
			self.checkbox.pack(padx=12, pady=10)

		def loginCommand(self):
			username = self.usernameEntry.get()
			password = self.passwordEntry.get()
			print("Username and password:")
			print(username)
			print(password)


		def registerCommand(self):
			username = self.usernameEntry.get()
			password = self.passwordEntry.get()
			print("Ping")
		


Login('Login', (854,480))