"""
Mail sender Sorbonne Université
Style
Quentin Deschamps, 2020
"""
from tkinter import ttk


class Style:
    """Définit le style d'une fenêtre"""
    def __init__(self, window, style, path):
        if style == 'polytech':
            self.image = "".join([path, "/image/polytech.png"])
            bgcolor = '#009ee0'
            fg_button = '#004877'
        else:
            self.image = "".join([path, "/image/su.png"])
            bgcolor = '#263068'
            fg_button = '#e63228'
        theme = 'clam'
        bg_button = '#ffffff'
        fg_label = '#ffffff'
        font_button = ('calibri', 10, 'bold')

        self.window = window
        self.window.configure(bg=bgcolor)
        self.style = ttk.Style()
        if theme in self.style.theme_names():
            self.style.theme_use(theme)
        # Button style
        self.style.configure('TButton',
                             foreground=fg_button,
                             background=bg_button,
                             font=font_button)
        # Label style
        self.style.configure('TLabel', foreground=fg_label, background=bgcolor)
        # Frame style
        self.style.configure('TFrame', background=bgcolor)
