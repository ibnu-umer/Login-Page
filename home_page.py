from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from signin_page import open_signin_window
from signup_page import open_signup_window




def open_homepage():
    #Home page window
    hp = Tk()
    hp.geometry("700x450")
    hp.resizable()
    hp.title("Homepage")
    hp.config(bg="white")

    #Image
    img = Image.open("/Users/user/OneDrive/Desktop/VSCode Python/Dependencies/homepage.png")
    img = img.resize((530,330))
    img = ImageTk.PhotoImage(img)
    panel = Label(hp, image = img, borderwidth=0)
    panel.place(x=70, y=85)




    def signup():#signup function, closes homepage and open signup window
        hp.destroy()
        open_signup_window()
    
    def signin():#signin function, closes homepage and open signin window
        hp.destroy()
        open_signin_window()


    #Frame on the top
    top_frame = Frame(hp, bg="gray7", width=700, height=55)
    top_frame.place(x=0, y=0)

    #Signin and Signup buttons
    Button(hp, width=10, pady=6, text="Sign UP",fg="white", bg="blue", border=0, command=signup, cursor="hand2").place(x=600, y=10)
    Button(hp, width=10, pady=7, text="Sign In", fg="blue", bg="white", border=0, command=signin, cursor="hand2").place(x=500, y=10)

    hp.mainloop()

open_homepage()