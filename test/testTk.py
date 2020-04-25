import os
import unittest
import tkinter as tk
from mailSenderSU.src.login_interface import LoginInterface
from mailSenderSU.src.mail_interface import MailSenderInterface
from mailSenderSU.src.files import Files


class Test(unittest.TestCase):
    """Tests de l'interface"""
    def test_app(self):
        failed = False
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            path = "/".join(path.split("/")[:-1] + ["mailSenderSU"])
            window = tk.Tk()
            LoginInterface(window, "su", path)
            window.destroy()
        except Exception:
            failed = True
        self.assertFalse(failed)

        failed = False
        try:
            data = Files(path, "")
            window = tk.Tk()
            MailSenderInterface(window, "su", data, "", "")
            window.destroy()
        except Exception:
            failed = True
        self.assertFalse(failed)


if __name__ == "__main__":
    unittest.main()
