from .base_page import BasePage
import tkinter as tk
from tkinter import ttk

class ChatPage(BasePage):
    def setup_ui(self):
        # Create main container
        container = ttk.Frame(self.frame, style='Content.TFrame')
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Add header
        header = ttk.Label(
            container,
            text="Chat with AI",
            style='Header.TLabel'
        )
        header.pack(pady=(0, 20))
        
        # Add chat area
        self.chat_area = tk.Text(
            container,
            bg=self.colors['card'],
            fg=self.colors['text'],
            wrap=tk.WORD,
            height=15
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True)
        
        # Add input area
        input_container = ttk.Frame(container, style='Content.TFrame')
        input_container.pack(fill=tk.X, pady=(10, 0))
        
        self.input_field = tk.Entry(
            input_container,
            bg=self.colors['card'],
            fg=self.colors['text'],
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        send_button = self.create_button(
            input_container,
            "Send",
            self.send_message
        )
        send_button.pack(side=tk.RIGHT, padx=(10, 0))
    
    def send_message(self):
        message = self.input_field.get()
        if message:
            self.chat_area.insert(tk.END, f"You: {message}\n")
            self.input_field.delete(0, tk.END)
            # Add AI response handling here 