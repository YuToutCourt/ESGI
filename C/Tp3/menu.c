/*****************************************************
* \file    menu.c
* \author  Yohann MALEY
* \date    15 décembre 2022
* \brief   Contient le code des fonctions du menu
* \version 1.0
******************************************************/

#include "livre.h"
#include "ptrTableauDouble_1.h"
#include "ptrTableauDouble_2.h"

void menu(){
    short n;
    unsigned choix;

    // Affichage du menu et choix de l'utilisateur
    do {
        printf("\n\nChoisissez un exercice : \n");
        printf("1. ptrTableauDouble_1\n");
        printf("2. ptrTableauDouble_2\n");
        printf("3. Livre\n");
        printf("0. Quitter\n");
        printf("Votre choix : ");
        scanf("%d", &choix);
        printf("\n\n");
        switch (choix){
        case 1:
            C_1();
            break;
        case 2:
            C_2();
            break;
        case 3:
            C_3();
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