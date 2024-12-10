import tkinter as tk
from tkinter import ttk
from .pages.home_page import HomePage
from .pages.chat_page import ChatPage

class BetterUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Thai Language App")
        
        # Define colors
        self.colors = {
            'bg': '#36393F',
            'card': '#40444B',
            'text': '#FFFFFF',
            'secondary_text': '#B9BBBE',
            'accent': '#5865F2',
            'hover': '#454950'
        }
        
        # Configure for smooth animations (60 FPS)
        self.frame_time = 1000 // 60  # 60 FPS in milliseconds
        self.animation_duration = 200  # Duration in milliseconds
        
        # Initialize animation variables
        self.current_page = None
        self.transitioning = False
        
        self.setup_styles()
        self.setup_window()
        self.create_layout()

    def setup_styles(self):
        # Configure styles for the application
        style = ttk.Style()
        style.configure('Content.TFrame', background=self.colors['bg'])
        style.configure('Card.TFrame', background=self.colors['card'])
        style.configure('Navbar.TFrame', background=self.colors['card'])
        style.configure('NavButton.TLabel',
                       background=self.colors['card'],
                       foreground=self.colors['text'],
                       font=('Arial', 12))
        style.configure('Header.TLabel',
                       background=self.colors['card'],
                       foreground=self.colors['text'],
                       font=('Arial', 16, 'bold'))
        style.configure('Discord.TLabel',
                       background=self.colors['card'],
                       foreground=self.colors['text'],
                       font=('Arial', 12))

    def setup_window(self):
        self.root.configure(bg=self.colors['bg'])
        self.root.geometry('1000x600')
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)  # Column 1 for content

    def create_layout(self):
        # Create navbar
        self.navbar = ttk.Frame(self.root, style='Navbar.TFrame', width=200)
        self.navbar.grid(row=0, column=0, sticky='ns')
        self.navbar.pack_propagate(False)  # Maintain width
        
        # Create main content area
        self.content_frame = ttk.Frame(self.root, style='Content.TFrame')
        self.content_frame.grid(row=0, column=1, sticky='nsew')
        
        self.create_navbar()
        self.create_content()

    def create_navbar(self):
        nav_items = [
            ("🏠 Home", "home"),
            ("💬 Chat", "chat"),
            ("📚 Dictionary", "dictionary"),
            ("⚙️ Settings", "settings")
        ]
        
        for text, page_name in nav_items:
            self.create_nav_button(text, lambda p=page_name: self.show_page(p))

    def create_nav_button(self, text, command):
        button_frame = ttk.Frame(self.navbar, style='Navbar.TFrame')
        button_frame.pack(fill=tk.X, pady=2)
        
        # Create a regular tk.Label instead of ttk.Label for better color control
        label = tk.Label(
            button_frame,
            text=text,
            background=self.colors['card'],  # Set initial background
            foreground=self.colors['text'],
            font=('Arial', 12),
            padx=20,
            pady=10
        )
        label.pack(fill=tk.X)
        
        # Bind hover animations
        label.bind('<Enter>', lambda e: self.animate_hover(label, True))
        label.bind('<Leave>', lambda e: self.animate_hover(label, False))
        label.bind('<Button-1>', lambda e: command())

    def animate_hover(self, widget, entering):
        target_bg = self.colors['hover'] if entering else self.colors['card']
        current_bg = widget.cget('background')
        
        def interpolate(start, end, progress):
            r1, g1, b1 = int(start[1:3], 16), int(start[3:5], 16), int(start[5:7], 16)
            r2, g2, b2 = int(end[1:3], 16), int(end[3:5], 16), int(end[5:7], 16)
            r = int(r1 + (r2 - r1) * progress)
            g = int(g1 + (g2 - g1) * progress)
            b = int(b1 + (b2 - b1) * progress)
            return f'#{r:02x}{g:02x}{b:02x}'
        
        def animate_step(start_time):
            elapsed = self.root.tk.call('clock', 'milliseconds') - start_time
            progress = min(1.0, elapsed / self.animation_duration)
            
            current_color = interpolate(current_bg, target_bg, progress)
            widget.configure(background=current_color)
            
            if progress < 1.0:
                self.root.after(self.frame_time, lambda: animate_step(start_time))
        
        start_time = self.root.tk.call('clock', 'milliseconds')
        animate_step(start_time)

    def create_content(self):
        self.pages = {}
        # Create pages with a simple dictionary
        self.page_classes = {
            'home': HomePage,
            'chat': ChatPage,
        }
        
        # Initialize all pages
        for page_name, page_class in self.page_classes.items():
            self.pages[page_name] = page_class(self.content_frame, self.colors)
        
        self.show_page('home')  # Changed from self.show_home() to self.show_page('home')

    def animate_page_transition(self, new_page):
        if self.transitioning:
            return
        
        self.transitioning = True
        old_page = self.current_page
        
        # Configure new page
        new_page.frame.place(relx=1.0, rely=0, relwidth=1, relheight=1)
        
        def animate_step(start_time):
            elapsed = self.root.tk.call('clock', 'milliseconds') - start_time
            progress = min(1.0, elapsed / self.animation_duration)
            
            if old_page:
                old_page.frame.place(relx=-progress, rely=0)
            new_page.frame.place(relx=1-progress, rely=0)
            
            if progress < 1.0:
                self.root.after(self.frame_time, lambda: animate_step(start_time))
            else:
                if old_page:
                    old_page.frame.place_forget()
                self.transitioning = False
        
        start_time = self.root.tk.call('clock', 'milliseconds')
        animate_step(start_time)

    def show_page(self, page_name):
        if page_name in self.pages:
            self.animate_page_transition(self.pages[page_name])
            self.current_page = self.pages[page_name]

    def run(self):
        self.root.mainloop() 