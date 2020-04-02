"""
Mail sender Sorbonne Université
Quentin Deschamps, 2020
"""
import tkinter as tk
from mailSenderSU.src.login_interface import LoginInterface
from mailSenderSU.src.mail_interface import MailSenderInterface
from mailSenderSU.src.files import Files


def main():
    window = tk.Tk()
    login_interface = LoginInterface(window)
    window.mainloop()
    if login_interface.login:
        data = Files()
        window = tk.Tk()
        MailSenderInterface(window, data,
                            login_interface.num_etudiant,
                            login_interface.password)
        window.mainloop()


if __name__ == "__main__":
    main()
