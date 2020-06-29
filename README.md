# Mail Sender Sorbonne Université
[![Build Status](https://travis-ci.org/Quentin18/Mail-Sender-Sorbonne-Universite.svg?branch=master)](https://travis-ci.org/Quentin18/Mail-Sender-Sorbonne-Universite)
![PyPI](https://img.shields.io/pypi/v/mailSenderSU)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mailSenderSU)
[![Downloads](https://pepy.tech/badge/mailsendersu)](https://pepy.tech/project/mailsendersu)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**New release soon...**

**Mail Sender SU** est une application de mail sender en Python pour les étudiants de Sorbonne-Université.
Une CLI (Command Line Interface) associée à une GUI (Graphical User Interface) permettent d'envoyer
des mails rapidement et facilement avec son adresse *sorbonne-universite*.

## Installation
Pour installer l'application, entrez la commande suivante :

```bash
pip3 install mailSenderSU
```

## Utilisation
Consultez la documentation complète [ici]().

La CLI de *Mail Sender SU* dispose des commandes suivantes :

```text
Usage: mailSenderSU [OPTIONS] COMMAND [ARGS]...

Mail Sender Sorbonne-University.

Options:
-v, --verbosity  Set the verbosity
--help           Show this message and exit.

Commands:
addcontact   Add contact ADDRESS.
adduser      Add user ADDRESS.
clear        Clear all data files.
contacts     Edit contacts.
delcontacts  Delete contacts.
deluser      Delete user addresses.
gui          Graphical user interface.
send         Send mail.
signature    Edit signature.
user         Edit user.
```

### GUI
Pour utiliser la GUI, utilisez la commande :

```bash
mailSenderSU gui
```

![](https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite/blob/master/docs/source/img/authentification.png)

![](https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite/blob/master/docs/source/img/mail_interface.png)

### CLI
La CLI permet aussi d'envoyer un mail directement depuis le terminal avec la commande :
```bash
mailSenderSU send
```

## Liens
* GitHub : https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite/
* PyPI : https://pypi.org/project/mailSenderSU/
* Documentation :
* Travis : https://travis-ci.org/github/Quentin18/Mail-Sender-Sorbonne-Universite/

## Auteur
Quentin Deschamps: quentin.deschamps@etu.sorbonne-universite.fr

## License
[MIT](https://choosealicense.com/licenses/mit/)
