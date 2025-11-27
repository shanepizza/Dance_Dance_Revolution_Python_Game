import tkinter as tk
from tkinter import ttk
from typing import Callable, Dict, Iterable, Optional, Sequence

"""
dance_dance_revolution/menu_frame.py

Tkinter Frame providing a simple menu of buttons intended to be used from main.py.

Usage example (in main.py):
    root = tk.Tk()
    menu = MenuFrame(root,
                     menu_items=["Start", "Options", "High Scores", "Quit"],
                     callbacks={"Start": start_cb, "Quit": root.quit})
    menu.pack(expand=True, fill="both")
"""



class MenuFrame(tk.Frame):
    """
    A configurable menu frame containing a title and a vertical column of buttons.

    Parameters
    - master: parent widget
    - menu_items: sequence of button names (strings)
    - callbacks: optional dict mapping button name -> callable
    - title: title text displayed above the buttons
    - button_style: optional ttk style name for buttons
    """

    def __init__(
        self,
        master,
        menu_items: Optional[Sequence[str]] = None,
        callbacks: Optional[Dict[str, Callable]] = None,
        title: str = "Dance Dance Revolution",
        button_style: Optional[str] = None,
        *args,
        **kwargs,
    ):
        super().__init__(master, *args, **kwargs)
        self.callbacks = callbacks.copy() if callbacks else {}
        self.buttons: Dict[str, ttk.Button] = {}
        self.title_text = title
        self.button_style = button_style

        if menu_items is None:
            menu_items = ["Start", "Options", "High Scores", "Quit"]

        # Title label
        title_label = tk.Label(self, text=self.title_text, font=("Helvetica", 20, "bold"))
        title_label.pack(pady=(20, 10))

        # Container for buttons
        btn_container = ttk.Frame(self)
        btn_container.pack(padx=30, pady=10, expand=True)

        for name in menu_items:
            cmd = self.callbacks.get(name, None)
            if cmd is None and name.lower() == "quit":
                cmd = master.quit if hasattr(master, "quit") else lambda: None
            btn = ttk.Button(btn_container, text=name, command=cmd, style=self.button_style)
            btn.pack(fill="x", pady=6, ipady=6)
            self.buttons[name] = btn

    def set_command(self, name: str, callback: Callable):
        """
        Assign or replace the command for a named button. Raises KeyError if button doesn't exist.
        """
        if name not in self.buttons:
            raise KeyError(f"No button named '{name}'")
        self.buttons[name].config(command=callback)
        self.callbacks[name] = callback

    def enable(self, name: str):
        """Enable a named button."""
        self.buttons[name].state(["!disabled"])

    def disable(self, name: str):
        """Disable a named button."""
        self.buttons[name].state(["disabled"])

    def enable_all(self):
        for btn in self.buttons.values():
            btn.state(["!disabled"])

    def disable_all(self):
        for btn in self.buttons.values():
            btn.state(["disabled"])


# Demo when run directly (optional)
if __name__ == "__main__":
    def demo_start():
        print("Start pressed")

    root = tk.Tk()
    root.title("DDR Menu Demo")
    mf = MenuFrame(root, callbacks={"Start": demo_start})
    mf.pack(expand=True, fill="both")
    root.mainloop()