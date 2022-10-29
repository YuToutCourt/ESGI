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

/**
 * @brief Fonction qui permet de résoudre une équation du second degré
 */
void equation_second_degre();

/**
 * @brief Fonction qui permet de calculer la suite Rn 
 * 
 */
void suite();

/**
 * @brief Fonction qui permet de calculer Fibonacci
 * 
 * @return unsigned long long int 
 */
unsigned long long int fibonacci();

/**
 * @brief Fonction qui permet de calculer le nombre d'or de Fibonacci
 * 
 */
void nombre_or_fibo();

/**
 * @brief Fonction qui permet de jouer au 421
 * 
 */
void dice();


/* prototype des fonctions de utils_fonc.c */

/**
 * @brief Fonction qui permet de savoir si un nombre est dans un tableau
 * 
 * @param value 
 * @param array 
 * @param size 
 * @return true 
 * @return false 
 */
extern bool in(short value, short *array, short size);

/**
 * @brief Fonction qui permet de savoir si tous les nombres d'un tableau sont dans un autre tableau
 * 
 * @param list 
 * @param array 
 * @param size 
 * @return true 
 * @return false 
 */
extern bool all_in(short *list, short *array, short size);

/**
 * @brief Fonction qui permet de lancer un dé
 * 
 * @return short 
 */
extern short roll_dice();

/**
 * @brief Fonction qui permet d'afficher les nombres obtenus
 * 
 * @param list 
 * @param size 
 */
extern void display_gotten_numbers(short *list, int size);

/**
 * @brief Fonction qui permet d'afficher les nombres gardés
 * 
 * @param list 
 * @param size 
 */
extern void keep(short list[], short size);



#endif /* TP2_H */