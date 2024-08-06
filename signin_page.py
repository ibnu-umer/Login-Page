import customtkinter as ctk
from PIL import ImageTk, Image
# from signup_page import users
# from signup_page import open_signup_window




def open_signin_window():


    si = ctk.CTk()
    si.geometry("700x500")
    si.resizable(False, False)
    si.title("SignIn Page")
    si.config(background="white")

    #Login Page Image setup
    # img = Image.open("/Users/user/OneDrive/Desktop/VSCode Python/Dependencies/loginimage.jpg")
    # img = img.resize((330,330))
    # img_log = ImageTk.PhotoImage(img)
    # panel = ctk.CTkLabel(si, image=img_log, borderwidth=0)
    # panel.place(x=55, y=85)


    # users.update({"riyas":"riyas777", "rishana":"rinu@123", "Shamil":"shanumon", "Shaha":"shaimol"})



    #Sign In Function
    def signin():
        global username, password
        username = user.get()
        # ctk.CTkFrame(frame, width=150, height=20, bg_color="white").place(x=40, y=112)
        # ctk.CTkFrame(frame, width=92, height=20, bg_color="white").place(x=40, y=173)
        
        # if username == "Username" or username == "":
        #     ctk.CTkLabel(frame, text="Enter username", fg_color="red", bg_color="white", font=("Microsoft YaMel U1 Light",9)).place(x=40, y=112)
        # elif username in users.keys():
        #     password = code.get()
        #     if password == "Password" or password == "":
        #         ctk.CTkFrame(frame, width=200, height=20, bg_color="white").place(x=40, y=173)
        #         ctk.CTkLabel(frame, text="Enter Password", fg_color="red", bg_color="white", font=("Microsoft YaMel U1 Light",9)).place(x=40, y=172)
        #     else:
        #         if password == users.get(username):
        #             password = code.get()
        #             ctk.CTkLabel(frame, text="Login Succesfull", fg_color="green", bg_color="white").place(x=70, y= 280)
        #         else:
        #             ctk.CTkFrame(frame, width=170, height=20, bg_color="white").place(x=40, y=173)
        #             ctk.CTkLabel(frame, text="Wrong Password", fg_color="red", bg_color="white", font=("Microsoft YaMel U1 Light",9)).place(x=40, y=172)
        # elif username not in [users.keys()]:
        #     ctk.CTkLabel(frame, text="Username not found!", fg_color="red", bg_color="white", font=("Microsoft YaMel U1 Light",9)).place(x=40, y=112)



    #Frame
    frame = ctk.CTkFrame(si, width=300, height=400, bg_color="white", fg_color='white', border_width=1)
    frame.configure(border_color='gray')
    frame.place(x=350, y=50)

    #SignIp Heading
    heading = ctk.CTkLabel(si, text="Sign In", fg_color="white", bg_color="white",
                           font=("Microsoft YaMel U1 Light", 32, "bold"))
    heading.configure(text_color="#57a1f8")
    heading.place(x=445, y=30)

    #Functions to make username visible and invisible
    def on_enter(e):
        name = user.get()
        if name == "Username":
            user.delete(0, "end")

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "Username")


    #Username entry box
    user = ctk.CTkEntry(frame, width=260, height=35, fg_color="white", bg_color="white",
                        font=("Microsoft YaMel U1 Light",13))
    user.place(x=20, y=60)
    user.insert(0,"Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    user.configure(text_color='black')

    #Functions to make Password visible and invisible
    def on_enter(e):
        password = code.get()
        if password == "Password":
            code.delete(0, "end")

    def on_leave(e):
        password = code.get()
        if password == "":
            code.insert(0, "Password")


    #Password Entry box
    code = ctk.CTkEntry(frame, width=260, height=35, fg_color="white", bg_color="white",
                        font=("Microsoft YaMel U1 Light",13))
    code.place(x=20, y=120)
    code.configure(text_color='black')
    code.insert(0,"Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    #A Border Line under entry columns
    # ctk.CTkFrame(frame, width=250, height=1, bg_color="black").place(x=40, y=110)
    # ctk.CTkFrame(frame, width=250, height=1, bg_color="black").place(x=40, y=170)

    #SignIn Button
    sign_button = ctk.CTkButton(frame, width=150, height=35, text="Sign In", font=("Helvetica", 22, "bold"),
                                corner_radius=70, bg_color="white", fg_color="#57a1f8",cursor="hand2",
                                command=signin)
    sign_button.configure(text_color='white')
    sign_button.place(x=70, y= 240)


    #Dont have an account?
    signup_label = ctk.CTkLabel(frame, text="Don't have an account?", fg_color="white", bg_color="White",
                                font=("Microsoft YaMel U1 Light",9))
    signup_label.configure(text_color='gray')
    signup_label.place(x=70, y=320)
    
    signup_button = ctk.CTkButton(frame, width=15, height=10, text="SignUp", fg_color="white", bg_color="white",
                                  cursor='hand2', font=("Microsoft YaMel U1 Light", 9), hover_color='#b3ccff',
                                  )
    signup_button.configure(text_color='gray')
    signup_button.place(x=172, y=326)
    
    
    si.mainloop()
    
    
open_signin_window()