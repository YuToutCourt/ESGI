/*****************************************************
* \file    examen.c
* \author  Yohann MALEY
* \date    10 mars 2023
* \brief   Contient le code des fonctions du examen
* \version 1.0
******************************************************/

#include "examen.h"
#include "menu.h"
#include "fonc.h"


void exercice1(){
    double x;
    unsigned N;
    printf("Entrez x : ");
    scanf("%lf", &x);
    printf("Entrez N : ");
    scanf("%d", &N);
    printf("U0 = %lf\n", suite(x, N));

    printf("atan(x) = %lf\n", atan(x));
    printf("U0 - atan(x) = %lf\n", suite(x, N) - atan(x));
}


void exercice2(){
    unsigned size;
    printf("Entrez la taille du tableau : ");
    scanf("%d", &size);
    Tableau tab = creer_tableau(size);
    for (int i = 0; i < size; i++){
        printf("Entrez la valeur de la case %d : ", i);
        scanf("%lf", &tab[i]);
    }
    printf("Tableau avant permutation : ");
    afficher_tableau(tab, size);
    permuter_tableau(tab, size);
    printf("Tableau apres permutation : ");
    afficher_tableau(tab, size);
    liberer_tableau(&tab);
}


void exercice3(){
    main_article();
}