import customtkinter as ctk
from PIL import ImageTk, Image
import joblib



users = {"riyas":"riyas777", "rishana":"rinu@123", "Shamil":"shanumon", "Shaha":"shaimol", "a":"aaa"}

def pass_prep(password):
    length = len(password)
    char, dig, sym = 0, 0, 0
    
    for i in password:
        if i.isalpha():
            char += 1
        elif i.isdigit():
            dig += 1
        else:
            sym += 1

        return [[length, char, dig, sym]]


def open_signup_window():

    su = ctk.CTk()
    su.geometry("700x500")
    su.resizable(False, False)
    su.title("SignUp Page")
    su.config(background="white")

    # Image
    img = ctk.CTkImage(light_image=Image.open("static/log_image.jpeg"), size=(300, 300))
    panel = ctk.CTkLabel(su, text='', image=img)
    panel.place(x=25, y=115)

    signup_status = False

    def signup():
        
        global username, password, signup_status
        
        # Frames to hide the prev warning messages or entry columns
        ctk.CTkFrame(frame, width=140, height=20, bg_color="white", fg_color='white').place(x=25, y=105)
        ctk.CTkFrame(frame, width=140, height=20, bg_color="white", fg_color='white').place(x=25, y=166)
        ctk.CTkFrame(frame, width=140, height=20, bg_color="white", fg_color='white').place(x=25, y=223)

        username = user.get()
        
        if username == "Username" or username == "":
            username_empty_errror = ctk.CTkLabel(frame, text=" ! Enter username", height=10, fg_color="white",
                                            bg_color="white", font=("Microsoft YaMel U1 Light",9))
            username_empty_errror.configure(text_color='red')
            username_empty_errror.place(x=25, y=110)
       
        elif username in users.keys():
            username_exist_errror = ctk.CTkLabel(frame, text=" ! Username Already Exist", height=10, fg_color="white",
                                            bg_color="white", font=("Microsoft YaMel U1 Light",9))
            username_exist_errror.configure(text_color='red')
            username_exist_errror.place(x=25, y=110)
        
        else:
            user_name = user.get()
            password = code.get()
            
            if password == "Password" or password == "":
                password_empty_error = ctk.CTkLabel(frame, text=" ! Enter Password", height=10, fg_color="white",
                                            bg_color="white", font=("Microsoft YaMel U1 Light",9))
                password_empty_error.configure(text_color='red')
                password_empty_error.place(x=25, y=170)
                
            else:
                # pass_prep = pass_prep(password)
                pass_strength = 2 # model.predict(pass_prep)
                
                if pass_strength == 0:
                    pass_status = "Weak"
                    weak_pass = ctk.CTkLabel(frame, text=f" ! Passowrd Status : {pass_status}", height=10, fg_color="white",
                                                bg_color="white", font=("Microsoft YaMel U1 Light",9))
                    weak_pass.configure(text_color='red')
                    weak_pass.place(x=25, y=170)
                
                else:
                    if pass_strength == 1:
                        pass_status = "Good"
                        
                    elif pass_strength == 2:
                        pass_status = "Strong"
                        
                    approved_pass = ctk.CTkLabel(frame, text=f" ! Passowrd Status : {pass_status}", height=10, fg_color="white",
                                                bg_color="white", font=("Microsoft YaMel U1 Light",9))
                    approved_pass.configure(text_color='green')
                    approved_pass.place(x=25, y=170)

                password = code.get()
                confirm_code = re_code.get()
                
                if confirm_code == "Re-Enter Password" or confirm_code == "":
                    recode_empty_error = ctk.CTkLabel(frame, text=" ! Confirm Password", fg_color="white",
                                                      bg_color="white", font=("Microsoft YaMel U1 Light", 9))
                    recode_empty_error.configure(text_color='red')
                    recode_empty_error.place(x=25, y=223)
                    
                elif password != confirm_code:
                    recode_match_error = ctk.CTkLabel(frame, text=" ! Password Mismatch", fg_color="white",
                                                      bg_color="white", font=("Microsoft YaMel U1 Light", 9))
                    recode_match_error.configure(text_color='red')
                    recode_match_error.place(x=25, y=223)
                    
                else:
                    users[user_name] = password
                    su.destroy()
                    

    # The Form container
    frame = ctk.CTkFrame(su, width=300, height=400, bg_color="White",
                         fg_color='white', border_width=1, border_color='gray')
    frame.place(x=360, y=50)

    #SignUp Heading
    heading = ctk.CTkLabel(su, text="Sign Up", fg_color="white", bg_color="white",
                           font=("Microsoft YaMel U1 Light", 32, "bold"))
    heading.configure(text_color="#57a1f8")
    heading.place(x=455, y=29)


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
    user.place(x=20, y=70)
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
    code.place(x=20, y=130)
    code.insert(0,"Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)
    code.configure(text_color='black')
    


    def on_enter(e):
        confirm = re_code.get()
        if confirm ==  "Re-Enter Password":
            re_code.delete(0, "end")

    def on_leave(e):
        confirm = re_code.get()
        if confirm == "":
            re_code.insert(0, "Re-Enter Password")


    #Confirm password Entry Box
    re_code = ctk.CTkEntry(frame, width=260, height=35, fg_color="white", bg_color="white",
                        font=("Microsoft YaMel U1 Light",13))
    re_code.configure(text_color='black')
    re_code.insert(0, "Re-Enter Password")
    re_code.bind("<FocusIn>", on_enter)
    re_code.bind("<FocusOut>", on_leave)
    re_code.place(x=20, y=188)


    # SignUp Button
    sign_button = ctk.CTkButton(frame, width=150, height=35, text="Sign Up", font=("Helvetica", 22, "bold"),
                            corner_radius=70, bg_color="white", fg_color="#57a1f8",cursor="hand2",
                            command=signup)
    sign_button.configure(text_color='white')
    sign_button.place(x=70, y= 260)


    # Already have an account?
    already_label = ctk.CTkLabel(frame, text="Already have an account?", fg_color="white", bg_color="White",
                                font=("Microsoft YaMel U1 Light",9))
    already_label.configure(text_color='gray')
    already_label.place(x=70, y=340)
    
    signin_button = ctk.CTkButton(frame, width=15, height=10, text="Sign In", fg_color="white", bg_color="white",
                                  cursor='hand2', font=("Microsoft YaMel U1 Light", 9), hover_color='#b3ccff',
                                  )
    signin_button.configure(text_color='gray')
    signin_button.place(x=182, y=346)
    

    su.mainloop()


if __name__ == "__main__":
    open_signup_window()