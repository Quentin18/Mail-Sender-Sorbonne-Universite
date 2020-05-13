import os
import unittest
import tkinter as tk
import mailSenderSU
from mailSenderSU.src.login_interface import LoginInterface
from mailSenderSU.src.mail_interface import MailSenderInterface
from mailSenderSU.src.files import Files
from mailSenderSU.src.send import send_mail


class Test(unittest.TestCase):
    """Tests de l'interface"""
    def test_app(self):
        path = os.path.dirname(mailSenderSU.__file__)
        window = tk.Tk()
        LoginInterface(window, "su", path)
        window.destroy()

        data = Files(path, "")
        window = tk.Tk()
        MailSenderInterface(window, "su", data, "", "")
        window.destroy()

    def test_send(self):
        path = os.path.dirname(mailSenderSU.__file__)
        data = Files(path, "")
        email_user = os.environ.get("MAIL_SU")
        email_send = os.environ.get("MAIL_TEST")
        num_etudiant = os.environ.get("NUM")
        password = os.environ.get("PWD")
        ret = send_mail(
            email_user,
            email_send,
            "",
            "Test Travis",
            "Test automatique réalisé par Travis !",
            [],
            num_etudiant,
            password,
            data.file_signature
            )
        self.assertTrue(ret[0])


if __name__ == "__main__":
    unittest.main()
