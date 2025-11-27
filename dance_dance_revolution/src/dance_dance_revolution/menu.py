import tkinter as tk
from tkinter import ttk
from typing import Callable, Dict, List, Optional
import button as btn


class Menu(tk.Frame):
    def __init__(
        self,
        master: tk.Tk,
        #menu_title: str = gff.get_title(), #This needs to be the parent window title 
        # This is the title for the menu and 
        # not the window and is curently not actually needed
        menu_items: Optional[List[str]] = None,
        callbacks: Optional[Dict[str, Callable]] = None,
        *args,
        **kwargs,
    ):
        super().__init__(master, *args, **kwargs)
        self.callbacks = callbacks if callbacks is not None else {}
        self.buttons: Dict[str, btn.Crafty_Button] = {}
        #self.title_text = menu_title
        # This is the title for the menu and 
        # not the window and is curently not actually needed


        # Title label
        #title_label = tk.Label(self, text=self.title_text, font=("Helvetica", 20, "bold"))
        #title_label.pack(pady=(20, 10))
        # This is the title for the menu and 
        # not the window and is curently not actually needed

        # Container for buttons
        btn_container = ttk.Frame(self)
        btn_container.pack(padx=30, pady=10, expand=True)

        #This creates buttons based on the menu_items list
        #It will use the create_button method to call the Crafty_Button class
        self.buttons = {name: self.create_button(
            who_the_parent=btn_container,
            what_the_name=name,
            command=None #buttons do nothing for now.
        ) for name in menu_items}
        for button in self.buttons.values():
            button.pack()

    #This method creates a Crafty_Button instance
    def create_button(self, who_the_parent, what_the_name:str, command:Callable):
        return btn.Crafty_Button(
            parent=who_the_parent,
            btn_text=what_the_name,
            btn_command=command,
        )
    
#Test window to display the Menu
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Menu Test")
    root.geometry("400x300")

    menu_items = ["Start Game", "Options", "Exit"]
    menu = Menu(root, menu_items=menu_items)
    menu.pack(fill=tk.BOTH, expand=True)

    root.mainloop()