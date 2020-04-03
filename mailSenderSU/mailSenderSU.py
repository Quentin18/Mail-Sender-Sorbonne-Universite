"""
Mail sender Sorbonne Université
Quentin Deschamps, 2020
"""
import tkinter as tk
from mailSenderSU.src.login_interface import LoginInterface
from mailSenderSU.src.mail_interface import MailSenderInterface
from mailSenderSU.src.files import Files
import click
import os


@click.command()
def main():
    """Mail sender Sorbonne Universite"""
    path = os.path.dirname(os.path.abspath(__file__))
    window = tk.Tk()
    login_interface = LoginInterface(window, path)
    window.mainloop()
    if login_interface.login:
        data = Files(path)
        window = tk.Tk()
        MailSenderInterface(window, data,
                            login_interface.num_etudiant,
                            login_interface.password)
        window.mainloop()