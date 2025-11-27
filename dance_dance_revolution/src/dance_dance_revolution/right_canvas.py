import tkinter as tk
from typing import Callable, Dict, List, Optional
import scrolling_arrows_canvas as sac
import get_from_files as gff

class right_Canvas(tk.Canvas):
    def __init__(
        self,
        master: tk.Frame,     
        *args,
        **kwargs,
    ):
        super().__init__(master, *args, **kwargs)
        self.config(
            highlightthickness=0, #This is what actually takes away the border
            bg=gff.get_right_canvas_background_color(), #cahnge the name to canvas background color later
            width=master.winfo_width()//2,
            height=gff.get_window_height(),
            



            #divide frame into four equal columns
            # and 1 row
            
            #width=gff.get_window_width() // 2, #this needs to be adjusted because the current size does not 
            #height=gff.get_window_height(),    #take into account the extra parts of the window like title bar and borders
            
            )
        self.pack_propagate(False)
        self.grid(row=0, column=0, sticky="nsew")


#Create test window to display the Scrolling_Arrows_Frame
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scrolling Arrows Frame Test")
    root.geometry("600x400")
    new_frame = tk.Frame(root)
    new_frame.pack(fill=tk.BOTH, expand=True)
    new_frame.grid_columnconfigure(0, weight=1)
    new_frame.grid_columnconfigure(1, weight=1) 
    new_frame.grid_rowconfigure(0, weight=1)
    
    
    

    canvas = right_Canvas(new_frame)
    canvas2 = sac.Scrolling_Arrows_Canvas(new_frame)
    canvas.grid(row=0, column=0, sticky="nsew")
    canvas2.grid(row=0, column=1, sticky="nsew")

    root.mainloop()