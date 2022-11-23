#include <stdio.h>
#include <stdlib.h>

typedef double* PtrTableauDouble;

void TableauDouble_construire(PtrTableauDouble* ptd, int taille) {
    // Allocation dynamique d'un tableau de taille "taille"
    *ptd = (PtrTableauDouble) malloc(taille * sizeof(double));

    if (*ptd == NULL) {
        printf("Erreur d'allocation mémoire");
        exit(1);
    }

    for (int i = 0; i < taille; i++) (*ptd)[i] = 0;
}

void TableauDouble_afficher(PtrTableauDouble ptd, int taille) {
    for (int i = 0; i < taille; i++) printf("%f ", ptd[i]);
    printf("\n");
}

void TableauDouble_modifier(PtrTableauDouble ptd, int taille, int index, double valeur) {
    if (index < 0 || index >= taille) {
        printf("Erreur d'index\nL'index doit etre compris entre 0 et %d", taille - 1);
        exit(1);
    }

    ptd[index] = valeur;
}

double TableauDouble_get(PtrTableauDouble ptd, int taille, int index) {
    if (index < 0 || index >= taille) {
        printf("Erreur d'index\nL'index doit etre compris entre 0 et %d", taille - 1);
        exit(1);
    }

    return ptd[index];
}

void TableauDouble_liberer(PtrTableauDouble* ptd) {
    free(*ptd);
    *ptd = NULL;
}

int C_1() {

    PtrTableauDouble d1 = NULL;
    unsigned t1=5;

    TableauDouble_construire(&d1, t1);
    TableauDouble_afficher(d1, t1);

    TableauDouble_modifier(d1, t1, 2, 3.13589985);
    TableauDouble_afficher(d1, t1);
    printf("%5.10f\n",TableauDouble_get(d1, t1, 2));
    
    TableauDouble_modifier(d1, t1, 2, 62.1);
    printf("%5.10f\n",TableauDouble_get(d1, t1, 2));
    TableauDouble_afficher(d1, t1);
    
    TableauDouble_liberer(&d1);
    TableauDouble_afficher(d1, t1);

    return 0;
}

int main() {

    return C_1(); 
}
