# Fonctionnement du Programme

Le programme va aller chercher des fichiers de logs qu'on lui précisera et les analysera.
Par la suite, des règles vont tourner sur le programme et si il trigger quelque chose de particulier, c'est directement mis dans le fichier de log (que l'on peut préciser également).

# Patterns 

Voici une liste de règles qui peuvent être trigger et affichées dans le fichier de logs : 

```python
patterns = {
    "SQL Injection": re.compile(r"(\%27)|(\')|(\-\-)|(\%23)|(#)|(\%3D)|(\=)|(\%0[9D])|(\%20UNION\%20)|(\%20SELECT\%20)|(\%20DROP\%20)|(\%20INSERT\%20)"),
    "Cross-Site Scripting (XSS)": re.compile(r"(<script>|%3Cscript%3E|alert\(|<img\s+src=|<iframe|<svg|<onload|<body\s+onload|<div\s+onmouseover)"),
    "Local File Inclusion (LFI)": re.compile(r"(\.\./)|(\%2e\%2e/)|(\.\.\\)|(\%2e\%2e\\)|(/etc/passwd)|(\%2F%65%74%63%2F%70%61%73%73%77%64)"),
    "Remote File Inclusion (RFI)": re.compile(r"(http:\/\/|https:\/\/|ftp:\/\/|https\%3A\%2F\%2F|http\%3A\%2F\%2F|ftp\%3A\%2F\%2F)"),
    "Command Injection": re.compile(r"(\;|\||\&\&|\$\(.*\)|\%24\%28.*\%29|<\%20cmd\%20)|(\`)|(\%60)|(\%26%26)|(\%3B)|(\%7C)"),
    "Directory Traversal": re.compile(r"(\.\./)|(\.\.\\)|(\%2e\%2e\%2f)|(\%2e\%2e\%5c)|(\%2e\%2e\%2e\%2e)|(\%2e\%2e\%2e\%5c)|(\%2e\%2e\%2e\%2f)"),
    "Brute Force": re.compile(r"(password=)|(\%70\%61\%73\%73\%77\%6f\%72\%64=)|(\%70\%61\%73\%73=)|(\%75\%73\%65\%72\%6e\%61\%6d\%65=)|(\%75\%6e\%61\%6d\%65=)"),
    "Sensitive Data Exposure": re.compile(r"(ssn=)|(\%73\%73\%6e=)|(\%63\%72\%65\%64\%69\%74\%63\%61\%72\%64\%6e\%75\%6d\%62\%65\%72=)|(\%63\%63\%6e\%75\%6d\%62\%65\%72=)"),
    "File Upload Attack": re.compile(r"(Content-Type:\s+application/octet-stream)|(\.php)|(\.asp)|(\.jsp)|(\%2Ephp)|(\%2Easp)|(\%2Ejsp)"),
    "Path Traversal": re.compile(r"(\.\./)|(\.\.\\)|(\%2e\%2e\%2f)|(\%2e\%2e\%5c)|(\%2f\%2e\%2e\%2f)|(\%5c\%2e\%2e\%5c)"),
    "Buffer Overflow": re.compile(r"(\%25\%25)|(\%5E)|(\%26\%23)"),
    "CSRF (Cross-Site Request Forgery)": re.compile(r"(csrf_token=)|(\%63\%73\%72\%66\%5f\%74\%6f\%6b\%65\%6e=)"),
}
```
Pour en rajouter de nouvelles, il suffit de suivre l'exemple fourni et de les ajouter à la ligne. 


# Disclaimer

Le mieux est d'avoir un fichier par logs pour savoir ce que l'on observe et surveille. On peut très bien, suivant les programmes, agréger les logs en un seul fichier et ensuite alimenter notre pattern. Ca rendra la tâche plus complexe en cas de Forensic.

# Auteurs
Les pyrobarbares DOVAKING