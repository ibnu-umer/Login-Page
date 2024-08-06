from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from signup_page import users
from signup_page import open_signup_window




def open_signin_window():


    si = Tk()
    si.geometry("700x500")
    si.resizable(False, False)
    si.title("SignIn Page")
    si.config(bg="white")

    #Login Page Image setup
    img = Image.open("/Users/user/OneDrive/Desktop/VSCode Python/Dependencies/loginimage.jpg")
    img = img.resize((330,330))
    img_log = ImageTk.PhotoImage(img)
    panel = Label(si, image=img_log, borderwidth=0)
    panel.place(x=55, y=85)


    users.update({"riyas":"riyas777", "rishana":"rinu@123", "Shamil":"shanumon", "Shaha":"shaimol"})



    #Sign In Function
    def signin():
        global username, password
        username = user.get()
        Frame(frame, width=150, height=20, bg="white").place(x=40, y=112)
        Frame(frame, width=92, height=20, bg="white").place(x=40, y=173)
        if username == "Username" or username == "":
            Label(frame, text="Enter username", fg="red", bg="white", font=("Microsoft YaMel U1 Light",9)).place(x=40, y=112)
        elif username in users.keys():
            password = code.get()
            if password == "Password" or password == "":
                Frame(frame, width=200, height=20, bg="white").place(x=40, y=173)
                Label(frame, text="Enter Password", fg="red", bg="white", font=("Microsoft YaMel U1 Light",9)).place(x=40, y=172)
            else:
                if password == users.get(username):
                    password = code.get()
                    Label(frame, text="Login Succesfull", fg="green", bg="white").place(x=70, y= 280)
                else:
                    Frame(frame, width=170, height=20, bg="white").place(x=40, y=173)
                    Label(frame, text="Wrong Password", fg="red", bg="white", font=("Microsoft YaMel U1 Light",9)).place(x=40, y=172)
        elif username not in [users.keys()]:
            Label(frame, text="Username not found!", fg="red", bg="white", font=("Microsoft YaMel U1 Light",9)).place(x=40, y=112)



    #Frame
    frame = Frame(si, width=300, height=300, bg="White")
    frame.place(x=380, y=80)

    #SignIp Heading
    heading = Label(si, text="Sign In", fg="#57a1f8", bg="white", font=("Microsoft YaMel U1 Light", 22, "bold"))
    heading.place(x=450, y=90)

    #Functions to make username visible and invisible
    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "Username")


    #Username entry box
    user = Entry(frame, width=25, fg="black",border=0, bg="white", font=("Microsoft YaMel U1 Light",11))
    user.place(x=40, y=90)
    user.insert(0,"Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    #Functions to make Password visible and invisible
    def on_enter(e):
        code.delete(0, "end")

    def on_leave(e):
        password = code.get()
        if password == "":
            code.insert(0, "Password")


    #Password Entry box
    code = Entry(frame, width=25, fg="black",border=0, bg="white", font=("Microsoft YaMel U1 Light",11))
    code.place(x=40, y=150)
    code.insert(0,"Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    #A Border Line under entry columns
    Frame(frame, width=250, height=1, bg="black").place(x=40, y=110)
    Frame(frame, width=250, height=1, bg="black").place(x=40, y=170)

    #SignIn Button
    Button(frame, width=15, pady=7, text="Sign In", bg="#57a1f8", fg="white",cursor="hand2", border=0, command=signin).place(x=80, y= 204)


    #Dont have an account?
    signup_label = Label(frame, text="Don't have an account?", fg="Black", bg="White", font=("Microsoft YaMel U1 Light",9))
    signup_label.place(x=50, y=250)
    signup_label2 = Label(frame, text="SignUp", fg="black", bg="white", font=("Microsoft YaMel U1 Light", 9))
    signup_label2.place(x=190, y=250)
    si.mainloop()