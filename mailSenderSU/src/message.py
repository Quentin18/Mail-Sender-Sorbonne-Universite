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


def show_send_mail_error():
    showerror("Erreur", "Merci de remplir tous les champs.")


def show_new_user(mail):
    return askyesno("Nouvelle adresse",
                    f"Ajouter {mail} à vos adresses ?")


def show_new_contact(mail):
    return askyesno("Nouveau contact",
                    f"Ajouter {mail} à vos contacts ?")
