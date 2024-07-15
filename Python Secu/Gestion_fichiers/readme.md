# File Integrity

Ce programme permet à l'entreprise DragonTech d'obtenir des informations sur les fichiers présents dans un répertoire.


# Quelles infos ?

Les informations obtenues sont:
* Un id propre au programme
* le chemin des fichiers
* la taille des fichiers
* Une somme de controle afin de vérifier si le fichier n'a pas été altéré

# Utilisations ?

L'utilisation est simple. le programme possède 2 arguments:
* -d: le chemin du dossier à analyser (par défault: ".")
* -o: le chemin du fichier json de sorti (par défault: ./result.json)

Exemple de commande:
```bash
python3 fileintegrity.py -d "/home" -o "./result-home.json"
```
# Exemple de résultat de sortie
```json
 {
    "1": {
        "chemin": "./main.py",
        "taille": 1601,
        "md5": "2b5cd8f1e29fac26d583ca0eadde3adf"
    }
}
```
# Exemple d'intégration dans crontab

On créer une variable temporaire pour le nom du dump

```bash
export $FILE='./fileintegrity-home-$(date +\%Y\%m\%d).json'
```

On déclare ensuite dans le crontab la tache qui va sauvegarder 1 fois par jour à 1H du matin le fichier de dump.
```bash
0 1 * * * python3 /scripts/fileintegrity.py -d "/home/" -o $FILE
```

Il est possible de multiplier les taches cron afin de surveillers plusieurs dossiers.

# Auteurs
Les pyrobarbares DOVAKING