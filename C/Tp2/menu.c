/*****************************************************
* \file    menu.h
* \author  Yohann MALEY
* \date    22 novembre 2022
* \brief   Contient le code menu
* \version 1.0
******************************************************/

#include "tp2.h"

void menu(){

    short n;
    unsigned choix;

    // Affichage du menu et choix de l'utilisateur
    do {
        printf("\n\nChoisissez un exercice : \n");
        printf("1. Equation du second degre\n");
        printf("2. Suite Rn\n");
        printf("3. Fibonacci\n");
        printf("4. Nombre d'or de Fibonacci\n");
        printf("5. Dice\n");
        printf("0. Quitter\n");
        printf("Votre choix : ");
        scanf("%d", &choix);
        switch (choix)
        {
        case 1:
            equation_second_degre();
            break;
        case 2:
            suite();
            break;
        case 3:
            printf("Entrez la valeur de n : ");
            scanf("%d", &n);
            signed long long int val = fibonacci(n);
            printf("Fibonacci de %d est %lli : F[%d] = %lli\n", n, val, n, val);
            break;
        case 4:
            nombre_or_fibo();
            break;
        case 5:
            dice();
            break;
        case 6:
            printf("Au revoir !\n");
            break;
        default:
            printf("Choix invalide !\n");
            break;
        }

    } while (choix != 0);

}