"""
Mail sender Sorbonne Université
Login interface
Quentin Deschamps, 2020
"""
import smtplib
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror


class LoginInterface():
    """Interface de connexion au serveur"""
    def __init__(self, window):
        self.login = False
        self.num_etudiant, self.password = "", ""

        self.login_window = window
        self.login_window.title("Authentification")
        self.login_window.resizable(width=False, height=False)

        # Style
        self.style = ttk.Style()
        if "clam" in self.style.theme_names():
            self.style.theme_use('clam')

        self.frame_login = ttk.Frame(self.login_window)
        self.label_num_etudiant = ttk.Label(self.frame_login,
                                            text="Numéro étudiant")
        self.label_password = ttk.Label(self.frame_login, text="Mot de passe")
        self.label_num_etudiant.grid(row=0, column=0, padx=5, pady=5)
        self.label_password.grid(row=1, column=0, pady=5)

        self.entry_num_etudiant = ttk.Entry(self.frame_login)
        self.entry_password = ttk.Entry(self.frame_login, show='*')
        self.entry_num_etudiant.grid(row=0, column=1, padx=5, pady=5)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        self.frame_login.grid(column=0, row=0, padx=5, pady=5)

        self.logo = tk.PhotoImage(file="su.png")
        self.label_logo = tk.Label(self.login_window, image=self.logo)
        self.label_logo.grid(column=1, row=0, padx=5, pady=5)

        self.button_login = ttk.Button(self.login_window,
                                       text="Connexion", command=self.connect)
        self.button_login.grid(column=0, row=1, padx=5, pady=5)

        self.label_author = ttk.Label(self.login_window,
                                      text="Quentin Deschamps, 2020")
        self.label_author.grid(column=1, row=1, padx=5, pady=5)

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
            showerror("Erreur", "La connexion a échoué. Veuillez réessayer.")
        else:
            self.login = True
            self.num_etudiant = num_etudiant
            self.password = password
            self.login_window.destroy()
