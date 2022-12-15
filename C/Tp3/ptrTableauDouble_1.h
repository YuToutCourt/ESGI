/*****************************************************
* \file    ptrTableauDouble_1.h
* \author  Yohann MALEY
* \date    15 décembre 2022
* \brief   Contient les prototypes des fonctions du ptrTableauDouble_1
* \version 1.0
******************************************************/

#include <stdio.h>
#include <stdlib.h>

#ifndef PTRTABLEAUDOUBLE_1_H
#define PTRTABLEAUDOUBLE_1_H

/** @typedef PtrTableauDouble1
 *  @brief Un tableau de double
 */
typedef double* PtrTableauDouble1;

/**
 * @brief Construit un tableau de double
 * 
 * @param ptd  Le tableau de double
 * @param taille  La taille du tableau
 */
void TableauDouble_construire(PtrTableauDouble1* ptd, int taille);


/**
 * @brief Affiche un tableau de double
 * 
 * @param ptd  Le tableau de double
 * @param taille  La taille du tableau
 */
void TableauDouble_afficher(PtrTableauDouble1 ptd, int taille);


/**
 * @brief Modifie un élément du tableau de double
 * 
 * @param ptd  Le tableau de double
 * @param taille  La taille du tableau
 * @param index  L'index de l'élément à modifier
 * @param valeur  La nouvelle valeur de l'élément
 */
void TableauDouble_modifier(PtrTableauDouble1 ptd, int taille, int index, double valeur);


/**
 * @brief Récupère un élément du tableau de double
 * 
 * @param ptd  Le tableau de double
 * @param taille  La taille du tableau
 * @param index  L'index de l'élément à récupérer
 * @return double  La valeur de l'élément
 */
double TableauDouble_get(PtrTableauDouble1 ptd, int taille, int index);


/**
 * @brief Libère la mémoire un tableau de double
 * 
 * @param ptd  Le tableau de double
 */
void TableauDouble_liberer(PtrTableauDouble1* ptd);


/**
 * @brief Exemple d'utilisation
 * 
 * @return int  0
 */
int C_1();


#endif // PTRTABLEAUDOUBLE_1_H