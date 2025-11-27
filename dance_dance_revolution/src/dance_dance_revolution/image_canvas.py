import image_processing as ips
import tkinter as tk
import get_from_files as gff

#images_path = gff.get_images_path()


class Image_Canvas(tk.Canvas):
    def __init__(
            self,         
            master: tk.Frame, #This is the parent frame
            image_name: str,   #This is the name of the image file
            *args,
            **PI_kwargs, #Currently only used for image processing options. maybe change the name.
    ):
        super().__init__(master, *args)
        
        # Remove border and highlight
        #Change this to be adjustable through kwargs or args.
        self.config(borderwidth=0, highlightthickness=0) 
        
        # create the PhotoImage using image_processing module
        #kwargs will rotate and resize the image if specified
        self.image_name = image_name
        self.photo_image = ips.get_tkinter_PhotoImage(self.image_name, **PI_kwargs)
        self.config(
            width=self.photo_image.width(),
            height=self.photo_image.height()
        )    
        
        # Create an image on the canvas
        self.create_image(0, 0, image=self.photo_image, anchor=tk.NW)






#Create a test window to display the Image_Canvas
#I don't fully understand how the if __name__ == "__main__": part works yet, but
#this is what allows me to run this file directly to test it.
if __name__ == "__main__":   
    root = tk.Tk()
    root.title("Image Canvas Test")

    #Create an instance of Image_Canvas
    img_canvas = Image_Canvas(
        root,
        image_name="arrow_angled_basic.png",
        rotate=180,  # Rotate the image by 180 degrees
        resize=(40, 40)  # Resize the image to 40x40 pixels
    )
    img_canvas.pack()

    root.mainloop()
