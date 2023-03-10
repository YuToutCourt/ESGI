/*****************************************************
* \file    menu.c
* \author  Yohann MALEY
* \date    10 mars 2023
* \brief   Contient le code menu
* \version 1.0
******************************************************/

#include "examen.h"

void menu(){

    short n;
    unsigned choix;

    // Affichage du menu et choix de l'utilisateur
    do {
        printf("\n\nChoisissez un exercice : \n");
        printf("1. Exo 1\n");
        printf("2. Exo 2\n");
        printf("3. Exo 3\n");
        printf("0. Quitter\n");
        printf("Votre choix : ");
        scanf("%d", &choix);
        switch (choix) {
        case 1:
            exercice1();
            break;
        case 2:
            exercice2();
            break;
        case 3:
            exercice3();
            break;
        case 0:
            printf("Au revoir !\n");
            break;
        default:
            printf("Choix invalide !\n");
            break;
        }

    } while (choix != 0);

}