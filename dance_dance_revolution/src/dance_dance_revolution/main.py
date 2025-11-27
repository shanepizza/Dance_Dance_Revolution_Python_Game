import tkinter as tk
import get_from_files as gff
import menu as menu

#setting the path to this file


# Create the main application window
root_window = tk.Tk()

# Set the window title and size using values from the config file
root_window.title(gff.get_title()  or "Title Not Found") # Not sure if I need the or statement here
root_window.geometry(gff.get_line_by_keyword("config.txt", "WindowSize:") or "80x50") # Not sure if I need the or statement here

# Create the menu
main_menu = menu.Menu(
    master=root_window,
    #menu_title=gff.get_title(), 
    # This is the title for the menu and 
    # not the window and is curently not actually needed
    menu_items=["Start", "Options", "High Scores", "Quit"],
)
main_menu.pack(expand=True)

#run the application
root_window.mainloop()