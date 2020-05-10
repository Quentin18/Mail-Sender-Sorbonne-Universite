# Mail Sender Sorbonne Université
[![Build Status](https://travis-ci.org/Quentin18/Mail-Sender-Sorbonne-Universite.svg?branch=master)](https://travis-ci.org/Quentin18/Mail-Sender-Sorbonne-Universite)

Application de mail sender en Python pour les étudiants de Sorbonne Université.

## Installation
Python 3.6 ou plus et pip3 sont requis. Pour installer l'application, entrez la commande suivante :

```bash
pip3 install mailSenderSU
```

## Utilisation
Il est recommandé d'utiliser cette application sur Linux. Elle reste utilisable sur Windows mais sans les options.
![](https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite/blob/master/img/interface.gif)

### Lancement
Pour lancer Mail Sender SU, entrez dans un terminal :
```bash
mailSenderSU
```
Sur Windows, ouvrez un terminal en faisant win+r puis cmd et entrez :
```bash
python3 -m mailSenderSU
```
Cette commande est aussi utilisable sur Linux.

### Authentification
Entrez votre numéro étudiant et votre mot de passe pour vous connecter au serveur. Si la connexion est établie, vous êtes dirigés sur la fenêtre pour rédiger votre mail.

### Votre adresse
Dans le premier champ, vous devez utiliser votre adresse sorbonne-universite.fr ou upmc.fr. Une adresse externe à l'université ne fonctionnera pas.

### Destinataires
Dans le deuxième champ, vous devez mettre les adresses des destinataires. Veuillez les séparer par des virgules s'il y en a plusieurs. Dans le troisième champ, ce sont les destinataires en copie. Cela fonctionne identiquement au deuxième champ.

### Pièces jointes
Pour insérer des pièces jointes, pressez le bouton "Joindre un fichier". Sélectionnez le(s) fichier(s) à insérer. Il apparaîtront dans le cadre du bas. Vous pouvez supprimer une pièce jointe en cliquant sur celle-ci puis en pressant le bouton "Supprimer".

### Signature
Les mails envoyés comporteront une signature automatique avec votre nom et les logos de l'université.
![](https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite/blob/master/img/mail_exemple.png)

### Options
- Obtenir l'aide :
```bash
mailSenderSU --help
```

- Mettre le style Polytech :
```bash
mailSenderSU --style polytech
```
![](https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite/blob/master/img/polytech_style.png)

- Nettoyer les fichiers :
```bash
mailSenderSU --clear [OPTION]
```
où [OPTION] peut prendre all, user, contacts, history

## Contact
Pour reporter un problème ou faire des remarques, veuillez me contacter à l'adresse suivante : quentin.deschamps@etu.sorbonne-universite.fr.

## License
[MIT](https://choosealicense.com/licenses/mit/)
