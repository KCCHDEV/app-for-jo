class ThemeColors:
    DISCORD = {
        'bg_dark': '#36393F',
        'bg_darker': '#2F3136',
        'text': '#DCDDDE',
        'accent': '#7289DA',
        'hover': '#40444B',
        'success': '#43B581',
        'danger': '#F04747',
        'warning': '#FAA61A',
        'textbox': '#40444B',
        'border': '#202225'
    }

class ThemeStyles:
    def __init__(self, style, colors):
        self.style = style
        self.colors = colors
        self.setup_styles()

    def setup_styles(self):
        self.style.theme_use('clam')
        
        # Basic styles
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
        
        # More styles...
        # (Add all your style configurations here) 