"""
.. module:: cli
    :synopsis: Manage command line interface.

.. moduleauthor:: Quentin Deschamps <quentindeschamps18@gmail.com>

"""
from mailSenderSU.src.login_interface import LoginInterface
from mailSenderSU.src.mail_interface import MailSenderInterface
from mailSenderSU.src.files import File
from mailSenderSU.src.email_utils import Email, EmailConnection
import os
from pathlib import Path
import click
import tkinter as tk
import logging
import getpass


@click.group()
@click.option('-v', '--verbosity', is_flag=True, help='Set the verbosity')
def cli(verbosity):
    """Mail Sender Sorbonne-University."""
    if verbosity:
        logging.basicConfig(format='%(levelname)s:%(message)s',
                            level=logging.INFO)


@cli.command()
@click.option('--style', help='Style: su/polytech', default='su')
def gui(style):
    """Graphical user interface."""
    window = tk.Tk()
    login_interface = LoginInterface(window, style)
    window.mainloop()
    if login_interface.login:
        window = tk.Tk()
        MailSenderInterface(
            window, style,
            login_interface.username,
            login_interface.password)
        window.mainloop()
        logging.info('Mail sender window closed')


@cli.command()
def send():
    """Send mail."""
    # Login
    logging.info('Getting username')
    username = click.prompt('Username')
    logging.info('Getting password')
    password = getpass.getpass()
    logging.info('Validating username and password')
    if not EmailConnection.is_valid(username, password):
        click.echo('Unable to connect to the server')
        quit()

    # Files
    directory = Path(os.path.dirname(os.path.abspath(__file__)))
    user_file = File(directory.joinpath('data', 'user.txt'))
    user_list = user_file.get_list()
    signature_file = File(directory.joinpath('data', 'signature.html'))

    # From
    logging.info('Getting from')
    if user_list != []:
        from_ = click.prompt('From', default=user_list[0])
    else:
        from_ = click.prompt('From')

    # To
    logging.info('Getting to')
    to = click.prompt('To')

    # Cc
    logging.info('Getting cc')
    cc = click.prompt('Cc', default='')

    # Subject
    logging.info('Getting subject')
    subject = click.prompt('Subject')

    # Message
    logging.info('Getting message')
    message = click.prompt('Message', default='')

    # Attachments
    attachments = []
    if click.confirm('Attach files?'):
        logging.info('Getting attachments')
        attachments.append(
            click.prompt('Filename', type=click.Path(exists=True)))
        while click.confirm('Add file?'):
            attachments.append(
                click.prompt('Filename', type=click.Path(exists=True)))

    if click.confirm('Are you sure to send the mail?'):
        # Send email
        server = EmailConnection(username, password)
        email = Email(from_, to, cc, subject, message, attachments,
                      signature_file.read())
        print(email)
        if server.send(email):
            click.echo('Successfully sent email')
        else:
            click.echo('Error')

        server.close()


@cli.command()
@click.argument('address')
def addUser(address):
    """Add user ADDRESS."""
    directory = Path(os.path.dirname(os.path.abspath(__file__)))
    user_file = File(directory.joinpath('data', 'user.txt'))
    user_file.add(address)


@cli.command()
@click.argument('address')
def addContact(address):
    """Add contact ADDRESS."""
    directory = Path(os.path.dirname(os.path.abspath(__file__)))
    contacts_file = File(directory.joinpath('data', 'contacts.txt'))
    contacts_file.add(address)


@cli.command()
def user():
    """Edit user."""
    logging.info('Editing user')
    directory = Path(os.path.dirname(os.path.abspath(__file__)))
    click.edit(filename=str(directory.joinpath('data', 'user.txt')))


@cli.command()
def contacts():
    """Edit contacts."""
    logging.info('Editing contacts')
    directory = Path(os.path.dirname(os.path.abspath(__file__)))
    click.edit(filename=str(directory.joinpath('data', 'contacts.txt')))


@cli.command()
def signature():
    """Edit signature."""
    logging.info('Editing signature')
    directory = Path(os.path.dirname(os.path.abspath(__file__)))
    click.edit(filename=str(directory.joinpath('data', 'signature.html')))


@cli.command()
def delUser():
    """Delete user addresses."""
    if click.confirm('Do you want to delete user addresses?'):
        directory = Path(os.path.dirname(os.path.abspath(__file__)))
        user_file = File(directory.joinpath('data', 'user.txt'))
        user_file.clear()


@cli.command()
def delContacts():
    """Delete contacts."""
    if click.confirm('Do you want to delete all contacts?'):
        directory = Path(os.path.dirname(os.path.abspath(__file__)))
        contacts_file = File(directory.joinpath('data', 'contacts.txt'))
        contacts_file.clear()


@cli.command()
def clear():
    """Clear all data files."""
    if click.confirm('Do you want to clear data files?'):
        directory = Path(os.path.dirname(os.path.abspath(__file__)))
        user_file = File(directory.joinpath('data', 'user.txt'))
        user_file.clear()
        contacts_file = File(directory.joinpath('data', 'contacts.txt'))
        contacts_file.clear()
