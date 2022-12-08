#include <tp3.h>

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
        switch (choix){
        case 1:
            ptrTableauDouble_1();
            break;
        case 2:
            ptrTableauDouble_2();
            break;
        case 3:
            livre();
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