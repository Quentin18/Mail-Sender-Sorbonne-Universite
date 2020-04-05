# Mail Sender Sorbonne Université

Application de mail sender en Python pour les étudiants de Sorbonne Université.

## Installation
Python 3.6 ou plus et pip3 sont requis. Pour installer l'application, entrez la commande suivante :

```bash
pip3 install mailSenderSU
```

## Utilisation
### Lancement
- Pour lancer Mail Sender SU, entrez :
```bash
mailSenderSU
```
### Authentification
Entrez votre numéro étudiant et votre mot de passe pour vous connecter au serveur. Si la connexion est établie, vous êtes dirigés sur la fenêtre pour rédiger votre mail.

### Votre adresse
Dans le premier champ, vous devez utiliser votre adresse sorbonne-universite.fr ou upmc.fr. Une adresse externe à l'université ne fonctionnera pas.

### Destinataires
Dans le deuxième champ, vous devez mettre les adresses des destinataires. Veuillez les séparer par des virgules s'il y en a plusieurs. Dans le troisième champ, se sont les destinataires en copie. Cela fonctionne identiquement au deuxième champ.

### Pièces jointes
Pour insérer des pièces jointes, pressez le bouton "Joindre un fichier". Sélectionner le(s) fichier(s) à insérer. Il apparaîtront dans le cadre du bas. Vous pouvez supprimer une pièce jointe en cliquant sur celle-ci et en pressant le bouton "Supprimer".

### Options
- Obtenir l'aide :
```bash
mailSenderSU --help
```

- Mettre le style Polytech :
```bash
mailSenderSU --style polytech
```

- Nettoyer les fichiers :
```bash
mailSenderSU --clear [OPTION]
```
où [OPTION] peut prendre all, user, contacts, subjects, history

## Contact
Pour reporter un problème ou faire des remarques, veuillez me contacter à l'adresse suivante ; quentin.deschamps.1@sorbonne-universite.fr.

## License
[MIT](https://choosealicense.com/licenses/mit/)