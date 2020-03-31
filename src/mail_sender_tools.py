"""
Mail sender Sorbonne Université
Outils de création et d'envoi du mail
Quentin Deschamps, 2020
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def list_file(file):
    """Retourne la liste des éléments d'un fichier"""
    f = open(file, "r")
    lines = f.readlines()
    ret_list = [i.strip("\n") for i in lines]
    f.close()
    return ret_list


def import_config():
    """Importe les configurations"""
    list_email_user = list_file("data/user.txt")
    list_email_send = list_file("data/contacts.txt")
    list_subject = list_file("data/subjects.txt")
    return list_email_user, list_email_send, list_subject


def clear_file(file):
    """Supprime les données d'un fichier"""
    f = open(file, "r+")
    f.truncate(0)
    f.close()


def get_attachment():
    """Récupère les pièces jointes"""
    f = open("data/attachment.txt", "r")
    path = f.read()
    filename = path.split("/")[-1]
    f.close()
    return path, filename


def get_signature():
    """Récupère la signature"""
    f = open("data/signature.html", "r")
    signature = f.read().strip("\n")
    f.close()
    return signature


def send_mail(email_user, email_send, email_cc,
              subject, body, num_etudiant, password,
              server="smtp.upmc.fr", port=587):
    """Envoie le mail"""
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    if email_cc != "":
        msg['Cc'] = email_cc
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    signature = get_signature()
    msg.attach(MIMEText(signature, 'html'))

    path, filename = get_attachment()
    if path != "":
        attachment = open(path, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= " + filename)

        msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP(server, port)
    server.starttls()
    server.login(num_etudiant, password)

    recipients = [email_send]
    if email_cc != "":
        recipients.append(email_cc)
    server.sendmail(email_user, recipients, text)
    server.quit()
