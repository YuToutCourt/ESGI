/*****************************************************
* \file    livre.c
* \author  Yohann MALEY
* \date    15 décembre 2022
* \brief   Contient le code des fonctions du livre
* \version 1.0
******************************************************/

#include "livre.h"


void Livre_creer(Livre *livre, char *nom, char *auteur, char *editeur, char *code_barre) {
    livre->nom = nom;
    livre->auteur = auteur;
    livre->editeur = editeur;
    for (int i = 0; i < 13; i++) livre->code_barre[i] = code_barre[i];
}


void Livre_set(Livre *livre, char *attribut, char *valeur) {
    if (strcmp(attribut, "nom") == 0) livre->nom = valeur;
    else if (strcmp(attribut, "auteur") == 0) livre->auteur = valeur;
    else if (strcmp(attribut, "editeur") == 0) livre->editeur = valeur;
    else if (strcmp(attribut, "code_barre") == 0) {
        for (int i = 0; i < 13; i++) livre->code_barre[i] = valeur[i];
    }
}

char *Livre_get(Livre *livre, char *attribut) {
    if (strcmp(attribut, "nom") == 0) return livre->nom;
    else if (strcmp(attribut, "auteur") == 0) return livre->auteur;
    else if (strcmp(attribut, "editeur") == 0) return livre->editeur;
    else if (strcmp(attribut, "code_barre") == 0) return livre->code_barre;
}



void Livre_afficher(Livre *livre) {
    printf("--------------------\n");
    printf("> Nom: %s\n", livre->nom);
    printf("> Auteur: %s\n", livre->auteur);
    printf("> Editeur: %s\n", livre->editeur);
    printf("> Code barre: %s\n", livre->code_barre);
    printf("--------------------\n");
}

int C_3() {
    Livre livre;
    Livre_creer(&livre, "Le petit prince", "Antoine de Saint-Exupéry", "Gallimard", "9782070413095");
    Livre_afficher(&livre);

    Livre_set(&livre, "nom", "Le petit prince 2");
    Livre_set(&livre, "auteur", "Antoine de Saint-Exupéry 2");
    Livre_set(&livre, "editeur", "Gallimard 2");
    Livre_set(&livre, "code_barre", "9782070413096");
    Livre_afficher(&livre);

    printf("Nom: %s", Livre_get(&livre, "nom"));
    printf("Auteur: %s", Livre_get(&livre, "auteur"));
    printf("Editeur: %s", Livre_get(&livre, "editeur"));
    printf("Code barre: %s", Livre_get(&livre, "code_barre"));
    
    return 0;
}
