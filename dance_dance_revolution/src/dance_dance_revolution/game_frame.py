import tkinter as tk
import scrolling_arrows_canvas as sac
import right_canvas as rc

class Game_Frame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(
            width=master.winfo_width(),
            height=master.winfo_height(),
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)  
        self.grid_rowconfigure(0, weight=1)
        self.pack_propagate(False)

        #Create scrolling arrows canvas on left side
        self.left_canvas = sac.Scrolling_Arrows_Canvas(self)
        self.left_canvas.grid(row=0, column=0, sticky="nsew")

        #Create right canvas on right side
        self.right_canvas = rc.right_Canvas(self)
        self.right_canvas.grid(row=0, column=1, sticky="nsew")


#Create test window to display the game_Frame
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Game Frame Test")
    root.geometry("600x400")
    game_frame = Game_Frame(root)
    game_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
        





