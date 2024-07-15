# Network Analyzer

Ce programme permet à l'entreprise DragonTech de surveiller une interface en temps réels sur une machine ou le script est installé.

# Les prérequis ?
* scapy

Pour l'installer:
```bash
pip install scapy
```

# Quelles infos ?

Les informations obtenues sont:
* le protocol utilisé
* l'adresse source
* l'adresse de destination

# Utilisations ?

L'utilisation est simple. le programme possède 2 arguments:
* -l: lorsque le paramètre est renseigner, celui-ci affiche la liste des interfaces disponibles.
* -i: le nom de l'interface sur laquelle le programme écoute

Exemple de commande:
```bash
python3 networkAnalyzer.py -i "wlp1s0"
```
# Exemple de résultat de sortie
Avec l'option -l:
```bash
['lo', 'wlp1s0', 'virbr0', 'br-5b6d402f06a8', 'docker0', 'br-dae0f51de23e']


```
Avec le scan actif:
```bash
UDP Datagram:
Source Port: 61323
Destination Port: 1900
Ether / IP / UDP 10.213.59.132:61325 > 239.255.255.250:ssdp / Raw
```

# Auteurs
Les pyrobarbares DOVAKING