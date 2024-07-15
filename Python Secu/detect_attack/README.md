# Detect Attack (SNORT BUT IN PYTHON)

## Description

Ce script va permettre de détecter des attaques sur un serveur en temps réel. Il va analyser les logs que l'utilisateur lui donne et va détecter des attaques en fonction de règles que l'utilisateur aura défini.

Ce qui le rend très modulable et adaptable à tout type de serveur.

On a choisi d'utiliser watchdog pour surveiller les logs en temps réel. 

Pourquoi watchdog ? Car il permet de surveiller les logs en temps réel et de ne pas avoir à relancer le script à chaque fois qu'un log est modifié.

**watchdog:** https://pypi.org/project/watchdog/


## Utilisation

```bash
python3 detect_attack.py -h
python3 detect_attack.py -l "/var/log/auth.log" "/var/log/syslog" -r "rules.txt"
```

### Exemple of rules.txt

```txt
Failed password
Invalid user           
authentication failure   
session opened for user
```

## Exemple de sorti

```bash
Started monitoring /var/log/auth.log for suspicious activity...      


Suspicious activity detected in /var/log/auth.log: Jul 15 13:53:27 pterodactyl sshd[1454623]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh    
ruser= rhost=141.98.10.15  user=root                                                                                                                                        
Suspicious activity detected in /var/log/auth.log: Jul 15 13:53:30 pterodactyl sshd[1454623]: Failed password for root from 141.98.10.15 port 50624 ssh2                    
Suspicious activity detected in /var/log/auth.log: Jul 15 13:53:32 pterodactyl sshd[1454603]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh    
ruser= rhost=159.89.99.112  user=root   
```

# Auteurs
Les pyrobarbares DOVAKING