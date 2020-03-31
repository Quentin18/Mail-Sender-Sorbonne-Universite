"""
Mail sender Sorbonne Université
Mail sender interface
Quentin Deschamps, 2020
"""
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo, showerror
from src.mail_sender_tools import send_mail


class MailSenderInterface:
    """Interface du mail sender"""
    def __init__(self, window, list_email_user, list_email_send,
                 list_email_cc, list_subject, num_etudiant, password):
        self.num_etudiant = num_etudiant
        self.password = password

        # Fenêtre
        self.fenetre = window
        self.fenetre.title("Mail Sender Sorbonne Université")
        self.fenetre.resizable(width=False, height=False)

        # Style
        self.style = ttk.Style()
        if "clam" in self.style.theme_names():
            self.style.theme_use('clam')

        # Partie du haut
        self.frame = ttk.Frame(self.fenetre)
        self.label_email_user = ttk.Label(self.frame, text="De")
        self.entry_email_user = ttk.Combobox(self.frame, width=50,
                                             values=list_email_user)
        self.entry_email_user.current(0)
        self.label_email_user.grid(row=0, column=0, padx=10, pady=5)
        self.entry_email_user.grid(row=0, column=1, padx=10, pady=5)
        self.label_email_send = ttk.Label(self.frame, text="À")
        self.entry_email_send = ttk.Combobox(self.frame, width=50,
                                             values=list_email_send)
        self.label_email_send.grid(row=1, column=0, padx=10, pady=5)
        self.entry_email_send.grid(row=1, column=1, padx=10, pady=5)
        self.label_email_cc = ttk.Label(self.frame, text="Cc")
        self.entry_email_cc = ttk.Combobox(self.frame, width=50,
                                           values=list_email_cc)
        self.label_email_cc.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email_cc.grid(row=2, column=1, padx=10, pady=5)
        self.label_subject = ttk.Label(self.frame, text="Objet")
        self.entry_subject = ttk.Combobox(self.frame, width=50,
                                          values=list_subject)
        self.label_subject.grid(row=3, column=0, padx=10, pady=5)
        self.entry_subject.grid(row=3, column=1, padx=10, pady=5)
        self.frame.grid(row=0)

        # Corps du texte
        self.entry_body = tk.Text(self.fenetre, height=10)
        self.entry_body.grid(row=1, padx=10, pady=5)

        # Pièces jointes
        self.button_attachment = ttk.Button(self.fenetre,
                                            text="Joindre un fichier",
                                            command=self.open_file)
        self.button_attachment.grid(row=2)

        self.frame_attachment = ttk.Frame(self.fenetre)
        self.frame_attachment.grid(row=3)

        # Bouton d'envoi
        self.button_send = ttk.Button(self.fenetre, text="Envoyer",
                                      command=self.send_message)
        self.button_send.grid(row=4, padx=10, pady=5)

        # Auteur
        self.label_author = ttk.Label(self.fenetre,
                                      text="Quentin Deschamps, 2020")
        self.label_author.grid(row=5, padx=10, pady=5)

    def send_message(self):
        """Lance l'envoi du mail"""
        email_user = self.entry_email_user.get()
        email_send = self.entry_email_send.get()
        email_cc = self.entry_email_cc.get()
        subject = self.entry_subject.get()
        body = self.entry_body.get("1.0", "end")
        if email_user and email_send and subject:
            if not email_cc:
                email_cc = ""
            send_mail(email_user, email_send, email_cc,
                      subject, body, self.num_etudiant, self.password)
            showinfo("Envoi réussi", "Le mail a été envoyé !")
        else:
            showerror("Erreur", "Merci de remplir tous les champs.")

    def open_file(self):
        """Ajoute une pièce jointe"""
        filename = askopenfilename(title="Ouvrir le fichier")
        if filename:
            f = open("data/attachment.txt", "w")
            f.write(filename)
            f.close()
            self.maj_frame_attachment(filename.split("/")[-1])

    def maj_frame_attachment(self, filename):
        """Met à jour le frame des pièces jointes"""
        self.frame_attachment.destroy()
        self.frame_attachment = ttk.Frame(self.fenetre)
        self.label_attachment = ttk.Label(self.frame_attachment, text=filename)
        self.label_attachment.pack()
        self.frame_attachment.grid(row=3)
