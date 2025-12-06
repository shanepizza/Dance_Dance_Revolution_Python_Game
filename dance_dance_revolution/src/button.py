import tkinter as tk
from tkinter import ttk
import get_from_files as gff

class Crafty_Button(ttk.Button):
    """Custom button class extending ttk.Button with additional styling."""

    def __init__(self, parent:tk.Frame, btn_text: str="Button", btn_command=None, **kwargs):
        """
        Initialize custom button.
        
        Args:
            parent: Parent widget
            text: Button text
            command: Command to execute on click
            **kwargs: Additional ttk.Button parameters
        """
        super().__init__(parent, text=btn_text, command=btn_command, **kwargs)
        self.configure(width=15, padding=10)
        self.configure(style=gff.get_button_style())
    """
    def set_hover_effect(self, normal_style="", hover_style=""):
        #Add hover effect to button.
        self.bind("<Enter>", lambda e: self.configure(style=hover_style))
        self.bind("<Leave>", lambda e: self.configure(style=normal_style))
    """