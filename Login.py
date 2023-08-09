import customtkinter
from tkinter import messagebox
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
			self.emailEntry = customtkinter.CTkEntry(self, placeholder_text="Email")
			self.loginButton = customtkinter.CTkButton(self, text= "Login", command = self.loginCommand)
			self.registerButton = customtkinter.CTkButton(self, text= "Register", command = self.registerCommand)
			self.forgotPwButton = customtkinter.CTkButton(self, text= "Forgot password", command = self.forgotPwCommand)
			self.checkbox = customtkinter.CTkCheckBox(self, text="Remember me")
			
			# place widgets

			self.label.pack(pady=12, padx=10)
			self.usernameEntry.pack(pady=12, padx=10)
			self.passwordEntry.pack(pady=12, padx=10)
			self.emailEntry.pack(pady=12, padx=10)
			self.loginButton.pack(pady=10, padx=10)
			self.registerButton.pack(pady=10, padx=10)
			self.forgotPwButton.pack(pady=10, padx=10)
			self.checkbox.pack(padx=12, pady=10)
		def forgotPwCommand(self):
			messagebox.showinfo("","Not my problem")
		
		def loginCommand(self):
			username = self.usernameEntry.get()
			password = self.passwordEntry.get()
			
			self.login(username, password) 
		
		def login(self, username : str, password : str):
			
			# create Table
			self.conn = sqlite3.connect('login.db')
			self.cursor = self.conn.cursor()	
			
			self.table_create_query = '''CREATE TABLE IF NOT EXISTS Login_Data 
						(usernameSql TEXT, passwordSql TEXT, emailSql TEXT, userIdSql TEXT, userLevelSql TEXT)'''
			self.conn.execute(self.table_create_query)
			
			# create admin
			self.cursor.execute("SELECT COUNT(*) FROM Login_Data")
			numberOfRows = str(self.cursor.fetchone())
			print(numberOfRows)

			if numberOfRows == "(0,)": 
				
				self.data_insert_query = '''INSERT INTO Login_Data (usernameSql, passwordSql, emailSql, 
						userIdSql, userLevelSql) VALUES (?, ?, ?, ?, ?)'''
				self.data_insert_tuple = ("Tommy", "password", "admin@email.com", "100001", "King")
				self.cursor.execute(self.data_insert_query, self.data_insert_tuple)

			# verify input for login and login if criteria is met
			if username and password:

				self.conn.execute(self.table_create_query)
				self.cursor.execute("SELECT * FROM Login_Data WHERE usernameSql = ?",(username,))
				nameAndPw = str(self.cursor.fetchone())

				if nameAndPw == "None": 
					messagebox.showinfo("","Account does not exist, register a new account")
				else:
					messagebox.showinfo("You are being logged in")
					
			else:
				messagebox.showinfo("","You need to type in both username and password!")
					
			self.conn.commit()
			self.conn.close()	
			

		def registerCommand(self):
			username = self.usernameEntry.get()
			password = self.passwordEntry.get()
			email = self.emailEntry.get()

			self.register(username, password, email)
		
		def register(self, username : str, password : str, email : str):
		# Create Table
			self.conn = sqlite3.connect('login.db')
			self.cursor = self.conn.cursor()	
			
			# verify input for registration and register account if criteria is met.
			if username and password and email:

				self.table_create_query = '''CREATE TABLE IF NOT EXISTS Login_Data 
						(usernameSql TEXT, passwordSql TEXT, emailSql TEXT, userIdSql TEXT, userLevelSql TEXT)'''
				

				self.conn.execute(self.table_create_query)

				self.cursor.execute("SELECT * FROM Login_Data WHERE usernameSql = ?",(username,))
				usernameRowSql = str(self.cursor.fetchone())
				
				if usernameRowSql == "None": 
					usernameExist = False
				else:
					usernameExist = True

				self.cursor.execute("SELECT * FROM Login_Data WHERE emailSql = ?",(email,))
				emailSqlRow = str(self.cursor.fetchone())
				
				if emailSqlRow == "None": 
					emailExist = False
				else:
					emailExist = True


				if emailSqlRow == usernameRowSql and emailExist and usernameExist: 
					messagebox.showinfo("","This account already exist!")
					
				elif emailExist:
					messagebox.showinfo("","This email already has an account bound to it, choose another!")

				elif usernameExist: 
					messagebox.showinfo("","The username you typed in is taken, choose another!")
				else:
					self.cursor.execute("SELECT COUNT(*) FROM Login_Data")
					numberOfRows = str(self.cursor.fetchone())
					s1="".join(c for c in numberOfRows if c.isalnum())
					userID : str = 100001 + int(s1)

					self.data_insert_query = '''INSERT INTO Login_Data (usernameSql, passwordSql, 
							emailSql, userIdSql, userLevelSql) VALUES (?, ?, ?, ?, ?)'''
					self.data_insert_tuple = (username, password, email, userID, "Pawn")

					self.cursor.execute(self.data_insert_query, self.data_insert_tuple)
					messagebox.showinfo("","New account created!")

			else:
				messagebox.showinfo("","You need to type in username, email and password to create an account!")
					
			self.conn.commit()
			self.conn.close()
		# def myMessageBox():
		# 	messagebox.showinfo()


Login('Login', (854,480))