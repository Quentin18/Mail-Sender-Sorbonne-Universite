"""
Mail sender Sorbonne Université
Mail sender interface
Quentin Deschamps, 2020
"""
import tkinter as tk
import tkinter.ttk as ttk
from mailSenderSU.src.send import send_mail
from mailSenderSU.src.attachment import Attachment
from mailSenderSU.src.style import Style
import mailSenderSU.src.message as Message


class MailSenderInterface:
    """Interface du mail sender"""
    def __init__(self, window, data, num_etudiant, password):
        self.data = data
        self.num_etudiant = num_etudiant
        self.password = password

        # Fenêtre
        self.fenetre = window
        self.fenetre.title("Mail Sender Sorbonne Université")
        self.fenetre.resizable(width=False, height=False)

        # Style
        self.style = Style(self.fenetre)

        # Partie du haut
        self.frame = ttk.Frame(self.fenetre)
        self.label_email_user = ttk.Label(self.frame, text="De")
        self.entry_email_user = ttk.Combobox(self.frame, width=50,
                                             values=data.list_email_user)
        self.entry_email_user.current(0)
        self.label_email_user.grid(row=0, column=0, padx=10, pady=5)
        self.entry_email_user.grid(row=0, column=1, padx=10, pady=5)
        self.label_email_send = ttk.Label(self.frame, text="À")
        self.entry_email_send = ttk.Combobox(self.frame, width=50,
                                             values=data.list_email_send)
        self.label_email_send.grid(row=1, column=0, padx=10, pady=5)
        self.entry_email_send.grid(row=1, column=1, padx=10, pady=5)
        self.label_email_cc = ttk.Label(self.frame, text="Cc")
        self.entry_email_cc = ttk.Combobox(self.frame, width=50,
                                           values=data.list_email_send)
        self.label_email_cc.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email_cc.grid(row=2, column=1, padx=10, pady=5)
        self.label_subject = ttk.Label(self.frame, text="Objet")
        self.entry_subject = ttk.Combobox(self.frame, width=50,
                                          values=data.list_subject)
        self.label_subject.grid(row=3, column=0, padx=10, pady=5)
        self.entry_subject.grid(row=3, column=1, padx=10, pady=5)
        self.frame.grid(row=0, padx=10, pady=10)

        # Corps du texte
        self.entry_body = tk.Text(self.fenetre, height=10, width=60)
        self.entry_body.grid(row=1, padx=10, pady=10)

        # Boutons
        self.button_frame = ttk.Frame(self.fenetre)
        self.button_send = ttk.Button(self.button_frame, text="Envoyer",
                                      command=self.send_message)
        self.button_send.grid(row=0, column=0, padx=5, pady=5)

        # Pièces jointes
        self.attachment = Attachment(self.fenetre, self.button_frame)

        self.button_frame.grid(row=3, padx=10, pady=10)

    def send_message(self):
        """Lance l'envoi du mail"""
        email_user = self.entry_email_user.get()
        email_send = self.entry_email_send.get()
        email_cc = self.entry_email_cc.get()
        subject = self.entry_subject.get()
        body = self.entry_body.get("1.0", "end")
        list_attachment = self.attachment.list_attachment
        if email_user and email_send and subject:
            if not email_cc:
                email_cc = ""
            send_mail(email_user, email_send, email_cc,
                      subject, body, list_attachment,
                      self.num_etudiant, self.password, self.data.signature)
            Message.show_send_mail()
            self.data.maj_files(email_user, email_send, email_cc)
        else:
            Message.show_send_mail_error()