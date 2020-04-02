"""
Mail sender Sorbonne Université
Style
Quentin Deschamps, 2020
"""
from tkinter import ttk


def set_style(window, bgcolor='#263068', bg_button='#ffffff',
              fg_button='#e63228', fg_label='#ffffff',
              theme='clam', font_button=('calibri', 10, 'bold', 'underline')):
    """Définit le style d'une fenêtre"""
    window.configure(bg=bgcolor)
    s = ttk.Style()
    if theme in s.theme_names():
        s.theme_use(theme)
    # Button style
    s.configure('TButton',
                foreground=fg_button,
                background=bg_button,
                font=font_button)
    # Label style
    s.configure('TLabel', foreground=fg_label, background=bgcolor)
    # Frame style
    s.configure('TFrame', background=bgcolor)
