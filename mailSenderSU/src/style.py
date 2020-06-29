"""
The ``style`` module manages the style of the GUI.

.. module:: style
    :synopsis: Manage style.

.. moduleauthor:: Quentin Deschamps <quentindeschamps18@gmail.com>

"""
import os
from pathlib import Path
from tkinter import ttk


class Style:
    """Manage the style of a window."""
    def __init__(self, window, style):
        """Init the style of a window."""
        directory = Path(os.path.dirname(os.path.abspath(__file__))).parent
        if style == 'polytech':
            self.image = directory.joinpath('img', 'polytech.gif')
            bgcolor = '#009ee0'
            fg_button = '#004877'
        else:
            self.image = directory.joinpath('img', 'su.gif')
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
