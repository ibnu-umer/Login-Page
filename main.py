import customtkinter as ctk
from PIL import Image



class App:
    
    def __init__(self, appearance_mode: str = None, geometry: str = '500x500', title : str = None,
                 resizable : bool = None, frame_width: int = None, frame_height: int = None,
                 first_color: str = None, secondary_color: str = None):
        
        self.appearance_mode = appearance_mode
        self.geometry = geometry
        self.title = title
        self.resizable = resizable
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.first_color = first_color
        self.secondary_color = secondary_color
        self.login_status = False
        self.users = {"riyas":"riyas777", "rishana":"rinu@123", "Shamil":"shanumon", "Shaha":"shaimol", "a":"aaa"}
        
        
        # Theme
        ctk.set_appearance_mode(self.appearance_mode)
        
        self.app = ctk.CTk()
        self.app.title(self.title)
        self.app.geometry(self.geometry)
        self.app.resizable(height=self.resizable, width=self.resizable)
        
        
        self.signin_frame = self.SignInFrame(self.app, height=self.frame_height, width=self.frame_width)
        self.signup_frame = self.SignUpFrame(self.app, height=self.frame_height, width=self.frame_width)
        self.homepage = self.HomePage(self.app, height=self.frame_height, width=self.frame_width)
        
        self.homepage.place(x=0, y=0)
    
    
    
    
        self.app.mainloop()
        
        
        
        
    def SignInFrame(self, master, height: int = None, width: int = None):
        
        mainFrame = ctk.CTkFrame(master, height=height, width=width, fg_color=self.first_color)
        
        # Main Image
        img = ctk.CTkImage(light_image=Image.open("static/log_image.jpeg"), size=(300, 300))
        img_frame = ctk.CTkLabel(mainFrame, text='', image=img)
        img_frame.place(x=25, y=115)
        
        # Form Frame
        frame = ctk.CTkFrame(mainFrame, width=300, height=400, bg_color="white", fg_color='white', border_width=1)
        frame.configure(border_color='gray')
        frame.place(x=350, y=50)
        
        # SignIn Heading
        heading = ctk.CTkLabel(mainFrame, text="Sign In", fg_color="white", bg_color="white",
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
        user = ctk.CTkEntry(frame, width=260, height=35, fg_color="white", bg_color="white",
                            font=("Microsoft YaMel U1 Light",13))
        user.place(x=20, y=60)
        user.insert(0,"Username")
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)
        user.configure(text_color='black')
        
        
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
        code = ctk.CTkEntry(frame, width=260, height=35, fg_color="white", bg_color="white",
                            font=("Microsoft YaMel U1 Light",13))
        code.place(x=20, y=120)
        code.configure(text_color='black')
        code.insert(0,"Password")
        code.bind("<FocusIn>", on_enter)
        code.bind("<FocusOut>", on_leave)
        
        
        # Sign In Function
        def signin():
            global username, password
            username = user.get()
            
            # The frame to display and hide error showing in the password or username.
            frame1 = ctk.CTkFrame(frame, width=150, height=20, bg_color="white", fg_color='white')
            frame1.place(x=25, y=97)
            
            if username == "Username" or username == "":
                username_empty_errror = ctk.CTkLabel(frame, text=" ! Enter username", height=10, fg_color="white",
                                                bg_color="white", font=("Microsoft YaMel U1 Light",9))
                username_empty_errror.configure(text_color='red')
                username_empty_errror.place(x=25, y=100)
                
            elif username in self.users.keys():
                password = code.get()
                
                if password == "Password" or password == "":
                    ctk.CTkFrame(frame, width=150, height=20, bg_color="white", fg_color='white').place(x=25, y=155)
                    password_empty_error = ctk.CTkLabel(frame, text=" ! Enter Password", height=10, 
                                                        fg_color="white", bg_color="white", font=("Microsoft YaMel U1 Light",9))
                    password_empty_error.configure(text_color='red')
                    password_empty_error.place(x=25, y=158)
                    
                else:
                    
                    if password == self.users.get(username):
                        # Closing the current frame and opening the homepage
                        self.login_status = True
                        self.swith_frame(mainFrame, self.homepage)
                        
                    else:
                        ctk.CTkFrame(frame, width=150, height=20, bg_color="white", fg_color='white').place(x=25, y=155)
                        password_error = ctk.CTkLabel(frame, text=" ! Wrong Password Entered", height=10, 
                                                            fg_color="white", bg_color="white", font=("Microsoft YaMel U1 Light",9))
                        password_error.configure(text_color='red')
                        password_error.place(x=25, y=158)
                        
            elif username not in self.users.keys():
                user_not_found = ctk.CTkLabel(frame, height=10, text=" ! Username not found", fg_color="white", bg_color="white",
                                            font=("Microsoft YaMel U1 Light",9))
                user_not_found.configure(text_color='red')
                user_not_found.place(x=25, y=100)
        

        # SignIn Button
        sign_button = ctk.CTkButton(frame, width=150, height=35, text="Sign In", font=("Helvetica", 22, "bold"),
                                    corner_radius=70, bg_color="white", fg_color="#57a1f8",cursor="hand2",
                                    command=signin)
        sign_button.configure(text_color='white')
        sign_button.place(x=70, y= 240)
        

        # Dont have an account?
        signup_label = ctk.CTkLabel(frame, text="Don't have an account?", fg_color="white", bg_color="White",
                                    font=("Microsoft YaMel U1 Light",9))
        signup_label.configure(text_color='gray')
        signup_label.place(x=75, y=320)
        
        signup_button = ctk.CTkButton(frame, width=15, height=10, text="SignUp", fg_color="white", bg_color="white",
                                    cursor='hand2', font=("Microsoft YaMel U1 Light", 9), hover_color='#b3ccff',
                                    command= lambda: self.swith_frame(mainFrame, 'signup'))
        signup_button.configure(text_color='gray')
        signup_button.place(x=178, y=326)
            
        
        return mainFrame
    
    
    
    def SignUpFrame(self, master, height: int = None, width: int = None):
        
        mainFrame = ctk.CTkFrame(master, height=height, width=width, fg_color=self.first_color)
        
        # Main Image
        img = ctk.CTkImage(light_image=Image.open("static/log_image.jpeg"), size=(300, 300))
        img_frame = ctk.CTkLabel(mainFrame, text='', image=img)
        img_frame.place(x=25, y=115)
        
        
        
        switch = ctk.CTkButton(mainFrame, command= lambda: self.swith_frame(mainFrame, 'homepage'))
        switch.place(x=100, y=100)
        
        return mainFrame
    
    
    def HomePage(self, master, height: int = None, width: int = None):
        
        mainFrame = ctk.CTkFrame(master, height=height, width=width, fg_color=self.first_color)
        
        if self.login_status == False:
            
            #Signin and Signup buttons
            signin_button = ctk.CTkButton(mainFrame, width=80, height=35, text="Sign UP", font=("Helvetica", 18, "bold"),
                        fg_color="blue", bg_color="black", cursor="hand2",
                        command=lambda: self.swith_frame(mainFrame, 'signin'))
            signin_button.place(x=600, y=10)
            
            signup_button = ctk.CTkButton(mainFrame, width=80, height=35, text="Sign In", font=("Helvetica", 18, "bold"),
                        fg_color="gray", bg_color="black", cursor="hand2",
                        command=lambda: self.swith_frame(mainFrame, 'signup'))
            signup_button.place(x=500, y=10)
        
        
        return mainFrame
        
    
    
    def swith_frame(self, current_frame, frame_to_open):
        
        current_frame.place_forget()
        if frame_to_open == 'signup':
            self.signup_frame = self.SignUpFrame(self.app, height=self.frame_height, width=self.frame_width)
            self.signup_frame.place(x=0, y=0)
        
        elif frame_to_open == 'signin':
            self.signin_frame = self.SignInFrame(self.app, height=self.frame_height, width=self.frame_width)
            self.signin_frame.place(x=0, y=0)
            
        else:
            self.homepage = self.HomePage(self.app, height=self.frame_height, width=self.frame_width)
            self.homepage.place(x=0, y=0)
        
        
        
        
        
        
        
app = App(
        appearance_mode='light',
        geometry='700x500',
        title='An self.App',
        resizable=False,
        frame_width=700,
        frame_height=500,
        first_color='white',
        secondary_color='black'
          )