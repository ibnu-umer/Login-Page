import customtkinter as ctk


def SignUpFrame(master, height: int =500, width: int = 500, firstColor: str = None, 
                secondaryColor: str = None):
    
    main_frame = ctk.CTkFrame(master, width=width, height=height, fg_color=firstColor)
    main_frame.place(x=0, y=0)
    
    form_frame = ctk.CTkFrame(main_frame, width=100, height=100, fg_color=secondaryColor)
    form_frame.place(x=50, y=50)
    
    return main_frame