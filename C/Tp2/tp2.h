/*****************************************************
* \file    TP2.h
* \author  Yohann MALEY
* \date    29 octobre 2022
* \brief   Contient les prototypes des fonctions du tp2
* \version 1.0
******************************************************/

#include <stdbool.h>
#ifndef TP2_H
#define TP2_H


/* prototype des fonctions de tp2.c */

void equation_second_degre();
void suite();
unsigned long long int fibonacci();
void nombre_or_fibo();
void dice();


/* prototype des fonctions de utils_fonc.c */

extern bool in(short value, short *array, short size);
extern short index_(short value, short *list, short size);
extern short random_value();
extern void display_gotten_numbers(short *list, int size);
extern void keep(short list[], short size);



#endif /* TP2_H */