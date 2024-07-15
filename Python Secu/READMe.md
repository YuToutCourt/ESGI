Yohann MALEY
Samuel NUEZ
Florent LEBORGNE


#  Analyse du besoin

## Identification des besoins

La société **DragonTech** a besoin d'outil pour automatiser certaines tâches comme l'analyse de logs de leurs machines mais aussi de la prise de décision automatique. Par exemple, en cas de tentative de brute force, on bloque l'adresse IP source.
Il est possible à l'aide d'outils maisons de pouvoir répondre à ces besoins et notamment avec le langage Python qui sera adéquat pour résoudre les différentes problématiques que **DragonTech** rencontre aujourd'hui.

## Etat de l'art 

**Surveillance en temps réel**

    IDS/IPS (Systèmes de détection et de prévention des intrusions) : Outils comme Snort, Suricata et Zeek.
    SIEM (Gestion des informations et des événements de sécurité) : Solutions comme Splunk, IBM QRadar, et ArcSight.

**Gestion de fichiers**

    Systèmes de gestion de fichiers : Solutions comme Tripwire pour l'intégrité des fichiers.
    Outils de journalisation et d'audit : Logiciels comme ELK Stack (Elasticsearch, Logstash, Kibana) pour analyser les journaux de fichiers.

**Détection d'attaques**

    Outils de détection des anomalies : Logiciels comme OSSEC et AlienVault USM.
    Analyse de journaux : Utilisation de scripts personnalisés en Python pour analyser les journaux de serveur.


## Présentation des besoins fonctionnels

**Surveillance en temps réel**

    Surveillance réseau : Analyse des paquets réseau en temps réel.
    Gestion de fichiers : Surveillance de l'intégrité des fichiers critiques.
    Analyse Forensic : Analyse des journaux pour détecter les attaques.

**Détection d'attaques**

    Détection d'attaques : Analyse des journaux pour détecter les attaques en temps réel.
    Prise de décision automatique : Blocage d'adresses IP en cas de tentative de brute force.



# Conception Technique 

Notre choix technologique va se tourner vers un HoneyPot qui mettra à jour les différentes machines de notre client via divers script python. Ce dernier sera en front et encaissera toutes les attaques possibles pour avoir un schéma et des patterns que les attaquants utiliseront.

## Schéma d'architecture

```
                   +----------------------+
                   |       Pare-feu       |
                   |       (pfSense)      |
                   +-----------+----------+
                               |
                               v
                   +----------------------+
                   |        IDS/IPS       |
                   |       (Snort)        |
                   +-----------+----------+
                               |
                               v
                   +----------------------+
                   |       Serveur SIEM   |
                   |       (Splunk)       |
                   +-----------+----------+
                               |
                               v
                   +----------------------+
                   | Serveur de gestion   |
                   |     de fichiers      |
                   |     (Tripwire)       |
                   +-----------+----------+
                               |
                               v
                   +----------------------+
                   x| Serveur de scripts   |
                   |      (Python)        |
                   +----------------------+
                     /   |    |   |   |   \
                    /    |    |   |   |    \
                   v     v    v   v   v     v
         Surv. réseau  Gest. fichiers  Dét. attaques  An. forens.
```
On a séparer chaque script python en fonction de leur utilité. On a un script pour la surveillance réseau, un autre pour la gestion de fichiers, un autre pour la détection d'attaques et un dernier pour l'analyse forensique. 

Le client va pouvoir gérer les scripts comme il le veut. Lancer qu'un un script ou plusieurs en même temps pour ces besoins.



## Explication des choix technologiques

LIRE READMED DE CHAQUE SCRIPT 


# Rapport 

Le projet est découpé en plusieurs scripts Python avec chacun leur utilité :  

- Vérifier le checksum de certains fichiers, intéressant dans le cas d'une attaque par ransomware ou modification de fichiers critiques.


- Analyse Forensic pour analyser et enregistrer les différents patterns qu'un attaquant va utiliser.

- La surveillance réseau qui va lister toutes les actions passant par une interface réseau précise (une sorte de TCPdump).

- Et enfin la détection d'attaque qui elle va lire en temps réelles les logs d'un service (comme SSH) et faire remonter les informations en cas d'un brute force par exemple.



# Auteurs
Les pyrobarbares DOVAKING

