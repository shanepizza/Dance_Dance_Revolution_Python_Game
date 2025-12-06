import tkinter as tk
import pathlib as pl

#This file will hold functions for retrieving config data from files

#sets paths for easier access
#get the top level path of the project
def get_top_level_file_path():
    return pl.Path().cwd() 
top_level_path = get_top_level_file_path()
styles = {  "Normal" : "styles.txt",
            "Orange" : "orange_style.txt",}

styles_path = styles["Normal"]
def set_styles_path(path: str):
    #fetch the    
    global styles_path
    styles_path = styles.get(path, styles[path])



#get src path
def get_src_path():
    return top_level_path / "src/"
#get images path
def get_images_path():
    return top_level_path / "assets/images/"
#get songs path
def get_songs_path():
    return top_level_path / "assests/songs/"


#opens a file and returns the file object
def open_file(filename):
    try:
        with open(filename) as thisfile:
            return thisfile
    except Exception as e:
        print(f"Oh fiddlessticks! an Error Occured: {e}")
        return e
        


#currently meant for getting title from txt file
def get_line_by_keyword(filename, keyword, second_level_path="src/"):
    """
    Reads a file line by line and returns the first line containing the keyword.
    """
    try:
        with open(top_level_path / second_level_path /filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith(keyword):
                    #Cannot have empty or whitespace keyword
                    if keyword == "" or keyword.isspace():
                        raise ValueError("Keyword cannot be empty or whitespace.")
                        
                    # Return the line content, stripped of the keyword and whitespace/newlines
                    return line[len(keyword):].strip()
        
        # If the loop finishes without finding the keyword
        print(f"Warning: The keyword '{keyword}' was not found in {filename}.")
        raise Warning("Keyword not found.")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return "Frank Not Found"
    except ValueError as e:
        print(f"An error occurred: {e}")
        return e.__class__
    except Warning as w:
        print(f"A warning occurred: {w}")
        return None

#Made this because I am tired of guessing why my colors are not showing up in frames.  
def check_if_is_color_str(s: str) -> bool:
    #A simple function to check if a string is a valid color name in tkinter
    try:
        tmp = tk.Tk()
        tmp.winfo_rgb(s)  # This will raise an exception if s is not a valid color
        tmp.destroy()
        return True
    except tk.TclError:
        return False
    
def get_title():
    return get_line_by_keyword("config.txt", "Title:")

def get_button_style():
    return get_line_by_keyword(styles_path, "ButtonStyle:")

def get_normal_button_width():
    return get_line_by_keyword(styles_path, "NormalButtonWidth:")

def get_normal_button_height():
    return get_line_by_keyword(styles_path, "NormalButtonHeight:")     

def get_normal_button_padding():
    return get_line_by_keyword(styles_path, "NormalButtonPadding:")

def get_refresh_rate():
    return int(get_line_by_keyword("config.txt", "RefreshRate:"))

def get_unit_time_per_second():
    return int(get_line_by_keyword("config.txt", "UnitTimePerSecond:"))

#def get_images_path():
    #return get_line_by_keyword("config.txt", "ImagesPath:")

def get_window_width():
    width_height_line = get_line_by_keyword("config.txt", "WindowSize:")
    return int(width_height_line.split('x')[0])

def get_window_height():
    #has to return the line after x because height is after width
    width_height_line = get_line_by_keyword("config.txt", "WindowSize:")
    return int(width_height_line.split('x')[1])

def get_scrolling_arrows_canvas_background_color():
    color = get_line_by_keyword(styles_path, "ScrollingArrowsCanvasBackgroundColor:")
    if not check_if_is_color_str(color):
        print("Error: Invalid color for ScrollingArrowsCanvasBackgroundColor.")
        return "white"  # Default color
    return color

def get_right_canvas_background_color():
    color = get_line_by_keyword(styles_path, "RightCanvasBackgroundColor:")
    if not check_if_is_color_str(color):
        print("Error: Invalid color for RightCanvasBackgroundColor.")
        return "white"  # Default color
    return color

def get_right_background_screen_color():
    color = get_line_by_keyword(styles_path, "RightScreenBackgroundColor:")
    if not check_if_is_color_str(color):
        print("Error: Invalid color for RightScreenBackgroundColor.")
        return "white"  # Default color
    return color

def get_left_background_screen_color():
    color = get_line_by_keyword(styles_path, "LeftScreenBackgroundColor:")
    if not check_if_is_color_str(color):
        print("Error: Invalid color for LeftScreenBackgroundColor.")
        return "white"  # Default color
    return color

#ArrowSprite info
def get_arrow_speed():
    return int(get_line_by_keyword("config.txt", "ArrowSpeed:"))
def get_arrow_pixel_size():
    return int(get_line_by_keyword("config.txt", "ArrowPixelSize:"))

#Button info
def get_button_pixel_size():
    return int(get_line_by_keyword("config.txt", "ButtonPixelSize:"))


if __name__ == "__main__":
    print("Current file path:", top_level_path/"src")