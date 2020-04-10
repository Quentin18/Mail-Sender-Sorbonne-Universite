"""
Mail sender Sorbonne Université
Login interface
Quentin Deschamps, 2020
"""
import smtplib
import tkinter as tk
import tkinter.ttk as ttk
from mailSenderSU.src.style import Style
from mailSenderSU.src.message import show_login_error


class LoginInterface:
    """Interface de connexion au serveur"""
    def __init__(self, window, style, path):
        self.login = False
        self.num_etudiant, self.password = "", ""

        # Fenêtre
        self.login_window = window
        self.login_window.title("Authentification")
        self.login_window.resizable(width=False, height=False)
        self.login_window.focus_set()
        self.login_window.bind("<Return>", self.return_connect)

        # Style
        self.style = Style(self.login_window, style, path)

        # Gauche
        self.frame_left = ttk.Frame(self.login_window)
        self.frame_login = ttk.Frame(self.frame_left)
        self.label_num_etudiant = ttk.Label(self.frame_login,
                                            text="Numéro étudiant")
        self.label_password = ttk.Label(self.frame_login, text="Mot de passe")
        self.label_num_etudiant.grid(row=0, column=0, padx=5, pady=5)
        self.label_password.grid(row=1, column=0, pady=5)

        self.entry_num_etudiant = ttk.Entry(self.frame_login)
        self.entry_password = ttk.Entry(self.frame_login, show='*')
        self.entry_num_etudiant.grid(row=0, column=1, padx=5, pady=5)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        self.frame_login.grid(row=0, column=0, padx=5, pady=5)

        self.button_login = ttk.Button(self.frame_left, text="Connexion",
                                       command=self.connect)
        self.button_login.grid(row=1, column=0, padx=5, pady=5)
        self.frame_left.grid(row=0, column=0, padx=10, pady=10)

        # Droite
        self.logo = tk.PhotoImage(file=self.style.image)
        self.label_logo = tk.Label(self.login_window, image=self.logo)
        self.label_logo.grid(row=0, column=1, padx=10, pady=10)

    def return_connect(self, event):
        """Connexion au serveur avec la touche Enter"""
        self.connect()

    def connect(self, server="smtp.upmc.fr", port=587):
        """Vérifie la validité du numéro étudiant et du mot de passe"""
        num_etudiant = self.entry_num_etudiant.get()
        password = self.entry_password.get()
        try:
            server = smtplib.SMTP(server, port)
            server.starttls()
            server.login(num_etudiant, password)
            server.quit()
        except Exception:
            show_login_error()
        else:
            self.login = True
            self.num_etudiant = num_etudiant
            self.password = password
            self.login_window.destroy()
