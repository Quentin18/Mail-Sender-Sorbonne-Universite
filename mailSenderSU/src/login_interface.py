"""
The ``login_interface`` module creates the login interface of the GUI.

.. module:: login_interface
    :synopsis: Create login interface.

.. moduleauthor:: Quentin Deschamps <quentindeschamps18@gmail.com>

"""
import tkinter as tk
import tkinter.ttk as ttk
import logging
from mailSenderSU.src.style import Style
from mailSenderSU.src.email_utils import EmailConnection
from mailSenderSU.src.message import show_login_error


class LoginInterface:
    """Manage login interface."""
    def __init__(self, window, style):
        """Create login interface."""
        self._login = False
        self._username, self._password = '', ''

        # Window
        self.login_window = window
        self.login_window.title('Authentification')
        self.login_window.resizable(width=False, height=False)
        self.login_window.focus_set()
        self.login_window.bind('<Return>', self.return_connect)

        # Style
        self.style = Style(self.login_window, style)

        # Left
        self.frame_left = ttk.Frame(self.login_window)
        self.frame_login = ttk.Frame(self.frame_left)
        self.label_username = ttk.Label(self.frame_login, text='Identifiant')
        self.label_password = ttk.Label(self.frame_login, text='Mot de passe')
        self.label_username.grid(row=0, column=0, padx=5, pady=5)
        self.label_password.grid(row=1, column=0, pady=5)

        self.entry_username = ttk.Entry(self.frame_login)
        self.entry_password = ttk.Entry(self.frame_login, show='*')
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        self.frame_login.grid(row=0, column=0, padx=5, pady=5)

        self.button_login = ttk.Button(self.frame_left, text='Connexion',
                                       command=self.connect)
        self.button_login.grid(row=1, column=0, padx=5, pady=5)
        self.frame_left.grid(row=0, column=0, padx=10, pady=10)

        # Right
        try:
            self.logo = tk.PhotoImage(file=self.style.image)
            self.label_logo = tk.Label(self.login_window, image=self.logo)
            self.label_logo.grid(row=0, column=1, padx=10, pady=10)
        except Exception:
            pass

        logging.info('Login window created')

    @property
    def login(self):
        """Get login."""
        return self._login

    @property
    def username(self):
        """Get username."""
        return self._username

    @property
    def password(self):
        """Get password."""
        return self._password

    @login.setter
    def login(self, val):
        """Set login."""
        self._login = val

    @username.setter
    def username(self, val):
        """Set username."""
        self._username = val

    @password.setter
    def password(self, val):
        """Set password."""
        self._password = val

    def return_connect(self, event):
        """Connect to the server with the <ENTER> command."""
        self.connect()

    def connect(self):
        """Try to connect to the server."""
        username = self.entry_username.get()
        password = self.entry_password.get()
        if not EmailConnection.is_valid(username, password):
            show_login_error()
        else:
            self.login = True
            self.username = username
            self.password = password
            self.login_window.destroy()
            logging.info('Login window closed')
