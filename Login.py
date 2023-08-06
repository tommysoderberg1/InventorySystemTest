import customtkinter 
import tkinter 

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

class windowLogin(customtkinter.CTk):
    def __init__(self):
        super().__init__()

root = customtkinter.CTk()
root.geometry("500x400")

def loginButton():
    print("login")

def registerButton():
    print("register")

def forgotPwButton():
    print("forgot password")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master = frame, text = "Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

loginButton = customtkinter.CTkButton(master=frame, text= "Login", command=loginButton,)
loginButton.pack(pady=10, padx=10)

registerButton = customtkinter.CTkButton(master=frame, text= "Register", command=registerButton)
registerButton.pack(pady=10, padx=10)

forgotPwButton = customtkinter.CTkButton(master=frame, text= "Forgot password", command=forgotPwButton)
forgotPwButton.pack(pady=10, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(padx=12, pady=10)

root.mainloop()