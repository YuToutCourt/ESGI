/*!****************************************************
* \file    tp1.c
* \author A Yohann MALEY
* \date   22 octobre 2022
* \brief  contient les définitions des fonctions du tp1
* \version 1.0
******************************************************
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846
#include "tp1.h"


int main(int argc, char const *argv[]){

    
    /*
        __
    ___( o)>  (KOINK)
    \ <_. )
    `---'  
               
    */

    // Affichage du menu et choix de l'utilisateur
    short choix;
    do {
        printf("Choisissez un exercice : \n");
        printf("1. Surface du pentagone\n");
        printf("2. Somme & multiplication\n");
        printf("3. Le plus grand nombre\n");
        printf("4. Suite\n");
        printf("5. Table ASCII\n");
        printf("6. Affichage d'un triangle de sapin\n");
        printf("7. Tableau\n");
        printf("0. Quitter\n");
        scanf("%d", &choix);

        switch (choix){
        case 1:
            printf("Surface du pentagone : %.2f\n", surface_pentagone());
            break;
        case 2:
            somme_multiple();
            break;
        case 3:
            the_greatest();
            break;
        case 4:
            suite();
            break;
        case 5:
            table_ascii();
            break;
        case 6:
            afficheTriangleSapin(10, '*');
            break;
        case 7:
            tableau();
            break;
        case 0:
            printf("Fin du programme.\n");
            break;
        default:
            printf("Erreur, le choix n'est pas valide.\n");
            break;
        }
    } while (choix != 0);


    return 0;
}

float surface_pentagone(){
    int cote, nb_cote;
    printf("Valeur de la mesure d'un cote c : ");
    scanf("%d", &cote);
    printf("Nombre de cote n : ");
    scanf("%d", &nb_cote);

    // Calcul de la surface
    float surface = (nb_cote * pow(cote, 2)) / (4 * tan(PI / nb_cote));
    return surface;

}

void somme_multiple(){
    int nombre;
    printf("Entre une valeur superieur a 0 : ");
    scanf("%d", &nombre);

    int somme = 0, multiple = 1;

    // Allocation dynamique de la memoire
    int *tableau = malloc(nombre * sizeof(int));

    // Calcul de la somme et du multiple
    for(int i = 1; i <= nombre; i++){
        somme += i;
        multiple *= i;
        tableau[i] = i;
    }
    
    // Affichage de la somme
    printf("- %d = ", somme);
    for(int i = 1; i < nombre; i++){
        if (i == nombre - 1) printf("%d + %d\n", tableau[i], tableau[i]+1);
        else printf("%d + ", tableau[i]);
    }

    // Affichage du multiple
    printf("- %d! = %d = ", nombre, multiple);
    for(int i = 1; i < nombre; i++){
        if (i == nombre - 1) printf("%d * %d\n", tableau[i], tableau[i]+1);
        else printf("%d * ", tableau[i]);
    }

    // Liberation de la memoire
    free(tableau);

}

void the_greatest(){
    const short number_of_numbers_to_compare = 5;
    short nombre, max;
    short index = 0;
    for(short i = 0; i < number_of_numbers_to_compare; i++){
        printf("Entrez le nombre numero %d/%d : ", i+1, number_of_numbers_to_compare);
        scanf("%d", &nombre);

        // On initialise le max avec le premier nombre
        if(i == 0) max = nombre;

        if (nombre > max) {
            max = nombre;
            index = i;
        }
        
    }
    printf("Le plus grand nombre est : %d\n", max);
    printf("C etait le nombre numero %d\n", index+1);
}

void suite(){
    int nombre;
    float somme = 0;
    do {
            do {
                printf("Entrez le nombre de terme de la suite a calculer n avec n > 0 (0 pour terminer) : ");
                scanf("%d", &nombre);
                if(nombre < 0) printf("Erreur, la valeur ne peut pas etre negative. \n");
            } while (nombre < 0);

            if(nombre != 0){
                for(int i = 1; i <= nombre; i++){
                    somme += 1. / i;
                }
                printf("U%d est : %.4f \n", nombre, somme);
            }
            somme = 0;
            
    } while (nombre != 0);

    printf("Fin du programme.\n");


}

void table_ascii(){

    short number_of_characters_on_line = 0;
    for(short i = 33; i <= 127; i++){
        printf("[%d, %c] ", i, i);
        number_of_characters_on_line++;

        if(number_of_characters_on_line % 10 == 0) printf("\n");
    }
    printf("\n");
}

void afficheTriangleSapin(const unsigned int n, char c){
    // Les exos avec des patterns sont toujours les plus chiant a faire

    int i, j;
    int nb_espace = n - 1;
    int nb_etoile = 1;

    for(i = 0; i < n; i++){
        for(int j = 0; j < nb_espace; j++){
            printf(" ");
        }
        for(j = 0; j < nb_etoile; j++){
            printf("%c", c);
        }
        printf("\n");
        nb_espace--;
        nb_etoile += 2;
    }

	//Affiche la base du sapin.
	for (i = 0; i <= nb_etoile / 2 - 3; i++) printf(" ");
	printf("***\n");
	for (i = 0; i <= nb_etoile / 2 - 3; i++) printf(" ");
	printf("************* Joyeux Noel *************\n");
}

void tableau(){
    int taille_tableau;
    float somme_of_all;
    do {
        somme_of_all = 0.;
        printf("Entrez la taille du tableau (0 pour terminer): ");
        scanf("%d", &taille_tableau);

        // Allocation dynamique de la memoire d'un tableau a 2 dimensions
        int **tableau = malloc(taille_tableau * sizeof(int*));
        for(int i = 0; i < taille_tableau; i++){
            tableau[i] = malloc(taille_tableau * sizeof(int));
        }

        int somme_ligne = 0, somme_colonne = 0;
        printf("%d", somme_ligne);
        for(int i = 0; i < taille_tableau; i++){
            for(int j = 0; j < taille_tableau; j++){
                printf("Entrez la valeur de la case [%d, %d] : ", i+1, j+1);
                scanf("%d", &tableau[i][j]);
            }
        }

        // Affichage du tableau & la moyenne de chaque ligne
        for(int i = 0; i < taille_tableau; i++){
            for(int j = 0; j < taille_tableau; j++){
                printf("%d\t", tableau[i][j]);
                somme_ligne += tableau[i][j];
            }
            somme_of_all += somme_ligne;
            printf("(%.2f)\n", (float) (somme_ligne / taille_tableau));
            somme_ligne = 0;
        }

        // Affichage de la moyenne de chaque colonne
        for(int i = 0; i < taille_tableau; i++){
            for(int j = 0; j < taille_tableau; j++){
                somme_colonne += tableau[j][i];
            }
            printf("(%.2f)\t", (float) (somme_colonne / taille_tableau));
            somme_colonne = 0;
        }
        printf("(%.2f)\n", somme_of_all / taille_tableau);

        // Libération de la memoire
        for(int i = 0; i < taille_tableau; i++) free(tableau[i]);
        free(tableau);

    } while (taille_tableau > 0);
    printf("Fin du programme.\n");

}