"""
Mail sender Sorbonne Université
Quentin Deschamps, 2020
"""
from mailSenderSU.src.login_interface import LoginInterface
from mailSenderSU.src.mail_interface import MailSenderInterface
from mailSenderSU.src.files import Files, add_file, clear_file
from mailSenderSU.src.send import send_mail
import os
import click
import tkinter as tk
import logging
import getpass


@click.group()
@click.option('-v', '--verbosity', is_flag=True, help='Set the verbosity')
def cli(verbosity):
    """Mail Sender Sorbonne-University"""
    if verbosity:
        logging.basicConfig(format='%(levelname)s:%(message)s',
                            level=logging.INFO)


@cli.command()
@click.option('--style', help='Style: su or polytech', default='su')
def gui(style):
    """Graphical user interface"""
    path = os.path.dirname(os.path.abspath(__file__))
    logging.info('Creating login window')
    window = tk.Tk()
    login_interface = LoginInterface(window, style, path)
    window.mainloop()
    logging.info('Closed login window')
    if login_interface.login:
        data = Files(path)
        logging.info('Creating mail sender window')
        window = tk.Tk()
        MailSenderInterface(window, style, data,
                            login_interface.num_etudiant,
                            login_interface.password)
        window.mainloop()
        logging.info('Closed mail sender window')


@cli.command()
@click.option('-n', help='Number of recipients', default=1)
def send(n):
    """Send mail"""
    if n < 1:
        raise ValueError('n must be >= 1')
    path = os.path.dirname(os.path.abspath(__file__))
    files = Files(path)
    logging.info('Getting login')
    login = click.prompt('Login')
    logging.info('Getting password')
    pwd = getpass.getpass()
    logging.info('Getting email user')
    if files.list_email_user != []:
        email_user = click.prompt('From', default=files.list_email_user[0])
    else:
        email_user = click.prompt('From')
    logging.info('Getting email send')
    if n == 1:
        email_send = click.prompt('To')
    else:
        email_send = ','.join([click.prompt('To ({}/{})'.format(i + 1, n))
                               for i in range(n)])
    logging.info('Getting email cc')
    email_cc = click.prompt('Cc', default='')
    logging.info('Getting subject')
    subject = click.prompt('Subject')
    logging.info('Getting body')
    body = click.prompt('Body', default='')
    logging.info('Sending mail')
    n_attachment = click.prompt('Number attachments', default=0)
    logging.info('Getting attachments')
    list_attachment = [click.prompt(
                       'Attachment ({}/{})'.format(i + 1, n_attachment),
                       type=click.Path(exists=True))
                       for i in range(n_attachment)]
    ret = send_mail(
        email_user, email_send, email_cc, subject, body,
        list_attachment, login, pwd, files.signature)
    if ret[0]:
        click.echo('Mail succesfully sent')
    else:
        click.echo('Error')


@cli.command()
@click.argument('email')
def addUser(email):
    """Add user email"""
    path = os.path.dirname(os.path.abspath(__file__))
    f = Files(path)
    add_file(f.file_user, email)


@cli.command()
@click.argument('email')
def addContact(email):
    """Add contacts"""
    path = os.path.dirname(os.path.abspath(__file__))
    f = Files(path)
    add_file(f.file_contacts, email)


@cli.command()
def user():
    """Edit user"""
    logging.info('Editing user')
    path = os.path.dirname(os.path.abspath(__file__))
    f = Files(path)
    click.edit(filename=f.file_user)


@cli.command()
def contacts():
    """Edit contacts"""
    logging.info('Editing contacts')
    path = os.path.dirname(os.path.abspath(__file__))
    f = Files(path)
    click.edit(filename=f.file_contacts)


@cli.command()
def signature():
    """Edit signature"""
    logging.info('Editing signature')
    path = os.path.dirname(os.path.abspath(__file__))
    f = Files(path)
    click.edit(filename=f.file_signature)


@cli.command()
def delUser():
    """Delete user addresses"""
    if click.confirm('Do you want to delete user addresses?'):
        path = os.path.dirname(os.path.abspath(__file__))
        f = Files(path)
        clear_file(f.file_user)


@cli.command()
def delContacts():
    """Delete contacts"""
    if click.confirm('Do you want to delete all contacts?'):
        path = os.path.dirname(os.path.abspath(__file__))
        f = Files(path)
        clear_file(f.file_contacts)


@cli.command()
def clear():
    """Clear all data files"""
    if click.confirm('Do you want to clear data files?'):
        path = os.path.dirname(os.path.abspath(__file__))
        f = Files(path)
        f.clear()
