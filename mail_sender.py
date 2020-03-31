"""
Mail sender Sorbonne Université
Quentin Deschamps, 2020
"""
import tkinter as tk
from src.login_interface import LoginInterface
from src.mail_interface import MailSenderInterface
from src.mail_sender_tools import import_config


def main():
    window = tk.Tk()
    login_interface = LoginInterface(window)
    window.mainloop()
    if login_interface.login:
        list_email_user, list_email_send, list_subject = import_config()
        window = tk.Tk()
        MailSenderInterface(window, list_email_user, list_email_send,
                            list_email_send, list_subject,
                            login_interface.num_etudiant,
                            login_interface.password)
        window.mainloop()


if __name__ == "__main__":
    main()
