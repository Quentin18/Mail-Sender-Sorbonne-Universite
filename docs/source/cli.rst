CLI
===
Voici les différentes commandes de la CLI :

Envoyer un mail
---------------
Il est aussi possible d'envoyer un mail via le terminal avec la commande ``send`` :

.. code-block:: bash

   mailSenderSU send [OPTIONS]

On vous demandera :

* Votre identifiant (numéro étudiant)
* Votre mot de passe
* Votre adresse d'envoi
* Les adresses des destinataires (et ceux en copie)
* L'objet du mail
* Le message
* Les pièces jointes

.. note:: Cette méthode est à utiliser si le message est plutôt court. Sinon, privilégier l'utilisation de la GUI.

Gérer les adresses
------------------
L'application *Mail Sender SU* garde en mémoire vos adresses et celles de vos contacts.
Vous pouvez gérer ces adresses avec les commandes suivantes :

* ``addcontact`` : ajoute une nouvelle adresse à votre liste des contacts.

.. code-block:: bash

    mailSenderSU addcontact [OPTIONS] ADDRESS

* ``adduser`` : ajoute une nouvelle adresse utilisateur.

.. code-block:: bash

    mailSenderSU adduser [OPTIONS] ADDRESS

* ``contacts`` : ouvre le fichier des contacts sur votre éditeur de texte par défaut. Vous pouvez alors ajouter ou supprimer des contacts facilement.

.. code-block:: bash

    mailSenderSU contacts [OPTIONS]

* ``user`` : ouvre le fichier des adresses utilisateur sur votre éditeur de texte par défaut.

.. code-block:: bash

    mailSenderSU user [OPTIONS]

* ``delcontacts`` : supprime tous vos contacts.

.. code-block:: bash

    mailSenderSU delcontacts [OPTIONS]

* ``deluser`` : supprime toutes vos adresses utilisateur.

.. code-block:: bash

    mailSenderSU deluser [OPTIONS]

* ``clear`` : supprime vos adresses et vos contacts.

.. code-block:: bash

    mailSenderSU clear [OPTIONS]

.. note:: Évitez de laisser une ligne vierge à la fin des fichiers d'adresses. Un groupe de plusieurs adresses peut être inscrite dans les contacts (sur une ligne, séparer par des virgules).

Gérer la signature
------------------
Les mails envoyés avec *Mail Sender SU* contiennent une signature automatique avec votre nom
et les logos de l'université comme ci-dessous.

.. image:: img/signature.png

Vous pouvez modifier cette signature HTML avec la commande suivante :

.. code-block:: bash

    mailSenderSU signature [OPTIONS]

Le fichier ``signature.html`` utilisé sera ouvert dans votre éditeur de texte par défaut
et vous pourrez ajouter des informations, des liens ou des images.
