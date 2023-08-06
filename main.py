import Login
import App
import customtkinter 

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

class main():
	
    approved_password = False
    
    Login()
    if approved_password == True:
        App()
    else:
        Login()
    
    


if __name__ == '__main__':
    main()
		