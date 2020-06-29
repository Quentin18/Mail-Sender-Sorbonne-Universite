"""
The ``mail_interface`` module creates the mail sender interface of the GUI.

.. module:: mail_interface
    :synopsis: Create mail sender interface.

.. moduleauthor:: Quentin Deschamps <quentindeschamps18@gmail.com>

"""
import os
from pathlib import Path
import tkinter as tk
import tkinter.ttk as ttk
import logging
from mailSenderSU.src.email_utils import Email, EmailConnection
from mailSenderSU.src.attachments import Attachments
from mailSenderSU.src.style import Style
import mailSenderSU.src.message as Message
from mailSenderSU.src.files import File


class MailSenderInterface:
    """Manage mail sender interface."""
    def __init__(self, window, style, username, password):
        """Create mail sender interface."""
        self._username = username
        self._password = password

        # Files
        directory = Path(os.path.dirname(os.path.abspath(__file__))).parent
        self.user_file = File(directory.joinpath('data', 'user.txt'))
        self.contacts_file = File(directory.joinpath('data', 'contacts.txt'))

        self.user_list = self.user_file.get_list()
        self.contacts_list = self.contacts_file.get_list()

        # Window
        self.window = window
        self.window.title('Mail Sender Sorbonne-Université')
        self.window.resizable(width=False, height=False)

        # Style
        self.style = Style(self.window, style)

        # Top
        self.frame = ttk.Frame(self.window)
        self.label_from_ = ttk.Label(self.frame, text='De')
        self.entry_from_ = ttk.Combobox(self.frame, width=50,
                                        values=self.user_list)
        if self.user_list != []:
            self.entry_from_.current(0)
        self.label_from_.grid(row=0, column=0, padx=10, pady=5)
        self.entry_from_.grid(row=0, column=1, padx=10, pady=5)
        self.label_to = ttk.Label(self.frame, text='À')
        self.entry_to = ttk.Combobox(self.frame, width=50,
                                     values=self.contacts_list)
        self.label_to.grid(row=1, column=0, padx=10, pady=5)
        self.entry_to.grid(row=1, column=1, padx=10, pady=5)
        self.label_cc = ttk.Label(self.frame, text='Cc')
        self.entry_cc = ttk.Combobox(self.frame, width=50,
                                     values=self.contacts_list)
        self.label_cc.grid(row=2, column=0, padx=10, pady=5)
        self.entry_cc.grid(row=2, column=1, padx=10, pady=5)
        self.label_subject = ttk.Label(self.frame, text='Objet')
        self.entry_subject = ttk.Entry(self.frame, width=52)
        self.label_subject.grid(row=3, column=0, padx=10, pady=5)
        self.entry_subject.grid(row=3, column=1, padx=10, pady=5)
        self.frame.grid(row=0, padx=10, pady=10)

        # Body
        self.entry_message = tk.Text(self.window, height=10, width=60,
                                     wrap=tk.WORD)
        self.entry_message.grid(row=1, padx=10, pady=10)

        # Buttons
        self.button_frame = ttk.Frame(self.window)
        self.button_send = ttk.Button(self.button_frame, text='Envoyer',
                                      command=self.send)
        self.button_send.grid(row=0, column=0, padx=5, pady=5)

        # Attachments
        self.attachments = Attachments(self.window, self.button_frame)

        self.button_frame.grid(row=3, padx=10, pady=5)

        logging.info('Mail window created')

    @property
    def username(self):
        """Get username."""
        return self._username

    @property
    def password(self):
        """Get password."""
        return self._password

    def check(self):
        """Check fields."""
        from_ = self.entry_from_.get()
        if not from_:
            Message.show_from_miss()
            return False
        to = self.entry_to.get()
        if not to:
            Message.show_to_miss()
            return False
        if not ('sorbonne-universite.fr' in from_
                or 'upmc.fr' in from_):
            Message.show_address_not_valid(from_)
            return False
        subject = self.entry_subject.get()
        if not subject:
            Message.show_subject_miss()
            return False
        return True

    def send(self):
        """Send an email."""
        if self.check():
            from_ = self.entry_from_.get()
            to = self.entry_to.get()
            cc = self.entry_cc.get()
            subject = self.entry_subject.get()
            message = self.entry_message.get('1.0', 'end')
            attachments = self.attachments.attachments
            if not cc:
                cc = ''
            directory = Path(os.path.dirname(os.path.abspath(__file__))).parent
            signature_file = File(directory.joinpath('data', 'signature.html'))
            server = EmailConnection(self.username, self.password)
            email = Email(from_, to, cc, subject, message, attachments,
                          signature_file.read())
            if server.send(email) == {}:
                Message.show_send()
                if from_ not in self.user_list:
                    if Message.show_new_user(from_):
                        self.user_file.add(from_)
                if to not in self.contacts_list:
                    if Message.show_new_contact(to):
                        self.contacts_file.add(to)
                if cc != '' and cc not in self.contacts_list:
                    if Message.show_new_contact(cc):
                        self.contacts_file.add(cc)
            else:
                Message.show_send_error()

            server.close()
