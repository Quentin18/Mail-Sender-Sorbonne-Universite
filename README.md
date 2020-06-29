# Mail Sender Sorbonne Université
[![Documentation Status](https://readthedocs.org/projects/mail-sender-sorbonne-universite/badge/?version=latest)](https://mail-sender-sorbonne-universite.readthedocs.io/fr/latest/?badge=latest)
[![Build Status](https://travis-ci.org/Quentin18/Mail-Sender-Sorbonne-Universite.svg?branch=master)](https://travis-ci.org/Quentin18/Mail-Sender-Sorbonne-Universite)
![PyPI](https://img.shields.io/pypi/v/mailSenderSU)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mailSenderSU)
[![Downloads](https://pepy.tech/badge/mailsendersu)](https://pepy.tech/project/mailsendersu)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**New release soon...**

**Mail Sender SU** est une application de mail sender en Python pour les étudiants de Sorbonne-Université.
Une CLI (*Command Line Interface*) associée à une GUI (*Graphical User Interface*) permettent d'envoyer
des mails rapidement et facilement avec son adresse *sorbonne-universite*.

![](https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite/blob/master/img/gui.gif)

## Installation
Pour installer l'application, entrez la commande suivante :

```bash
pip3 install mailSenderSU
```

## Utilisation
Consultez la documentation complète [ici](https://mail-sender-sorbonne-universite.readthedocs.io/fr/latest/).

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

### CLI
La CLI permet aussi d'envoyer un mail directement depuis le terminal avec la commande :
```bash
mailSenderSU send
```

## Liens
* GitHub : https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite/
* PyPI : https://pypi.org/project/mailSenderSU/
* Documentation : https://mail-sender-sorbonne-universite.readthedocs.io/fr/latest/
* Travis : https://travis-ci.org/github/Quentin18/Mail-Sender-Sorbonne-Universite/

## Auteur
Quentin Deschamps: quentin.deschamps@etu.sorbonne-universite.fr

## License
[MIT](https://choosealicense.com/licenses/mit/)

![](https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite/blob/master/docs/source/img/polytech_su.png)