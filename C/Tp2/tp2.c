/*****************************************************
* \file    TP2.h
* \author  Yohann MALEY
* \date    29 octobre 2022
* \brief   Contient le code des fonctions du tp2
* \version 1.0
******************************************************/


#include "tp2.h"
#include "menu.h"


int main(){

    /*
        __
    ___( o)>  (KOINK)
    \ <_. )
    `---'  
 
    */

    srand(time(NULL));  /* initialise le générateur pseudo aléatoire */
    menu();

    return 0;
}


float equation_second_degre(){
    float a, b, c;
    float delta;
    float x1, x2;

    printf("Entrez les coefficients a, b et c de l equation ax^2 + bx + c = 0 : \n");
    scanf("%f %f %f", &a, &b, &c);

    delta = b*b - 4*a*c;

    if (delta < 0) printf("Pas de solution dans R\n");

    else if (delta == 0){
        x1 = -b / (2*a);
        printf("Une solution : x = %.2f\n", x1);
        return x1;

    } else {
        x1 = (-b - sqrt(delta)) / (2*a);
        x2 = (-b + sqrt(delta)) / (2*a);
        printf("Deux solutions : x1 = %.2f et x2 = %.2f\n", x1, x2);
        return x1;
    }
}


void suite(){
    int n;
    float u0 = 2.;
    float un1;

    printf("Entrez la valeur de n : ");
    scanf("%d", &n);

    // Calcul de la valeur de u(n-1)
    for (int i = 0; i <= n-1; i++){
        if (i % 10 == 0) printf("U%d = %.2f\n", i, u0);
        un1 = 0.5 * (u0 + 2/u0);
        u0 = un1;
    }

    // Calcul de la valeur de U(n)
    un1 = 0.5 * (u0 + 2/u0);
    u0 = un1;
    printf("Le resultat de U[%d] est : %.2f\n", n, u0);

    // J'ai pas trop compris le sens de la question, mais j'ai fait ce que je comprennais
    printf("Cette suite tant vers le resultat positif de la resolution de l equation [x^2 - 2] qui est : %.2f\n", equation_second_degre(1, 0, -2));
}

unsigned long long fibonacci(short n){

    // J'utilise unsigned long long car le nombre de fibonacci devient trop grand pour un int

    short val = n;
    unsigned long long  first = 0, second = 1;
    unsigned long long tmp;

    while (n--) {
        tmp = first + second;
        first = second;
        second = tmp;
    }

    return first;
}

void nombre_or_fibo()
{
    int n, i;
    float fn, fn1, fn2, on;
    printf("Calcul de la suite definie par O[n]=F[n+1]/F[n] \n");
    printf("Entrez N :");
    scanf("%d", &n);
    for (i = 1; i <= n; i++){
        fn = fibonacci(i);
        fn1 = fibonacci(i+1);
        on = fn1/fn;
        if (i%5 == 0 || i == 1)  printf("O[%d] = %.2f \n", i, on);
    }
    printf("Le resultat de O[%d] = %.2f \n", n, on);
}

void dice(){

    // Déclaration des variables
    short dices[3];
    short value_we_need[3] = {1, 2, 4};
    short value_gotten[3] = {-1, -1, -1};
    short index_value_gotten = 0;
    short nb_value_gotten;

    short nb_games;
    short nb_wins = 0, nb_loses = 0;
    short nb_dice = 3;
    
    printf("Entrez le nombre de parties : ");
    scanf("%hd", &nb_games);


    // Boucle de jeu sur le nombre de parties
    for (short i = 0; i < nb_games; i++){

        // Boucle sur 3 lancer de dés
        for(short r = 0; r < 3; r++){

            // Ajout de la valeur obtenue dans le tableau de dés
            for (short j = 0; j < nb_dice; j++) dices[j] = roll_dice();

            printf("Lancer %d avec %d des : ", r+1, nb_dice);

            // Affichage des valeurs obtenues
            for (short j = 0; j < 3; j++){
                printf("%d ", dices[j]);
            }

            // Si aucun des dés n'a les valeurs recherchée
            if (!in(1, dices, nb_dice) && !in(2, dices, nb_dice) && !in(4, dices, nb_dice)){
                printf("Je ne garde rien ");
                display_gotten_numbers(value_gotten, 3);
            }
            else {
                nb_value_gotten = 0;
                for (short j = 0; j < 3; j++){
                    // Si la valeur recherchée est présente dans le tableau de dés et qu'elle n'a pas déjà été obtenue
                    if (in(value_we_need[j], dices, 3) && !in(value_we_need[j], value_gotten, 3)){
                        value_gotten[index_value_gotten] = value_we_need[j];
                        index_value_gotten++;
                        nb_value_gotten++;
                    }
                }
                if(nb_value_gotten == 0) printf("Je ne garde rien ");

                else{
                    keep(value_gotten, 3);
                    nb_dice -= index_value_gotten;
                }
                
                display_gotten_numbers(value_gotten, 3);
            }

            // Si toute les valeurs recherchées sont présentes dans le tableau des valeurs obtenues
            if (all_in(value_we_need, value_gotten, 3)) {
                printf("Partie %d gagnee en %d coups", i+1, r+1);
                nb_wins++;
                break;
            }
            else if (r == 2){
                printf("Partie %d perdue", i+1);
                nb_loses++;
            } 
        }

        // Réinitialisation des variables
        printf("\n\n\n");
        nb_dice = 3;
        index_value_gotten = 0;
        memset(value_gotten, -1, 3);
    }

    printf("Vous avez joue %d parties, %d gagnees et %d perdue(s) soit %.2f%% de gain\n", nb_games, nb_wins, nb_loses, (float)nb_wins / nb_games * 100);

}