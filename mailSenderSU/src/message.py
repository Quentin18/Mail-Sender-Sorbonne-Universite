"""
Mail sender Sorbonne Université
Messages
Quentin Deschamps, 2020
"""
from tkinter.messagebox import showerror, showinfo, askyesno


def show_login_error():
    showerror("Erreur", "La connexion a échoué. Veuillez réessayer.")


def show_send_mail():
    showinfo("Envoi réussi", "Le mail a été envoyé !")


def show_email_user_miss():
    showerror("Pas d'envoyeur", "Merci d'indiquer votre mail.")


def show_email_send_miss():
    showerror("Pas de destinataires", "Merci d'indiquer les destinataires.")


def show_email_not_valid(mail):
    showerror("Email non valide", f"L'email {mail} n'est pas valide.")


def show_subject_miss():
    showerror("Pas d'objet", "Vous avez oublié d'indiquer l'objet !")


def show_new_user(mail):
    return askyesno("Nouvelle adresse",
                    f"Ajouter {mail} à vos adresses ?")


def show_new_contact(mail):
    return askyesno("Nouveau contact",
                    f"Ajouter {mail} à vos contacts ?")
