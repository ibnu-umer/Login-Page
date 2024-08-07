from PIL import ImageTk, Image
import customtkinter as ctk
from signin_page import open_signin_window


ctk.set_appearance_mode('dark')

login_status = False


def open_homepage():
    
    #Home page window
    hp = ctk.CTk()
    hp.geometry("700x450")
    hp.resizable(width=False, height=False)
    hp.title("Homepage")
    hp.configure(bg_color='white')

    # #Image
    # img = Image.open("/Users/user/OneDrive/Desktop/VSCode Python/Dependencies/homepage.png")
    # img = img.resize((530,330))
    # img = ImageTk.PhotoImage(img)
    # panel = Label(hp, image = img, borderwidth=0)
    # panel.place(x=70, y=85)




    def signup():#signup function, closes homepage and open signup window
        hp.destroy()
        # open_signup_window()
    
    def signin():#signin function, closes homepage and open signin window
        hp.destroy()
        open_signin_window()


    #Frame on the top
    if login_status == False:
        
        top_frame = ctk.CTkFrame(hp, bg_color="black", fg_color="black", width=700, height=55)
        top_frame.place(x=0, y=0)

        #Signin and Signup buttons
        ctk.CTkButton(hp, width=80, height=35, text="Sign UP", font=("Helvetica", 18, "bold"),
                    fg_color="blue", bg_color="black", command=signup, cursor="hand2").place(x=600, y=10)
        
        ctk.CTkButton(hp, width=80, height=35, text="Sign In", font=("Helvetica", 18, "bold"),
                    fg_color="gray", bg_color="black", command=signin, cursor="hand2").place(x=500, y=10)
        

    hp.mainloop()


open_homepage()