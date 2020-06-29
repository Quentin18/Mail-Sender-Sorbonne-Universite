"""
The ``email_utils`` module is used to create and send emails.
It uses ``smtplib`` to send an email.

.. module:: email_utils
    :synopsis: Create and send emails.

.. moduleauthor:: Quentin Deschamps <quentindeschamps18@gmail.com>

"""
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from mimetypes import guess_type
from email.header import Header
from email.encoders import encode_base64
from smtplib import SMTP
import logging


class Email(object):
    """Manage emails."""
    @staticmethod
    def get_name_from_address(address):
        """Return the name associated to the address."""
        fullname = address.split('@')[0]
        firstname = ' '.join([
            i.capitalize() for i in fullname.split('.')[0].split('-')])
        name = ' '.join([
            i.capitalize() for i in fullname.split('.')[1].split('_')])
        if name[-1] in '1234567890':
            name = name[:-1]
        return f'{firstname} {name}'

    @staticmethod
    def add_name_to_signature(signature, name, color='#263068'):
        """Add the name to the signature."""
        signature = signature.split('\n')
        line = f'<p><small><font color={color}>{name}</font></small></p>'
        signature.insert(4, line)
        return ''.join(signature)

    def __init__(self, from_, to, cc, subject, message, attachments,
                 signature):
        """Create an email."""
        name = self.get_name_from_address(from_)
        self.from_ = from_
        self.to = to
        self.cc = cc

        self.email = MIMEMultipart()
        self.email['From'] = Header(f'{name} <{from_}>', 'ascii',
                                    header_name=name)
        self.email['To'] = Header(to, 'ascii')
        if cc != '':
            self.email['Cc'] = Header(cc, 'ascii')
        self.email['Subject'] = Header(subject, 'ascii')

        signature = self.add_name_to_signature(signature, name)

        self.email.attach(MIMEText(message, 'plain'))
        self.email.attach(MIMEText(signature, 'html'))

        for filename in attachments:
            mimetype, _ = guess_type(filename)
            mimetype = mimetype.split('/', 1)
            fp = open(filename, 'rb')
            attachment = MIMEBase(mimetype[0], mimetype[1])
            attachment.set_payload(fp.read())
            fp.close()
            encode_base64(attachment)
            attachment.add_header('Content-Disposition', 'attachment',
                                  filename=os.path.basename(filename))
            self.email.attach(attachment)

        logging.info('Mail created')

    def __str__(self):
        """Return the string format."""
        return self.email.as_string()


class EmailConnection(object):
    """Manage communication with the SMTP server."""
    def __init__(self, username, password, server='smtps.upmc.fr', port=587):
        """Create commnection to the server."""
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.connect()
        logging.info('Connected to {}'.format(server))

    def connect(self):
        """Connect to the server."""
        self.connection = SMTP(self.server, self.port)
        self.connection.ehlo()
        self.connection.starttls()
        self.connection.login(self.username, self.password)

    @staticmethod
    def is_valid(username, password, server='smtps.upmc.fr', port=587):
        """Return True if the username and the password are valid."""
        try:
            server = SMTP(server, port)
            server.starttls()
            server.login(username, password)
            server.quit()
        except Exception:
            return False
        else:
            return True

    @staticmethod
    def get_list(addresses):
        """Return a list of addresses from a string."""
        addresses = addresses.split(',')
        return [a.strip() for a in addresses]

    def send(self, message):
        """Envoie un email."""
        from_ = message.from_
        to = self.get_list(message.to)
        cc = self.get_list(message.cc)
        message = str(message)
        logging.info('Sending mail')
        return self.connection.sendmail(from_, to + cc, message)

    def close(self):
        """Ferme la connection."""
        self.connection.close()
        logging.info('Connection closed')
