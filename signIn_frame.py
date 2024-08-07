import customtkinter as ctk
from main import switch_frames



def switch_frames(frame_to_oepn):
    
    if frame_to_oepn == 'signin':
        frame_to_oepn = signUpFrame
    
    elif current_frame == 'signup':
        current_frame = signUpFrame
        frame_to_oepn = signInFrame


def SignInFrame(master, height: int =500, width: int = 500, firstColor: str = None, 
                secondaryColor: str = None):
    
    
    
    main_frame = ctk.CTkFrame(master, width=width, height=height, fg_color=firstColor)
    main_frame.place(x=0, y=0)
    
    switch_button = ctk.CTkButton(main_frame, text='switch frames', fg_color='red', command= lambda: switch_frames('signin'))
    switch_button.place(x = 100, y=50)
    
    form_frame = ctk.CTkFrame(main_frame, width=100, height=100, fg_color='red')
    form_frame.place(x=50, y=50)
    
    return main_frame