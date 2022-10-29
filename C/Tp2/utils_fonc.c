#include <stdio.h>
#include <time.h>

#include "tp2.h"


bool in(short value, short *array, short size){
    for (int i = 0; i < size; i++){
        if (array[i] == value) return true;
    }
    return false;
}


short index_(short value, short *list, short size){
    short i;
    for (i = 0; i < size; i++){
        if (list[i] == value){
            return i;
        }
    }
    return -1;
}

short random_value(){
    srand(time(NULL));  /* initialise le générateur pseudo aléatoire */
    short value = rand() % 6 + 1;
    return value;
}

void display_gotten_numbers(short *list, int size){
    printf("[");    
    for (short i = 0; i < size; i++){
        if (list[i] != -1){
            printf("%d", list[i]);
            if (i != size - 1) printf(", ");
        }
    }
    printf("]\n");
}

void keep(short list[], short size){
    printf("Je garde ");
    for(short i = 0; i < size; i++){
        if (list[i] != -1){
            printf("%d ", list[i]);
            if (i != size - 1) printf("et ");
        }
    }

}