/***********************************************************************
* \file    TP2.h
* \author  Yohann MALEY
* \date    29 octobre 2022
* \brief   Fichier qui contient des fonctions utiles pour le tp2 (dice)
* \version 1.0
************************************************************************/

#include "tp2.h"


bool in(short value, short array[], short size){
    for (int i = 0; i < size; i++){
        if (array[i] == value) return true;
    }
    return false;
}

bool all_in(short list[], short array[], short size){
    for (int i = 0; i < size; i++){
        if (!in(list[i], array, size)) return false;
    }
    return true;
}

short roll_dice(){
    short value = rand() % 6 + 1;
    return value;
}

void display_gotten_numbers(short list[], int size){
    printf("[");    
    for (short i = 0; i < size; i++){
        // Je n'ai pas compris pourquoi j'ai des 255 dans mon tableau. Problemes de mémoire ?
        if (list[i] == -1 || list[i] == 255) continue;
        if (i > 0) printf(", ");
        printf("%d", list[i]);
    }
    printf("]\n");
}

void keep(short list[], short size){
    printf("Je garde ");
    for(short i = 0; i < size; i++){
        // Je n'ai pas compris pourquoi j'ai des 255 dans mon tableau. Problemes de mémoire ?
        if(list[i] == -1 || list[i] == 255) continue;
        if (i > 0) printf("et ");
        printf("%d ", list[i]);
        
        
    }

}