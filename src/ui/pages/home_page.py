import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self, parent, colors):
        self.parent = parent
        self.colors = colors
        self.frame = self.create_page()

    def create_page(self):
        frame = ttk.Frame(self.parent, style='Content.TFrame')
        
        # Welcome card
        self.create_welcome_card(frame)
        
        # Feature cards
        features_frame = ttk.Frame(frame, style='Content.TFrame')
        features_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        
        self.create_feature_cards(features_frame)
        
        return frame

    def create_welcome_card(self, parent):
        card = ttk.Frame(parent, style='Card.TFrame', padding="20")
        card.pack(fill=tk.X, pady=20, padx=20)
        
        ttk.Label(
            card,
            text="ยินดีต้อนรับ / Welcome",
            style='Header.TLabel'
        ).pack(pady=(0, 10))
        
        ttk.Label(
            card,
            text="แอพพลิเคชันภาษาไทยของคุณ / Your Thai Language Application",
            style='Discord.TLabel',
            wraplength=500
        ).pack()

    def create_feature_cards(self, parent):
        features = [
            ("💬 Chat", "Practice Thai conversation"),
            ("📚 Dictionary", "Look up Thai words"),
            ("⚙️ Settings", "Customize your experience")
        ]
        
        for title, desc in features:
            self.create_feature_card(parent, title, desc)

    def create_feature_card(self, parent, title, description):
        card = ttk.Frame(parent, style='Card.TFrame', padding="15")
        card.pack(fill=tk.X, pady=5)
        
        ttk.Label(
            card,
            text=title,
            style='Discord.TLabel'
        ).pack(anchor='w')
        
        ttk.Label(
            card,
            text=description,
            style='Discord.TLabel'
        ).pack(anchor='w') 