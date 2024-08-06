from tkinter import *
from PIL import ImageTk, Image
import joblib
import pandas as pd
import tensorflow as tf





users = {}
model_path = "Models\Pass-strength-Predictor"
model = tf.keras.models.load_model(model_path)
# model = joblib.load("Models/Pass_stren_predictor.joblib")



def pass_to_df(password): #A function to make dataframe from a password for make the prediction.
    dic = {}
    length = len(password)
    char = 0
    dig = 0
    sym = 0
    for i in password:
        if i.isalpha():
            char += 1
        elif i.isdigit():
            dig += 1
        else:
            sym += 1

    dic["Length"] = [length]   # Adding Key Value pair to the dic dictionary
    dic["Characters"] = [char]
    dic["Digits"] = [dig]
    dic["Symbols"] = [sym]

    to_df = pd.DataFrame(dic) # Converting the dic to dataframe
    return to_df # Returning dataframe





def open_signup_window():


    su = Tk()
    su.geometry("700x500")
    su.resizable(False, False)
    su.title("SignUp Page")
    su.config(bg="white")

    #Image
    img1 = Image.open("/Users/user/OneDrive/Desktop/VSCode Python/Dependencies/signup.jpg")
    img1 = img1.resize((330,330))
    img1 = ImageTk.PhotoImage(img1)
    panel = Label(su, image = img1, borderwidth=0)
    panel.place(x=55, y=85)


    def signup():
        global username, password
        username = user.get()
        Frame(frame, width=92, height=20, bg="white").place(x=40, y=93)
        Frame(frame, width=300, height=35, bg="white").place(x=40, y=140)
        Frame(frame, width=150, height=20, bg="white").place(x=40, y=198)
        if username == "Username" or username == "":
            Label(frame, text="Enter username", fg="red", bg="white", font=("Microsoft YaMel U1 Light",9)).place(x=40, y=93)
        else:
            user_name = user.get()
            password = code.get()
            df_pass = pass_to_df(password)
            pas_strength = model.predict(df_pass)
            if pas_strength == 0:
                Label(frame, text="Weak Password, Use numbers, alphabets and\nsymbols to increase strength.", bg="white", fg="red", font=("Microsoft YaMel U1 Light", 8)).place(x=35, y=140)
            else:
                if pas_strength == 1:
                    Label(frame, text="Password Status :", bg="white", fg="black", font=("Microsoft YaMel U1 Light", 8)).place(x=35, y=140)
                    Label(frame, text="Good", bg="white", fg="green", font=("Microsoft YaMel U1 Light", 8)).place(x=130, y=140)
                elif pas_strength == 2:
                    Label(frame, text="Password Status :", bg="white", fg="black", font=("Microsoft YaMel U1 Light", 8)).place(x=35, y=140)
                    Label(frame, text="Strong", bg="white", fg="violet", font=("Microsoft YaMel U1 Light", 8)).place(x=130, y=140)
                pass_word = code.get()
                confirm_code = re_code.get()
                if confirm_code == "Re-Enter Password" or "":
                    Label(frame, text="Confirm Password", fg="red", bg="white", font=("Microsoft YaMel U1 Light", 9)).place(x=40, y=198)
                elif pass_word != confirm_code:
                    Label(frame, text="Confirm Password", fg="red", bg="white", font=("Microsoft YaMel U1 Light", 9)).place(x=40, y=198)
                else:
                    users[user_name] = pass_word
                    Label(frame, text="Account Created. Signup Succesful", fg="green", bg="white", font=("Microsoft YaMel U1 Light",9)).place(x = 40, y=280)
                    print(users)



    frame = Frame(su, width=300, height=300, bg="White")
    frame.place(x=380, y=80)

    #SignUp Heading
    heading = Label(su, text="SignUp", fg="#57a1f8", bg="white", font=("Microsoft YaMel U1 Light", 22, "bold"))
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
    user.place(x=40, y=70)
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
    code.place(x=40, y=120)
    code.insert(0,"Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)


    def on_enter(e):
        re_code.delete(0, "end")

    def on_leave(e):
        confirm = re_code.get()
        if confirm == "":
            re_code.insert(0, "Re-Enter Password")


    #Confirm password Entry Box
    re_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaMel U1 Light",11))
    re_code.place(x=40, y=178)
    re_code.insert(0, "Re-Enter Password")
    re_code.bind("<FocusIn>", on_enter)
    re_code.bind("FocusOut", on_leave)

    #A Border Line under entry columns
    Frame(frame, width=250, height=1, bg="black").place(x=40, y=90)
    Frame(frame, width=250, height=1, bg="black").place(x=40, y=138)
    Frame(frame, width=250, height=1, bg="black").place(x=40, y=196)


    #SignUp Button
    Button(frame, width=15, pady=7, text="SignUp", bg="#57a1f8", fg="white", border=0, command=signup).place(x=80, y= 230)


    





    su.mainloop()
