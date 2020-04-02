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


def send_mail(email_user, email_send, email_cc, subject,
              body, list_attachment, num_etudiant, password,
              signature, server="smtp.upmc.fr", port=587):
    """Envoie le mail"""
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    if email_cc != "":
        msg['Cc'] = email_cc
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(signature, 'html'))

    for path in list_attachment:
        attachment = open(path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        filename = path.split("/")[-1]
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
