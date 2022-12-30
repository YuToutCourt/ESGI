/*****************************************************
* \file    ptrTableauDouble_2.c
* \author  Yohann MALEY
* \date    15 décembre 2022
* \brief   Contient le code des fonctions du ptrTableauDouble_2
* \version 1.0
******************************************************/

#include "PtrTableauDouble_2.h"


void TableauDouble_construire2(PtrTableauDouble2* ptd, int taille) {
    // Allocation dynamique d'un tableau de taille "taille"
    *ptd = (PtrTableauDouble2) malloc(sizeof(TableauDouble));

    if (*ptd == NULL) {
        printf("Erreur d'allocation mémoire");
        exit(1);
    }

    (*ptd)->a_tab = (double*) malloc(taille * sizeof(double));

    if ((*ptd)->a_tab == NULL) {
        printf("Erreur d'allocation mémoire");
        exit(1);
    }

    (*ptd)->a_taille = taille;

    memset((*ptd)->a_tab, 0, taille * sizeof(double));
    // for (int i = 0; i < taille; i++) (*ptd)->a_tab[i] = 0;
}

void TableauDouble_afficher2(PtrTableauDouble2 ptd) {
    for (unsigned i = 0; i < ptd->a_taille; i++) printf("%f ", ptd->a_tab[i]);
    printf("\n");
}

void TableauDouble_modifier2(PtrTableauDouble2 ptd, int index, double valeur) {
    if (index < 0 || index >= ptd->a_taille) {
        printf("Erreur d'index\nL'index doit etre compris entre 0 et %d", ptd->a_taille - 1);
        exit(1);
    }

    ptd->a_tab[index] = valeur;
}

double TableauDouble_get2(PtrTableauDouble2 ptd, int index) {
    if (index < 0 || index >= ptd->a_taille) {
        printf("Erreur d'index\nL'index doit etre compris entre 0 et %d", ptd->a_taille - 1);
        exit(1);
    }

    return ptd->a_tab[index];
}

void TableauDouble_liberer2(PtrTableauDouble2* ptd) {
    free((*ptd)->a_tab);
    (*ptd)->a_tab = NULL;
    free(*ptd);
    *ptd = NULL;
}

int C_2() {
    PtrTableauDouble2 d1 = NULL;
    unsigned taille_tableau = 5;

    TableauDouble_construire2(&d1, taille_tableau);
    TableauDouble_afficher2(d1);

    TableauDouble_modifier2(d1, 2, 3.13589985);
    TableauDouble_afficher2(d1);
    printf("%5.10f\n",TableauDouble_get2(d1, 2));

    TableauDouble_modifier2(d1, 2, 62.1);
    printf("%5.10f\n",TableauDouble_get2(d1, 2));
    TableauDouble_afficher2(d1);

    TableauDouble_liberer2(&d1);
    // Segmentation fault (core dumped) : d1 est NULL (libéré) et on tente d'y accéder (afficher) !
    // TableauDouble_afficher2(d1); 

    return 0;
}