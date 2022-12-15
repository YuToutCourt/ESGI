/*****************************************************
* \file    ptrTableauDouble_1.c
* \author  Yohann MALEY
* \date    15 décembre 2022
* \brief   Contient le code des fonctions du ptrTableauDouble_1
* \version 1.0
******************************************************/

#include "ptrTableauDouble_1.h"


void TableauDouble_construire(PtrTableauDouble1* ptd, int taille) {
    // Allocation dynamique d'un tableau de taille "taille"
    *ptd = (PtrTableauDouble1) malloc(taille * sizeof(double));

    if (*ptd == NULL) {
        printf("Erreur d'allocation mémoire");
        exit(1);
    }

    for (int i = 0; i < taille; i++) (*ptd)[i] = 0;
}

void TableauDouble_afficher(PtrTableauDouble1 ptd, int taille) {
    for (int i = 0; i < taille; i++) printf("%f ", ptd[i]);
    printf("\n");
}

void TableauDouble_modifier(PtrTableauDouble1 ptd, int taille, int index, double valeur) {
    if (index < 0 || index >= taille) {
        printf("Erreur d'index\nL'index doit etre compris entre 0 et %d", taille - 1);
        exit(1);
    }

    ptd[index] = valeur;
}

double TableauDouble_get(PtrTableauDouble1 ptd, int taille, int index) {
    if (index < 0 || index >= taille) {
        printf("Erreur d'index\nL'index doit etre compris entre 0 et %d", taille - 1);
        exit(1);
    }

    return ptd[index];
}

void TableauDouble_liberer(PtrTableauDouble1* ptd) {
    free(*ptd);
    *ptd = NULL;
}

int C_1() {

    PtrTableauDouble1 d1 = NULL;
    unsigned taille_tableau = 5;

    TableauDouble_construire(&d1, taille_tableau);
    TableauDouble_afficher(d1, taille_tableau);

    TableauDouble_modifier(d1, taille_tableau, 2, 3.13589985);
    TableauDouble_afficher(d1, taille_tableau);
    printf("%5.10f\n",TableauDouble_get(d1, taille_tableau, 2));
    
    TableauDouble_modifier(d1, taille_tableau, 2, 62.1);
    printf("%5.10f\n",TableauDouble_get(d1, taille_tableau, 2));
    TableauDouble_afficher(d1, taille_tableau);
    
    TableauDouble_liberer(&d1);
    
    // Segmentation fault (core dumped) : d1 est NULL (libéré) et on tente d'y accéder (afficher) !
    // TableauDouble_afficher(d1, taille_tableau); 

    return 0;
}