import tkinter as tk
from tkinter import ttk
import requests
import os
from io import BytesIO
from PIL import Image, ImageFont, ImageTk
from fontTools.ttLib import TTFont

class BetterUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Thai Language Support App")
        
        # Discord-like colors
        self.colors = {
            'bg_dark': '#36393F',
            'bg_darker': '#2F3136',
            'text': '#DCDDDE',
            'accent': '#7289DA',
            'hover': '#40444B'
        }
        
        # Configure window and theme
        self.root.geometry("1000x600")
        self.root.configure(bg=self.colors['bg_dark'])
        
        # Configure ttk styles
        self.setup_styles()
        
        # Download and setup Thai font
        self.setup_thai_font()
        
        # Create main layout
        self.setup_layout()
        
        # Initialize pages
        self.current_page = None
        self.pages = {}
        self.setup_pages()
        self.show_page('home')

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure ttk styles with Discord colors
        self.style.configure('Nav.TButton',
            background=self.colors['bg_darker'],
            foreground=self.colors['text'],
            padding=10,
            font=('Noto Sans Thai', 11)
        )
        
        self.style.configure('Content.TFrame',
            background=self.colors['bg_dark']
        )
        
        self.style.configure('Nav.TFrame',
            background=self.colors['bg_darker']
        )
        
        self.style.configure('Discord.TEntry',
            fieldbackground=self.colors['hover'],
            foreground=self.colors['text']
        )
        
        self.style.configure('Discord.TLabel',
            background=self.colors['bg_dark'],
            foreground=self.colors['text']
        )

    def setup_layout(self):
        # Create navigation sidebar
        self.nav_frame = ttk.Frame(self.root, style='Nav.TFrame', padding="10")
        self.nav_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        # Create content area
        self.content_frame = ttk.Frame(self.root, style='Content.TFrame', padding="20")
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add navigation buttons
        self.create_nav_buttons()

    def create_nav_buttons(self):
        nav_buttons = [
            ("🏠 หน้าแรก", "home"),
            ("💬 แชท", "chat"),
            ("⚙️ ตั้งค่า", "settings")
        ]
        
        for text, page in nav_buttons:
            btn = ttk.Button(
                self.nav_frame,
                text=text,
                style='Nav.TButton',
                command=lambda p=page: self.show_page(p)
            )
            btn.pack(fill=tk.X, pady=2)

    def setup_pages(self):
        # Home page
        self.pages['home'] = self.create_home_page()
        # Chat page
        self.pages['chat'] = self.create_chat_page()
        # Settings page
        self.pages['settings'] = self.create_settings_page()

    def create_home_page(self):
        frame = ttk.Frame(self.content_frame, style='Content.TFrame')
        
        header = ttk.Label(
            frame,
            text="ยินดีต้อนรับ / Welcome",
            font=("Noto Sans Thai", 24),
            style='Discord.TLabel'
        )
        header.pack(pady=20)
        
        description = ttk.Label(
            frame,
            text="แอพพลิเคชันภาษาไทยของคุณ / Your Thai Language Application",
            font=("Noto Sans Thai", 14),
            style='Discord.TLabel'
        )
        description.pack(pady=10)
        
        return frame

    def create_chat_page(self):
        frame = ttk.Frame(self.content_frame, style='Content.TFrame')
        
        # Text display area
        self.text_display = tk.Text(
            frame,
            font=("Noto Sans Thai", 12),
            bg=self.colors['hover'],
            fg=self.colors['text'],
            height=20,
            wrap=tk.WORD
        )
        self.text_display.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Input area
        input_frame = ttk.Frame(frame, style='Content.TFrame')
        input_frame.pack(fill=tk.X, pady=10)
        
        self.text_input = ttk.Entry(
            input_frame,
            font=("Noto Sans Thai", 12),
            style='Discord.TEntry'
        )
        self.text_input.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        submit_button = ttk.Button(
            input_frame,
            text="ส่ง",
            style='Nav.TButton',
            command=self.submit_action
        )
        submit_button.pack(side=tk.RIGHT, padx=5)
        
        return frame

    def create_settings_page(self):
        frame = ttk.Frame(self.content_frame, style='Content.TFrame')
        
        header = ttk.Label(
            frame,
            text="⚙️ ตั้งค่า / Settings",
            font=("Noto Sans Thai", 24),
            style='Discord.TLabel'
        )
        header.pack(pady=20)
        
        # Add your settings controls here
        
        return frame

    def show_page(self, page_name):
        # Hide current page if exists
        if self.current_page:
            self.pages[self.current_page].pack_forget()
        
        # Show new page
        self.pages[page_name].pack(fill=tk.BOTH, expand=True)
        self.current_page = page_name

    def submit_action(self):
        text = self.text_input.get()
        if text:
            self.text_display.insert(tk.END, f"You: {text}\n")
            self.text_input.delete(0, tk.END)

    def setup_thai_font(self):
        # Google Fonts API URL for Noto Sans Thai
        font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;700&display=swap"
        
        # Create fonts directory if it doesn't exist
        if not os.path.exists("fonts"):
            os.makedirs("fonts")
            
        # Download font if not already present
        font_path = "fonts/NotoSansThai-Regular.ttf"
        if not os.path.exists(font_path):
            try:
                response = requests.get(font_url)
                font_css = response.text
                # Extract the actual font file URL from CSS
                font_file_url = font_css.split("url(")[1].split(")")[0]
                
                # Download the font file
                font_response = requests.get(font_file_url)
                with open(font_path, "wb") as f:
                    f.write(font_response.content)
            except Exception as e:
                print(f"Error downloading font: {e}")
                
        return font_path
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BetterUI()
    app.run()
