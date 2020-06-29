import os
from pathlib import Path
import unittest
import tkinter as tk
from mailSenderSU.src.login_interface import LoginInterface
from mailSenderSU.src.mail_interface import MailSenderInterface
from mailSenderSU.src.files import File
from mailSenderSU.src.email_utils import EmailConnection, Email


class Test(unittest.TestCase):
    """Tests de l'interface"""
    def test_app(self):
        window = tk.Tk()
        LoginInterface(window, 'su')
        window.destroy()

        window = tk.Tk()
        MailSenderInterface(window, 'su', '', '')
        window.destroy()

    def test_send(self):
        from_ = os.environ.get('MAIL_SU')
        to = os.environ.get('MAIL_TEST')
        username = os.environ.get('USERNAME')
        password = os.environ.get('PASSWORD')

        directory = Path(os.path.dirname(os.path.abspath(__file__))).parent
        signature_file = File(
            directory.joinpath('mailSenderSU', 'data', 'signature.html'))

        server = EmailConnection(username, password)
        email = Email(
            from_, to, '',
            'Test Travis',
            'Test automatique réalisé par Travis',
            [],
            signature_file.read()
        )
        ret = server.send(email)
        server.close()
        self.assertTrue(ret == {})


if __name__ == "__main__":
    unittest.main()
