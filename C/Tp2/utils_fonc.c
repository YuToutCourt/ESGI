#include <stdio.h>
#include <time.h>

#include "tp2.h"


bool in(short value, short *array, short size){
    for (int i = 0; i < size; i++){
        if (array[i] == value) return true;
    }
    return false;
}

bool all_in(short *list, short *array, short size){
    for (int i = 0; i < size; i++){
        if (!in(list[i], array, size)) return false;
    }
    return true;
}

short roll_dice(){
    short value = rand() % 6 + 1;
    return value;
}

void display_gotten_numbers(short *list, int size){
    printf("[");    
    for (short i = 0; i < size; i++){
        if (list[i] != -1){
            printf("%d", list[i]);
            if (i < size - 2) printf(", ");
        }
    }
    printf("]\n");
}

void keep(short list[], short size){
    printf("Je garde ");
    for(short i = 0; i < size; i++){
        if (list[i] != -1){
            printf("%d ", list[i]);
            if (i < size - 2) printf("et ");
        }
    }

}