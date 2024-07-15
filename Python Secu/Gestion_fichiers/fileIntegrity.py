#Import des différentes bibliothèques
import os
import argparse
import hashlib
import json

#fonction de génération du hash afin de fournir un controle de somme pour les fichiers
def md5_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

#Fonction qui retourne un dictionnaire de chaque fichier contenant "id, chemin, taille, md5"
def list_files_in_directory(directory):
    files_dict = {}
    file_id = 1
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_md5 = md5_hash(file_path)
            files_dict[file_id] = {'chemin': file_path, 'taille': file_size, 'md5': file_md5}
            file_id += 1
    return files_dict

def main():
    #Mise en place des arguments
    parser = argparse.ArgumentParser(description='Liste les fichiers dans un dossier spécifié et génère un fichier de sortie avec un hachage MD5 de chaque fichier')
    parser.add_argument('-d', '--directory', type=str, help='Le chemin du dossier à analyser', default='.')
    parser.add_argument('-o', '--output_file', type=str, help='Le chemin du fichier de sortie (JSON)', default='./result.json')
    args = parser.parse_args()
    #Déclaration des variables sorti des arguments
    directory = args.directory
    output_file = args.output_file

    #Vérification que le chemin est un dossier
    if not os.path.isdir(directory):
        print(f"Erreur: {directory} n'est pas un dossier valide.")
        return

    #Ecriture du fichier de sorti au format Json.
    with open(output_file, 'w') as f:
        json.dump(list_files_in_directory(directory), f, indent=4)

    print(f"Les informations des fichiers ont été écrites dans {output_file}")

#Exécution du script
if __name__ == '__main__':
    main()
