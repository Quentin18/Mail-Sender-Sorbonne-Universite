"""
Mail sender Sorbonne Université
Style
Quentin Deschamps, 2020
"""
from tkinter import ttk


def set_style(window, bgcolor, bg_button, fg_label, theme='clam'):
    """Définit le style d'une fenêtre"""
    window.configure(bg=bgcolor)
    s = ttk.Style()
    if theme in s.theme_names():
        s.theme_use(theme)
    # Button style
    s.configure('TButton', background=bg_button)
    # Label style
    s.configure('TLabel', foreground=fg_label, background=bgcolor)
    # Frame style
    s.configure('TFrame', background=bgcolor)
