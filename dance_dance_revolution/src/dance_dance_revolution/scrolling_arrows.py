import tkinter as tk
import image_canvas as ic
import game_frame as gf


#this class is how we call the arrow images and make them scroll.
#master is the parent frame
#image_name is the name of the image file
#the full path to the image file is assembeled in the image_processing module

class Scrolling_Arrow(ic.Image_Canvas):
    def __init__(
            self, 
            master: tk.Frame,  
            image_name: str,
            *args, 
            **PI_kwargs
    ):
        super().__init__(master, image_name,*args, **PI_kwargs)
        self.speed = 0  # Placeholder for arrow speed
        self.y_position = 0  # Initial vertical position #future versions will have the arrows start off screen
        self.addtag_withtag(tk.ALL, "arrows")  # Tag to identify the arrow items

    def create_scrolling_arrow(direction:str) -> Scrolling_Arrow:
        #A simple factory function to create scrolling arrows based on direction
        direction_map = {
            "up": ("arrow_basic.png", 0),
            "down": ("arrow_basic.png", 180),
            "left": ("arrow_angled_basic.png", 270),
            "right": ("arrow_angled_basic.png", 90)
        }
        
        if direction in direction_map:
            image_name, rotation = direction_map[direction]
            return Scrolling_Arrow(
                master=None,  # Master will be set when packing into a frame
                image_name=image_name,
                rotate=rotation,
                resize=(40, 40)  # Standard size for arrows
            )
        else:
            raise ValueError(f"Invalid direction '{direction}'. Valid directions are: {list(direction_map.keys())}")

    # Now the keyevent handler can simply call the move method on the arrow object.
    def move_arrow_down(self):
        self.y_position += self.speed
        # Move the arrow down by its speed
        self.move("arrows", 0, self.y_position)

    # Set the speed of the arrow. This is important for future song syncing.
    def set_speed(self, speed: int):
        self.speed = speed
    
    # Check if the arrow has moved off the bottom of the canvas
    def check_off_screen(self):
        canvas_height = self.winfo_height()
        if self.y_position > canvas_height:
            self.destroy()  # Remove the arrow from the canvas


    def update(self):
        self.move_arrow_down()
        self.check_off_screen()

        



#create the test window to display the Scrolling_Arrows_Frame
if __name__ == "__main__":
    #import from game_frame to test integration
    import get_from_files as gff
    root = tk.Tk()
    root.title("Scrolling Arrows Frame Test")
    root.geometry("400x600")
    root_frame = gf.Game_Frame(root)
    root_frame.pack(fill=tk.BOTH, expand=True)
    

    

    box = Scrolling_Arrow(
            root_frame.left_canvas,
            image_name="arrow_angled_basic.png",
            rotate=0,
            resize=(40, 40)
        )
    box2 = Scrolling_Arrow(
            root_frame.left_canvas,
            image_name="arrow_basic.png",
            rotate=90,
            resize=(40, 40)
        )
    box.pack()
    box2.pack()
    


    root.mainloop()