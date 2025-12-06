import tkinter as tk
import get_from_files as gff
import menu as menu
import game_window as gw
import tkinter.messagebox as messagebox





# Create the main application window
root_window = tk.Tk()

# Set the window title and size using values from the config file
root_window.title(gff.get_title()  or "Title Not Found") # Not sure if I need the or statement here
root_window.geometry(gff.get_line_by_keyword("config.txt", "WindowSize:") or "80x50") # Not sure if I need the or statement here

def exit_program():
    root_window.quit()
    root_window.destroy()

def sart_game():
    game = gw.GameWindow()
    game.run()

def change_style():
    
    
    if gff.styles_path == "styles.txt":
        gff.set_styles_path("Orange")
    elif gff.styles_path == "orange_style.txt":
        gff.set_styles_path("Normal")

   
def in_production():
    print("This feature is still in production.")
    #display a text box that says this feature is still in production to the current window
    """Show info using messagebox"""
    messagebox.showinfo(
        title="In Production",
        message="This feature is still in production. Please check back later."
    )   
    


# Create the menu
main_menu = menu.Menu(
    master=root_window,
    #menu_title=gff.get_title(), 
    # This is the title for the menu and 
    # not the window and is curently not actually needed
    menu_items=["Start", "Options", "High Scores", "Quit"],
    callbacks={"Quit": exit_program, "Start": sart_game, "Options": change_style, "High Scores": in_production} # Currently only the Quit button does something
)
main_menu.pack(expand=True)

#run the application
root_window.mainloop()