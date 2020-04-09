"""
Mail sender Sorbonne Université
Messages
Quentin Deschamps, 2020
"""
from tkinter.messagebox import showerror, showinfo, askyesno


def show_login_error():
    """Message d'erreur de login"""
    showerror("Erreur", "La connexion a échoué. Veuillez réessayer.")


def show_send_mail():
    """Message d'envoi réussi"""
    showinfo("Envoi réussi", "Le mail a été envoyé !")


def show_email_user_miss():
    """Message d'envoyeur manquant"""
    showerror("Pas d'envoyeur", "Merci d'indiquer votre mail.")


def show_email_send_miss():
    """Message de destinataires manquants"""
    showerror("Pas de destinataires", "Merci d'indiquer les destinataires.")


def show_email_not_valid(mail):
    """Message de mail non valide"""
    showerror("Email non valide", f"L'adresse {mail} n'est pas valide.")


def show_subject_miss():
    """Message d'objet manquant"""
    showerror("Pas d'objet", "Vous avez oublié d'indiquer l'objet !")


def show_new_user(mail):
    """Message de nouvel utilisateur"""
    return askyesno("Nouvelle adresse",
                    f"Ajouter {mail} à vos adresses ?")


def show_new_contact(mail):
    """Message de nouveau contact"""
    return askyesno("Nouveau contact",
                    f"Ajouter {mail} à vos contacts ?")


def show_send_mail_error():
    """Message d'erreur d'envoi"""
    return showerror("Erreur envoi", "L'envoi a échoué !")
