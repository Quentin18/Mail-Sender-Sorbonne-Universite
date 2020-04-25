import os
import unittest
import tkinter as tk
import mailSenderSU
from mailSenderSU.src.login_interface import LoginInterface
from mailSenderSU.src.mail_interface import MailSenderInterface
from mailSenderSU.src.files import Files


class Test(unittest.TestCase):
    """Tests de l'interface"""
    def test_app(self):
        if os.environ.get('DISPLAY', '') == '':
            print('No display found. Using:0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')

        path = os.path.dirname(mailSenderSU.__file__)
        window = tk.Tk()
        LoginInterface(window, "su", path)
        window.destroy()

        data = Files(path, "")
        window = tk.Tk()
        MailSenderInterface(window, "su", data, "", "")
        window.destroy()


if __name__ == "__main__":
    unittest.main()
