#include <stdio.h>
#include <stdlib.h>

typedef struct {
    double* a_tab;
    unsigned int a_taille;
} TableauDouble;

typedef TableauDouble* PtrTableauDouble;

void TableauDouble_construire(PtrTableauDouble* ptd, int taille) {
    // Allocation dynamique d'un tableau de taille "taille"
    *ptd = (PtrTableauDouble) malloc(sizeof(TableauDouble));

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

    for (int i = 0; i < taille; i++) (*ptd)->a_tab[i] = 0;
}

void TableauDouble_afficher(PtrTableauDouble ptd) {
    for (int i = 0; i < ptd->a_taille; i++) printf("%f ", ptd->a_tab[i]);
    printf("\n");
}

void TableauDouble_modifier(PtrTableauDouble ptd, int index, double valeur) {
    if (index < 0 || index >= ptd->a_taille) {
        printf("Erreur d'index\nL'index doit etre compris entre 0 et %d", ptd->a_taille - 1);
        exit(1);
    }

    ptd->a_tab[index] = valeur;
}

double TableauDouble_get(PtrTableauDouble ptd, int index) {
    if (index < 0 || index >= ptd->a_taille) {
        printf("Erreur d'index\nL'index doit etre compris entre 0 et %d", ptd->a_taille - 1);
        exit(1);
    }

    return ptd->a_tab[index];
}

void TableauDouble_liberer(PtrTableauDouble* ptd) {
    free((*ptd)->a_tab);
    (*ptd)->a_tab = NULL;
    free(*ptd);
    *ptd = NULL;
}

int C_2() {
    PtrTableauDouble d1 = NULL;
    unsigned t1=5;

    TableauDouble_construire(&d1, t1);
    TableauDouble_afficher(d1);

    TableauDouble_modifier(d1, 2, 3.13589985);
    TableauDouble_afficher(d1);
    printf("%5.10f\n",TableauDouble_get(d1, 2));

    TableauDouble_modifier(d1, 2, 62.1);
    printf("%5.10f\n",TableauDouble_get(d1, 2));
    TableauDouble_afficher(d1);

    TableauDouble_liberer(&d1);
    TableauDouble_afficher(d1);

    return 0;
}

int main() {

    return C_2(); 
}
