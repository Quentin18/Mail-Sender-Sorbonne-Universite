.. Mail Sender SU documentation master file, created by
   sphinx-quickstart on Thu Apr  9 08:49:02 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenue sur la documentation de Mail Sender SU !
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

**Mail Sender SU** est une application de mail sender en Python pour les étudiants de Sorbonne Université.
Vous trouverez ce projet au lien suivant : https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite

Installation
============
Python 3.6 ou plus et pip3 sont requis. Pour installer l'application, entrez la commande suivante :
**pip3 install mailSenderSU**

Utilisation
===========
Lancement
---------
Pour lancer Mail Sender SU, entrez :
**mailSenderSU**

.. warning::
   Cette commande ne fonctionne pas sur Windows.

Authentification
----------------
Entrez votre numéro étudiant et votre mot de passe pour vous connecter au serveur. Si la connexion est établie, vous êtes dirigés sur la fenêtre pour rédiger votre mail.

Votre adresse
-------------
Dans le premier champ, vous devez utiliser votre adresse sorbonne-universite.fr ou upmc.fr. Une adresse externe à l'université ne fonctionnera pas.

Destinataires
-------------
Dans le deuxième champ, vous devez mettre les adresses des destinataires. Veuillez les séparer par des virgules s'il y en a plusieurs. Dans le troisième champ, se sont les destinataires en copie. Cela fonctionne identiquement au deuxième champ.

Pièces jointes
--------------
Pour insérer des pièces jointes, pressez le bouton "Joindre un fichier". Sélectionner le(s) fichier(s) à insérer. Il apparaîtront dans le cadre du bas. Vous pouvez supprimer une pièce jointe en cliquant sur celle-ci et en pressant le bouton "Supprimer".

Options
-------
* Obtenir l'aide : **mailSenderSU --help**
* Mettre le style Polytech : **mailSenderSU --style polytech**
* Nettoyer les fichiers : **mailSenderSU --clear [OPTION]** où [OPTION] peut prendre all, user, contacts, history

Modules
=======
.. automodule:: attachment
   :members:

.. automodule:: files
   :members:

.. automodule:: login_interface
   :members:

.. automodule:: mail_interface
   :members:

.. automodule:: message
   :members:

.. automodule:: send
   :members:

.. automodule:: style
   :members:

Contact
=======
Pour reporter un problème ou faire des remarques, veuillez me contacter à l'adresse suivante ; quentin.deschamps.1@sorbonne-universite.fr.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
