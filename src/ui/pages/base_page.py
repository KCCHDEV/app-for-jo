import tkinter as tk
from tkinter import ttk

class BasePage:
    def __init__(self, parent, colors):
        self.frame = ttk.Frame(parent, style='Content.TFrame')
        self.colors = colors
        self.setup_ui()
    
    def setup_ui(self):
        """Override this method in child classes to create the page UI"""
        pass
    
    def create_button(self, parent, text, command):
        """Helper method to create styled buttons"""
        btn = tk.Button(
            parent,
            text=text,
            bg=self.colors['accent'],
            fg=self.colors['text'],
            relief='flat',
            command=command
        )
        btn.bind('<Enter>', lambda e: btn.configure(bg=self.colors['hover']))
        btn.bind('<Leave>', lambda e: btn.configure(bg=self.colors['accent']))
        return btn 