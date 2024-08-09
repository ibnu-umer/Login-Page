import customtkinter as ctk
from PIL import Image
import time
import ast
from tensorflow.keras.models import load_model
import numpy as np



class App:
    
    def __init__(self, appearance_mode: str = None, title : str = None):
        
        self.appearance_mode = appearance_mode
        self.geometry = '700x500'
        self.title = title
        self.resizable = False
        self.frame_width = 700
        self.frame_height = 500
        
        self.login_status = False
        
        # Fetching data from the database
        data = open('database.txt', 'r')
        data = data.read()
        # Convert the string to a dictionary
        self.users = ast.literal_eval(data)

        self.user = None
        
        # Color setting
        if appearance_mode == "dark":
            self.first_color = 'black'
            self.secondary_color = 'white'
        else:
            self.first_color = 'white'
            self.secondary_color = 'black'
        
        # Loading the password strength predicting model
        self.pas_stren_model = load_model('models/Pass-stren-pred-Model.keras')
        
        
        # Mode of the app
        ctk.set_appearance_mode(self.appearance_mode)
        
        # Initialising app window
        self.app = ctk.CTk()
        self.app.title(self.title)
        self.app.geometry(self.geometry)
        self.app.resizable(height=self.resizable, width=self.resizable)
        
        self.homepage = self.HomePage()
        self.homepage.place(x=0, y=0)
        
        self.app.mainloop()
   
        
    def SignInFrame(self):
        
        mainFrame = ctk.CTkFrame(self.app, height=self.frame_height, width=self.frame_width, fg_color=self.first_color)
        
        # Main Image
        img = ctk.CTkImage(light_image=Image.open("static/signin_img.png"), size=(300, 300))
        img_frame = ctk.CTkLabel(mainFrame, text='', image=img)
        img_frame.place(x=25, y=100)
        
        # Form Frame
        frame = ctk.CTkFrame(mainFrame, width=300, height=400, bg_color=self.first_color, fg_color=self.first_color, border_width=1)
        frame.configure(border_color='gray')
        frame.place(x=350, y=50)
        
        # SignIn Heading
        heading = ctk.CTkLabel(mainFrame, text="Sign In", fg_color=self.first_color, bg_color=self.first_color,
                                font=("Microsoft YaMel U1 Light", 32, "bold"))
        heading.configure(text_color="#57a1f8")
        heading.place(x=445, y=30)
        
        
        # Functions to make username visible and invisible
        def on_enter(e):
            name = user.get()
            if name == "Username":
                user.delete(0, "end")

        def on_leave(e):
            name = user.get()
            if name == "":
                user.insert(0, "Username")

        # Username entry box
        user = ctk.CTkEntry(frame, width=260, height=35, fg_color=self.first_color, bg_color=self.first_color,
                            font=("Microsoft YaMel U1 Light",13))
        user.place(x=20, y=60)
        user.insert(0,"Username")
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)
        user.configure(text_color=self.secondary_color)
        
        
        # Functions to make Password visible and invisible
        def on_enter(e):
            password = code.get()
            if password == "Password":
                code.delete(0, "end")

        def on_leave(e):
            password = code.get()
            if password == "":
                code.insert(0, "Password")


        # Password Entry box
        code = ctk.CTkEntry(frame, width=260, height=35, fg_color=self.first_color, bg_color=self.first_color,
                            font=("Microsoft YaMel U1 Light",13))
        code.place(x=20, y=120)
        code.configure(text_color=self.secondary_color)
        code.insert(0,"Password")
        code.bind("<FocusIn>", on_enter)
        code.bind("<FocusOut>", on_leave)
        
        
        # Sign In Function
        def signin():
            global username, password
            username = user.get()
            
            # The frame to display and hide error showing in the password or username.
            frame1 = ctk.CTkFrame(frame, width=150, height=20, bg_color=self.first_color, fg_color=self.first_color)
            frame2 = ctk.CTkFrame(frame, width=150, height=20, bg_color=self.first_color, fg_color=self.first_color)
            frame1.place(x=25, y=97)
            frame2.place(x=25, y=155)
            
            if username == "Username" or username == "":
                username_empty_errror = ctk.CTkLabel(frame1, text=" ! Enter username", height=10, fg_color=self.first_color,
                                                bg_color=self.first_color, font=("Microsoft YaMel U1 Light",9))
                username_empty_errror.configure(text_color='red')
                username_empty_errror.place(x=0, y=3)
                
            elif username in self.users.keys():
                password = code.get()
                
                if password == "Password" or password == "":
                    password_empty_error = ctk.CTkLabel(frame2, text=" ! Enter Password", height=10, 
                                                        fg_color=self.first_color, bg_color=self.first_color, font=("Microsoft YaMel U1 Light",9))
                    password_empty_error.configure(text_color='red')
                    password_empty_error.place(x=0, y=3)
                    
                else:
                    
                    if password == self.users.get(username):
                        # Closing the current frame and opening the homepage
                        self.login_status = True
                        self.user = username
                        self.switch_frames(mainFrame, self.homepage)
                        
                    else:
                        ctk.CTkFrame(frame2, width=150, height=20, bg_color=self.first_color, fg_color=self.first_color).place(x=25, y=155)
                        password_error = ctk.CTkLabel(frame2, text=" ! Wrong Password Entered", height=10, 
                                                            fg_color=self.first_color, bg_color=self.first_color, font=("Microsoft YaMel U1 Light",9))
                        password_error.configure(text_color='red')
                        password_error.place(x=0, y=3)
                        
            elif username not in self.users.keys():
                user_not_found = ctk.CTkLabel(frame1, height=10, text=" ! Username not found", fg_color=self.first_color, bg_color=self.first_color,
                                            font=("Microsoft YaMel U1 Light",9))
                user_not_found.configure(text_color='red')
                user_not_found.place(x=0, y=3)
        

        # SignIn Button
        sign_button = ctk.CTkButton(frame, width=150, height=35, text="Sign In", font=("Helvetica", 22, "bold"),
                                    corner_radius=70, bg_color=self.first_color, fg_color="#57a1f8",cursor="hand2",
                                    command=signin)
        sign_button.configure(text_color='white')
        sign_button.place(x=70, y= 260)
        

        # Dont have an account?
        signup_label = ctk.CTkLabel(frame, text="Don't have an account?", fg_color=self.first_color, bg_color=self.first_color,
                                    font=("Microsoft YaMel U1 Light",9))
        signup_label.configure(text_color='gray')
        signup_label.place(x=75, y=320)
        
        signup_button = ctk.CTkButton(frame, width=15, height=10, text="SignUp", fg_color=self.first_color, bg_color=self.first_color,
                                    cursor='hand2', font=("Microsoft YaMel U1 Light", 9), hover_color='#b3ccff',
                                    command= lambda: self.switch_frames(mainFrame, 'signup'))
        signup_button.configure(text_color='gray')
        signup_button.place(x=178, y=326)
        
        
        # Back Button
        back_img = ctk.CTkImage(light_image=Image.open('static/back_button.png'), dark_image=Image.open('static/back_button_1.png'),
                                size=(20,20))
        back_button = ctk.CTkButton(mainFrame, text='', width=10, height=10, image=back_img, cursor='hand2', 
                                    fg_color=self.first_color, bg_color=self.first_color, hover=False,
                                    command=lambda : self.switch_frames(mainFrame, 'homepage'))
        back_button.place(x=10, y=10)
            
        
        return mainFrame
    
    
    def SignUpFrame(self):
        
        mainFrame = ctk.CTkFrame(self.app, height=self.frame_height, width=self.frame_width, fg_color=self.first_color)
        
        # Main Image
        img = ctk.CTkImage(light_image=Image.open("static/signup_img.png"), size=(300, 300))
        img_frame = ctk.CTkLabel(mainFrame, text='', image=img)
        img_frame.place(x=25, y=100)
        
        
        # The Form container
        frame = ctk.CTkFrame(mainFrame, width=300, height=400, bg_color=self.first_color,
                            fg_color=self.first_color, border_width=1, border_color='gray')
        frame.place(x=350, y=50)

        #SignUp Heading
        heading = ctk.CTkLabel(mainFrame, text="Sign Up", fg_color=self.first_color, bg_color=self.first_color,
                            font=("Microsoft YaMel U1 Light", 32, "bold"))
        heading.configure(text_color="#57a1f8")
        heading.place(x=442, y=30)


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
        user = ctk.CTkEntry(frame, width=260, height=35, fg_color=self.first_color, bg_color=self.first_color,
                            font=("Microsoft YaMel U1 Light",13))
        user.place(x=20, y=60)
        user.insert(0,"Username")
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)
        user.configure(text_color=self.secondary_color)


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
        code = ctk.CTkEntry(frame, width=260, height=35, fg_color=self.first_color, bg_color=self.first_color,
                            font=("Microsoft YaMel U1 Light",13))
        code.place(x=20, y=120)
        code.insert(0,"Password")
        code.bind("<FocusIn>", on_enter)
        code.bind("<FocusOut>", on_leave)
        code.configure(text_color=self.secondary_color)
    


        def on_enter(e):
            confirm = re_code.get()
            if confirm ==  "Re-Enter Password":
                re_code.delete(0, "end")

        def on_leave(e):
            confirm = re_code.get()
            if confirm == "":
                re_code.insert(0, "Re-Enter Password")


        #Confirm password Entry Box
        re_code = ctk.CTkEntry(frame, width=260, height=35, fg_color=self.first_color, bg_color=self.first_color,
                            font=("Microsoft YaMel U1 Light",13))
        re_code.configure(text_color=self.secondary_color)
        re_code.insert(0, "Re-Enter Password")
        re_code.bind("<FocusIn>", on_enter)
        re_code.bind("<FocusOut>", on_leave)
        re_code.place(x=20, y=180)
        
        
        # Preprocess password and return arr to input to the model
        def prep_pass(password):
            
            length = len(password)
            dig, char, sym = 0, 0, 0 
            
            for i in password:
                
                if i.isdigit():
                    dig += 1
                
                elif i.isalpha():
                    char += 1
                    
                else:
                    sym += 1
            
            list = [[length, char, dig, sym]]
            arr = np.array(list)
            
            return arr
        
        
        def signup():
        
            # Frames to hide the prev warning messages of entry columns
            frame1 = ctk.CTkFrame(frame, width=140, height=20, bg_color=self.first_color, fg_color=self.first_color)
            frame2 = ctk.CTkFrame(frame, width=140, height=20, bg_color=self.first_color, fg_color=self.first_color)
            frame3 = ctk.CTkFrame(frame, width=140, height=20, bg_color=self.first_color, fg_color=self.first_color)
            
            frame1.place(x=25, y=97)
            frame2.place(x=25, y=155)
            frame3.place(x=25, y=216)
            
            username = user.get()
            
            if username == "Username" or username == "":
                username_empty_errror = ctk.CTkLabel(frame1, text=" ! Enter username", height=10, fg_color=self.first_color,
                                                bg_color=self.first_color, font=("Microsoft YaMel U1 Light",9))
                username_empty_errror.configure(text_color='red')
                username_empty_errror.place(x=0, y=3)
        
            elif username in self.users.keys():
                username_exist_errror = ctk.CTkLabel(frame1, text=" ! Username Already Exist", height=10, fg_color=self.first_color,
                                                bg_color=self.first_color, font=("Microsoft YaMel U1 Light",9))
                username_exist_errror.configure(text_color='red')
                username_exist_errror.place(x=0, y=3)
            
            else:
                user_name = user.get()
                password = code.get()
                
                if password == "Password" or password == "":
                    password_empty_error = ctk.CTkLabel(frame2, text=" ! Enter Password", height=10, fg_color=self.first_color,
                                                bg_color=self.first_color, font=("Microsoft YaMel U1 Light",9))
                    password_empty_error.configure(text_color='red')
                    password_empty_error.place(x=0, y=3)
                    
                else:
                    
                    # Predicting password strength using a ML Model
                    prepped_pass = prep_pass(password)
                    pass_strength_conf = self.pas_stren_model.predict(prepped_pass)
                    pass_strength = np.argmax(pass_strength_conf)
                    
                    if pass_strength == 0:
                        pass_status = "Weak"
                        weak_pass = ctk.CTkLabel(frame2, text=f" ! Passowrd Status : {pass_status}", height=10, fg_color=self.first_color,
                                                    bg_color=self.first_color, font=("Microsoft YaMel U1 Light",9))
                        weak_pass.configure(text_color='red')
                        weak_pass.place(x=0, y=3)
                    
                    else:
                        if pass_strength == 1:
                            pass_status = "Good"
                            
                        elif pass_strength == 2:
                            pass_status = "Strong"
                            
                        approved_pass = ctk.CTkLabel(frame2, text=f" ! Passowrd Status : {pass_status}", height=10, fg_color=self.first_color,
                                                    bg_color=self.first_color, font=("Microsoft YaMel U1 Light",9))
                        approved_pass.configure(text_color='green')
                        approved_pass.place(x=0, y=3)

                        password = code.get()
                        confirm_code = re_code.get()
                        
                        if confirm_code == "Re-Enter Password" or confirm_code == "":
                            recode_empty_error = ctk.CTkLabel(frame3, text=" ! Confirm Password", height=10, fg_color=self.first_color,
                                                            bg_color=self.first_color, font=("Microsoft YaMel U1 Light", 9))
                            recode_empty_error.configure(text_color='red')
                            recode_empty_error.place(x=0, y=3)
                            
                        elif password != confirm_code:
                            recode_match_error = ctk.CTkLabel(frame3, text=" ! Password Mismatch", height=10, fg_color=self.first_color,
                                                            bg_color=self.first_color, font=("Microsoft YaMel U1 Light", 9))
                            recode_match_error.configure(text_color='red')
                            recode_match_error.place(x=0, y=3)
                            
                        else:
                            self.users[user_name] = password
                            data = open('database.txt', 'w')
                            data.write(str(self.users))
                            
                            self.user = user_name
                            self.login_status = True

                            time.sleep(1)
                            self.switch_frames(mainFrame, 'homepage')
        


        # SignUp Button
        sign_button = ctk.CTkButton(frame, width=150, height=35, text="Sign Up", font=("Helvetica", 22, "bold"),
                                corner_radius=70, bg_color=self.first_color, fg_color="#57a1f8",cursor="hand2",
                                command=signup)
        sign_button.configure(text_color='white')
        sign_button.place(x=70, y= 260)


        # Already have an account?
        already_label = ctk.CTkLabel(frame, text="Already have an account?", fg_color=self.first_color, bg_color=self.first_color,
                                    font=("Microsoft YaMel U1 Light",9))
        already_label.configure(text_color='gray')
        already_label.place(x=71, y=320)
        
        signin_button = ctk.CTkButton(frame, width=15, height=10, text="Sign In", fg_color=self.first_color, bg_color=self.first_color,
                                    cursor='hand2', font=("Microsoft YaMel U1 Light", 9), hover_color='#b3ccff',
                                    command=lambda : self.switch_frames(mainFrame, 'signin'))
        signin_button.configure(text_color='gray')
        signin_button.place(x=182, y=326)
        
        
        # Back Button
        back_img = ctk.CTkImage(light_image=Image.open('static/back_button.png'), dark_image=Image.open('static/back_button_1.png'),
                                size=(20,20))
        back_button = ctk.CTkButton(mainFrame, text='', width=10, height=10, image=back_img, cursor='hand2', 
                                    fg_color=self.first_color, bg_color=self.first_color, hover=False,
                                    command=lambda : self.switch_frames(mainFrame, 'homepage'))
        back_button.place(x=10, y=10)

        
        return mainFrame
    
    
    def HomePage(self):
        
        mainFrame = ctk.CTkFrame(self.app, height=self.frame_height, width=self.frame_width, fg_color=self.first_color)
        
        # Main Image
        img = ctk.CTkImage(dark_image=Image.open("static/homepage_white.png"), light_image=Image.open('static/homepage.png'), size=(300, 300))
        img_frame = ctk.CTkLabel(mainFrame, text='', image=img)
        img_frame.place(x=200, y=115)
        
        if self.login_status == False:
            
            #Signin and Signup buttons
            signin_button = ctk.CTkButton(mainFrame, width=80, height=35, text="Sign In", font=("Helvetica", 18, "bold"),
                        fg_color="blue", bg_color=self.first_color, cursor="hand2",
                        command=lambda: self.switch_frames(mainFrame, 'signin'))
            signin_button.place(x=600, y=10)
            
            signup_button = ctk.CTkButton(mainFrame, width=80, height=35, text="Sign Up", font=("Helvetica", 18, "bold"),
                        fg_color="gray", bg_color=self.first_color, cursor="hand2",
                        command=lambda: self.switch_frames(mainFrame, 'signup'))
            signup_button.place(x=500, y=10)
            
        else:
            
            logout_button = ctk.CTkButton(mainFrame, width=40, height=10, text='logout', font=('Helvetica', 18),
                                          fg_color=self.first_color, bg_color=self.first_color, cursor='hand2',
                                          command= self.logout)
            logout_button.configure(text_color='red')
            logout_button.place(x=600, y=10)
            
            user_title = ctk.CTkLabel(mainFrame, width=40, height=15, text=f"Hi, {self.user.upper()}",
                                      font=('Helvetica', 23, 'bold'), fg_color="transparent", bg_color="transparent")
            user_title.configure(text_color=self.secondary_color)
            user_title.place(x=15, y=15)
            
        # change mode button
        mode_img = ctk.CTkImage(dark_image=Image.open('static/dark_Mode.png'), light_image=Image.open('static/white_Mode.png'),
                                size=(35, 35))
        mode_button = ctk.CTkButton(mainFrame, text='', image=mode_img, height=15, width=35, corner_radius=60,
                                    fg_color=self.first_color, bg_color=self.first_color, hover_color=self.first_color,
                                    cursor='hand2', command=self.change_mode)
        
        mode_button.place(x=0, y=450)
        
        return mainFrame
        
    
    def switch_frames(self, current_frame, frame_to_open):
        
        current_frame.place_forget()
        if frame_to_open == 'signup':
            self.signup_frame = self.SignUpFrame()
            self.signup_frame.place(x=0, y=0)
        
        elif frame_to_open == 'signin':
            self.signin_frame = self.SignInFrame()
            self.signin_frame.place(x=0, y=0)
            
        else:
            self.homepage = self.HomePage()
            self.homepage.place(x=0, y=0)
               
            
    def logout(self):
        
        self.login_status = False
        time.sleep(1)
        self.homepage.place_forget()
        
        self.homepage = self.HomePage()
        self.homepage.place(x=0, y=0)
 
        
    # Change the appearence mode
    def change_mode(self):
        
        if self.appearance_mode == 'dark':
            self.appearance_mode = 'light'
            ctk.set_appearance_mode(self.appearance_mode)
            self.first_color = 'white'
            self.secondary_color = 'black'
            
        else:
            self.appearance_mode = 'dark'
            ctk.set_appearance_mode(self.appearance_mode)
            self.first_color = 'black'
            self.secondary_color = 'white'
        
        self.homepage.place_forget()
        
        self.homepage = self.HomePage()
        self.homepage.place(x=0, y=0)
        
        
        
def main():
       
    app = App(
            appearance_mode='dark',
            title='Login App'
            )
    
    
if __name__ == '__main__':
    main()