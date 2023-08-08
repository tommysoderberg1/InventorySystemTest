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

			self.database(username, password)

			print("Ping")
		
		def database(self, username : str, password : str):
		# Create Table
			self.conn = sqlite3.connect('login.db')
			self.cursor = self.conn.cursor()	
			
			if username and password:

				self.table_create_query = '''CREATE TABLE IF NOT EXISTS Login_Data 
						(usernameSql TEXT, passwordSql TEXT)'''
				
				self.conn.execute(self.table_create_query)

				self.cursor.execute("SELECT * FROM Login_Data WHERE usernameSql = ?",(username,))

				if self.cursor.fetchone() == None: 
					# Insert Data
					self.data_insert_query = '''INSERT INTO Login_Data (usernameSql, passwordSql) VALUES (?, ?)'''
					self.data_insert_tuple = (username, password)

					self.cursor.execute(self.data_insert_query, self.data_insert_tuple)
					
				else:
					print("Username already exists, choose another!") 
					
			else:
				print("You need to type in both username and password!")
					
			self.conn.commit()
			self.conn.close()


Login('Login', (854,480))