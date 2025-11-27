from typing import Any, Dict
from PIL import Image, ImageTk
import get_from_files as gff

def get_image(image_name: str) -> Image.Image:
    image_path = gff.get_images_path()
    try:
        with Image.open(image_path + image_name) as img:
            return img.copy()  # Return a copy of the image to avoid issues with closed files  
    except FileNotFoundError:
        print(f"Error: The image at {image_path} was not found.")
        return None


def process_image(image_name: str, **kwargs) -> Image.Image:
    img = get_image(image_name)

    #this will rotate the image by the rotate argument in **kwargs dictionary.
    #If no rotate argument is given, it defaults to 0 (no rotation).
    img = img.rotate(kwargs.get('rotate', 0))   
    
    # Same thing for resize                                         
    img = img.resize(kwargs.get('resize', (img.width, img.height)))  

    # Additional image processing can be added here. Just keep the same format. all processing
    # functions should come from kwargs dictionary with a default value that changes nothing or 
    # uses a standard default from the syles or config files.
    return img

    # This is the function that will be called by other modules to get a processed image.
    # It will call the process image function which in turn calls get_image to retrieve the image
    # from the file system. Process image will then apply any processing specified in **kwargs.
    # Finally, it will return the processed image.
def get_tkinter_PhotoImage(image_name: str, **kwargs) -> ImageTk.PhotoImage:
    img = process_image(image_name, **kwargs)
    return ImageTk.PhotoImage(img)