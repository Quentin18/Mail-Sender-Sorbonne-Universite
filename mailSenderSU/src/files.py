"""
Mail sender Sorbonne Université
Gestion des fichiers
Quentin Deschamps, 2020
"""
import mailSenderSU.src.message as Message
import os


def list_file(file):
    """Retourne la liste des éléments d'un fichier"""
    f = open(file, "r")
    lines = f.readlines()
    ret_list = [i.strip("\n") for i in lines]
    f.close()
    return ret_list


def clear_file(file):
    """Supprime les données d'un fichier"""
    f = open(file, "r+")
    f.truncate(0)
    f.close()


def add_file(file, data):
    """Ajoute une donnée à un fichier"""
    f = open(file, "a")
    f.write(f"{data}\n")
    f.close()


class Files:
    """Gère les fichiers de données"""
    def __init__(self, path):
        self.path = path
        self.file_user = self.absolute_path("/data/user.txt")
        self.file_contacts = self.absolute_path("/data/contacts.txt")
        self.file_subject = self.absolute_path("/data/subjects.txt")
        self.file_signature = self.absolute_path("/data/signature.html")
        self.file_history = self.absolute_path("/data/history.log")
        self.create_files()
        self.list_email_user = list_file(self.file_user)
        self.list_email_send = list_file(self.file_contacts)
        self.list_subject = list_file(self.file_subject)
        self.signature = self.get_signature()

    def absolute_path(self, file):
        """Retourne le chemin absolu d'un fichier"""
        return "".join([self.path, file])

    def create_files(self):
        """Crée les fichiers s'ils n'existent pas"""
        if not os.path.exists(self.file_user):
            with open(self.file_user, 'w'):
                pass
        if not os.path.exists(self.file_contacts):
            with open(self.file_contacts, 'w'):
                pass
        if not os.path.exists(self.file_subject):
            with open(self.file_subject, 'w'):
                pass
        if not os.path.exists(self.file_history):
            with open(self.file_history, 'w'):
                pass

    def get_signature(self):
        """Récupère la signature"""
        f = open(self.file_signature, "r")
        signature = f.read()
        f.close()
        return signature

    def maj_files(self, email_user, email_send, email_cc, text):
        """Met à jour les fichiers de données"""
        add_file(self.file_history, text)
        if email_user not in self.list_email_user:
            if Message.show_new_user(email_user):
                add_file(self.file_user, email_user)
                self.list_email_user.append(email_user)
        if email_send not in self.list_email_send:
            if Message.show_new_contact(email_send):
                add_file(self.file_contacts, email_send)
                self.list_email_send.append(email_send)
        if email_cc != "" and email_cc not in self.list_email_send:
            if Message.show_new_contact(email_cc):
                add_file(self.file_contacts, email_cc)
                self.list_email_user.append(email_cc)
