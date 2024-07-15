import re
import signal
import sys

# Chemins vers les fichiers de journaux
log_files = [
    "/home/yu/Bureau/ESGI/python_secu/examen/forensic/test.log",
    "/home/yu/Bureau/ESGI/python_secu/examen/forensic/forensic_report.txt"
]

# Fichier de sortie pour les résultats de l'analyse
output_file = "/home/yu/Bureau/ESGI/python_secu/examen/forensic/forensic_report.txt"

# Expressions régulières pour détecter les schémas d'attaques potentielles
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

def signal_handler(sig, frame):
    """
    Gère l'interruption du script avec le signal SIGINT (Ctrl+C).
    
    Parameters:
    sig (int): Numéro du signal.
    frame (frame object): Frame actuel (non utilisé dans cette fonction).
    
    Actions:
    - Affiche un message d'arrêt du script.
    - Termine le programme en appelant sys.exit(0).
    """
    print("\nArrêt du script.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def analyze_log_line(line, output):
    """
    Analyse une ligne de journal pour détecter des schémas d'attaques potentielles.
    
    Parameters:
    line (str): Ligne du journal à analyser.
    output (file object): Fichier de sortie pour écrire les résultats de l'analyse.
    
    Actions:
    - Parcourt chaque motif d'attaque dans le dictionnaire patterns.
    - Si une correspondance est trouvée, écrit un message dans le fichier de sortie et l'affiche à l'écran.
    """
    for attack, pattern in patterns.items():
        if pattern.search(line):
            output.write(f"Potentiel {attack} détecté: {line.strip()}\n")
            print(f"Potentiel {attack} détecté: {line.strip()}")

def analyze_logs():
    """
    Analyse les fichiers de journaux spécifiés pour détecter des schémas d'attaques potentielles.
    
    Actions:
    - Ouvre le fichier de sortie en mode append.
    - Pour chaque fichier de journaux dans log_files:
        - Tente d'ouvrir le fichier de journal en lecture.
        - Si le fichier est trouvé, analyse chaque ligne en appelant analyze_log_line.
        - Si le fichier n'est pas trouvé, écrit un message d'erreur dans le fichier de sortie.
        - Si une erreur se produit lors de la lecture du fichier, écrit un message d'erreur dans le fichier de sortie.
    """
    with open(output_file, "a") as output:
        for log_file in log_files:
            try:
                with open(log_file, "r") as file:
                    print(f"Analyse du fichier : {log_file}")
                    for line in file:
                        analyze_log_line(line, output)
            except FileNotFoundError:
                print(f"Le fichier {log_file} est introuvable.")
                output.write(f"Le fichier {log_file} est introuvable.\n")
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier {log_file} : {e}")
                output.write(f"Erreur lors de la lecture du fichier {log_file} : {e}\n")

if __name__ == "__main__":
    """
    Boucle principale du script.
    
    Actions:
    - Appelle analyze_logs pour analyser les journaux.
    - Affiche un message indiquant que l'analyse est terminée et attend de nouvelles données.
    - Attend l'interruption par le signal SIGINT (Ctrl+C) pour arrêter le script.
    """
    while True:
        analyze_logs()
        print("Analyse terminée. En attente de nouvelles données...")
        try:
            signal.pause()
        except AttributeError:
            import time
            time.sleep(1)
