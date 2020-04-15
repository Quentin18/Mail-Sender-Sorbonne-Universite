"""
Mail sender Sorbonne Université
Envoi du mail
Quentin Deschamps, 2020
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import mailSenderSU.src.message as Message


def get_name_from_email(email):
    """Retourne le nom associé à une adresse mail"""
    fullname = email.split("@")[0]
    firstname = " ".join([
        i.capitalize() for i in fullname.split(".")[0].split("-")])
    name = " ".join([
        i.capitalize() for i in fullname.split(".")[1].split("_")])
    return f"{firstname} {name}"


def list_email(email):
    """Retourne la liste des emails à partir d'une chaîne de caractères"""
    liste = email.split(",")
    liste = [i.strip(" ") for i in liste]
    return liste


def add_name_to_signature(signature, name, color="#263068"):
    """Ajoute le nom à la signature"""
    signature = signature.split("\n")
    line = f'<p><small><font color={color}>{name}</font></small></p>'
    signature.insert(4, line)
    return "".join(signature)


def is_zip(path):
    """Retourne True si le fichier est un zip"""
    return path.split(".")[-1] == "zip"


def send_mail(email_user, email_send, email_cc, subject,
              body, list_attachment, num_etudiant, password,
              signature, server="smtp.upmc.fr", port=587):
    """Envoie le mail"""
    name = get_name_from_email(email_user)
    msg = MIMEMultipart()
    msg['From'] = f"{name} <{email_user}>"
    msg['To'] = email_send
    if email_cc != "":
        msg['Cc'] = email_cc
    msg['Subject'] = subject

    signature = add_name_to_signature(signature, name)

    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(signature, 'html'))

    for path in list_attachment:
        attachment = open(path, 'rb')
        if is_zip(path):
            type_file = 'zip'
        else:
            type_file = 'octet-stream'
        part = MIMEBase('application', type_file)
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        filename = path.split("/")[-1].replace(" ", "_")
        part.add_header('Content-Disposition',
                        'attachment; filename= ' + filename)

        msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP(server, port)
    server.starttls()
    server.login(num_etudiant, password)

    recipients = list_email(email_send)
    if email_cc != "":
        recipients += list_email(email_cc)
    try:
        server.sendmail(email_user, recipients, text)
        server.quit()
    except Exception:
        Message.show_send_mail_error()
        return text
    Message.show_send_mail()
    return text
