# Python-avancé

## Fonctionnement

### Téléchargement du projet

Pour lancer notre projet sur votre machine, veuillez le cloner sur votre ordinateur puis le lancer sur votre IDE.  

Après cela il vous faudra un environnement virtuel python à la base de ce projet. Dans le terminal entrez la commande suivante :

```bash
python -m venv nom_de_l-envrionnement_virtuel
```  

Puis, sur Windows, lancez celui-ci avec la commande : 

```bash
nom_de_l-envrionnement_virtuel/Scripts/Activate.ps1
```  

### Installation des librairies 

Pour le fonctionnement de l'application, certaines librairies sont nécessaires.

Installez les librairies requises pour le fonctionnement du projet avec la commande :  
```bash
pip install -r requirements.txt 
```  

### Lancement du site web 

Enfin vous pouvez désormais lancer l'application avec la commande : 
```bash
python ./application/app.py
```  

Le premier lancement prendra du temps pour télécharger les données depuis 1996 mais ensuite, une fois les que les données
seront présentes sur votre machine l'application ne téléchargera que le mois dernier et celui en cours. 
