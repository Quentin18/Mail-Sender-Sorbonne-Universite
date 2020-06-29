"""
The ``message`` module manages the messages of the GUI.
It uses the ``tkinter.messagebox`` module.

.. module:: message
    :synopsis: Manage messages.

.. moduleauthor:: Quentin Deschamps <quentindeschamps18@gmail.com>

"""
from tkinter.messagebox import showerror, showinfo, askyesno


def show_login_error():
    """Login error message."""
    showerror("Erreur", "La connexion a échoué. Veuillez réessayer.")


def show_send():
    """Success send message."""
    showinfo("Envoi réussi", "Le mail a été envoyé !")


def show_from_miss():
    """Miss 'from' field message."""
    showerror("Pas d'envoyeur", "Merci d'indiquer votre mail.")


def show_to_miss():
    """Miss 'to' field message."""
    showerror("Pas de destinataires", "Merci d'indiquer les destinataires.")


def show_address_not_valid(mail):
    """'Not valid address' message."""
    showerror("Email non valide", f"L'adresse {mail} n'est pas valide.")


def show_subject_miss():
    """Miss 'subject' field message."""
    showerror("Pas d'objet", "Vous avez oublié d'indiquer l'objet !")


def show_new_user(mail):
    """New user message."""
    return askyesno("Nouvelle adresse",
                    f"Ajouter {mail} à vos adresses ?")


def show_new_contact(mail):
    """New contact message."""
    return askyesno("Nouveau contact",
                    f"Ajouter {mail} à vos contacts ?")


def show_send_error():
    """Send error message."""
    return showerror("Erreur envoi", "L'envoi a échoué !")
