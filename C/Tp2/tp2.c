#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "tp2.h"


int main(int argc, char const *argv[]){

    dice();
    return 0;
}


void equation_second_degre(){
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

    } else {
        x1 = (-b - sqrt(delta)) / (2*a);
        x2 = (-b + sqrt(delta)) / (2*a);
        printf("Deux solutions : x1 = %.2f et x2 = %.2f\n", x1, x2);
    }
}


void suite(){
    int n;
    float u0 = 2;
    float un, un1;

    printf("Entrez la valeur de n : ");
    scanf("%d", &n);

    for (int i = 0; i < n-1; i++){
        un1 = 0.5 * (u0 + 2/u0);
        u0 = un1;
        if (i % 10 == 0) printf("U%d = %.2f\n", i, u0);
    }
    un1 = 0.5 * (u0 + 2/u0);
    u0 = un1;
    printf("Le resultat de U[%d] est : %.2f\n", n, u0);
}

unsigned long long int fibonacci(){

    unsigned long long int n;
    printf("Entrez la valeur de n : ");
    scanf("%d", &n);
    unsigned long long int val = n;
    unsigned long long int first = 0, second = 1;
    unsigned long long int tmp;

    while (n--) {
        tmp = first + second;
        first = second;
        second = tmp;
    }
    printf("Fibonacci de %d est %d : F[%d] = %d\n", val, first, val, first);
    return first;
}

void nombre_or_fibo(){

    int n;
    printf("Entrez la valeur de n : "); 
    scanf("%d", &n);

    for(int i = 1; i <= n; i++){
        if (i % 5 == 0) printf("O[%d] = %f\n", i, fibonacci(i+1)/fibonacci(i));
    }

    printf("Le resultat de O[%d] est %f\n", n, fibonacci(n+1)/fibonacci(n));
    printf("Le nombre d'or est egal a : %f\n", fibonacci(n+1)/fibonacci(n));

}

void dice(){


    short dices[3];
    short value_we_need[3] = {1, 2, 4};
    short value_gotten[3] = {-1, -1, -1};
    short index_value_gotten = 0;

    short nb_games;
    short nb_wins = 0, nb_loses = 0;
    short nb_dice = 3, nb_roll = 0;
    
    printf("Entrez le nombre de parties : ");
    scanf("%d", &nb_games);

    for (short i = 0; i < nb_games; i++){

        for(short r = 0; r < 3; r++){

            for (short j = 0; j < nb_dice; j++){
                dices[j] = random_value();
            }

            printf("Lancer %d avec %d des : ", r+1, nb_dice);

            for (short j = 0; j < 3; j++){
                printf("%d ", dices[j]);
            }

            // if any of the dices have given a value we need
            if (index_(1, dices, nb_dice) == -1 && index_(2, dices, nb_dice) == -1 && index_(4, dices, nb_dice) == -1){
                printf("Je ne garde rien ");
                display_gotten_numbers(value_gotten, 3);
            }
            else {
                for (short j = 0; j < 3; j++){
                    if (index_(value_we_need[j], dices, nb_dice) != -1 && !in(value_we_need[j], value_gotten, 3)){
                        value_gotten[index_value_gotten] = value_we_need[j];
                        index_value_gotten++;
                        nb_dice--;
                    }
                }
                keep(value_gotten, 3);
                display_gotten_numbers(value_gotten, 3);
            }

            if (nb_dice == 0) {
                printf("Partie %d gagnee en %d coups", i+1, r+1);
                nb_wins++;
            }
            else if (r == 2){
                printf("Partie %d perdue", i+1);
                nb_loses++;
            } 
        }

        printf("\n\n\n");
        nb_dice = 3;
        index_value_gotten = 0;
        value_gotten[0] = -1;
        value_gotten[1] = -1;
        value_gotten[2] = -1;
    }

    printf("Vous avez joue %d parties, %d gagnees et %d perdue(s) soit %.2f%% de gain", nb_games, nb_wins, nb_loses, (float)nb_wins / nb_games * 100);

}