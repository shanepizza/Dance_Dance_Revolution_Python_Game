import tkinter as tk

#This file will hold functions for retrieving config data from files

#set path for easier access

import os
def get_current_file_path():
    return os.path.dirname(os.path.abspath(__file__))
main_path = get_current_file_path()


def open_file(filename):
    try:
        with open(filename) as thisfile:
            return thisfile
    except Exception as e:
        print(f"An Error Occured: {e}")
        return e
        


#currently meant for getting title from txt file
def get_line_by_keyword(filename, keyword):
    """
    Reads a file line by line and returns the first line containing the keyword.
    """
    try:
        with open(main_path + filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith(keyword):
                    # Return the line content, stripped of the keyword and whitespace/newlines
                    return line[len(keyword):].strip()
        
        # If the loop finishes without finding the keyword
        print(f"Warning: The keyword '{keyword}' was not found in {filename}.")
        return None

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
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
    return get_line_by_keyword("styles.txt", "ButtonStyle:")

def get_normal_button_width():
    return get_line_by_keyword("styles.txt", "NormalButtonWidth:")

def get_normal_button_height():
    return get_line_by_keyword("styles.txt", "NormalButtonHeight:")     

def get_normal_button_padding():
    return get_line_by_keyword("styles.txt", "NormalButtonPadding:")

def get_refresh_rate():
    return int(get_line_by_keyword("config.txt", "RefreshRate:"))

def get_unit_time_per_second():
    return int(get_line_by_keyword("config.txt", "UnitTimePerSecond:"))

def get_images_path():
    return get_line_by_keyword("config.txt", "ImagesPath:")

def get_window_width():
    width_height_line = get_line_by_keyword("config.txt", "WindowSize:")
    return int(width_height_line.split('x')[0])

def get_window_height():
    #has to return the line after x because height is after width
    width_height_line = get_line_by_keyword("config.txt", "WindowSize:")
    return int(width_height_line.split('x')[1])

def get_scrolling_arrows_canvas_background_color():
    color = get_line_by_keyword("styles.txt", "ScrollingArrowsCanvasBackgroundColor:")
    if not check_if_is_color_str(color):
        print("Error: Invalid color for ScrollingArrowsCanvasBackgroundColor.")
        return "white"  # Default color
    return color

def get_right_canvas_background_color():
    color = get_line_by_keyword("styles.txt", "RightCanvasBackgroundColor:")
    if not check_if_is_color_str(color):
        print("Error: Invalid color for RightCanvasBackgroundColor.")
        return "white"  # Default color
    return color


if __name__ == "__main__":
    print("Current file path:", get_current_file_path())