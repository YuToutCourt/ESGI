/*****************************************************
* \file    ptrTableauDouble_2.h
* \author  Yohann MALEY
* \date    15 décembre 2022
* \brief   Contient les prototypes des fonctions du ptrTableauDouble_2
* \version 1.0
******************************************************/

#include <stdio.h>
#include <stdlib.h>

#ifndef PTRTABLEAUDOUBLE_2_H
#define PTRTABLEAUDOUBLE_2_H

/** @struct TableauDouble
 *  @brief Structure d'un tableau de double
 *  @var TableauDouble::a_tab
 *  Le tableau de double
 *  @var TableauDouble::a_taille
 *  La taille du tableau
 */
typedef struct {
    double* a_tab;
    unsigned int a_taille;
} TableauDouble;

/** @typedef PtrTableauDouble
 *  @brief Pointeur sur un tableau de double
 */
typedef TableauDouble* PtrTableauDouble2;

/**
 * @brief Construit un tableau de double
 * 
 * @param ptd  Le tableau de double
 * @param taille  La taille du tableau
 */
void TableauDouble_construire2(PtrTableauDouble2* ptd, int taille);


/**
 * @brief Affiche un tableau de double
 * 
 * @param ptd  Le tableau de double
 */
void TableauDouble_afficher2(PtrTableauDouble2 ptd);


/**
 * @brief Modifie un élément du tableau de double
 * 
 * @param ptd  Le tableau de double
 * @param index  L'index de l'élément à modifier
 * @param valeur  La nouvelle valeur de l'élément
 */
void TableauDouble_modifier2(PtrTableauDouble2 ptd, int index, double valeur);


/**
 * @brief Récupère un élément du tableau de double
 * 
 * @param ptd  Le tableau de double
 * @param index  L'index de l'élément à récupérer
 * @return double  La valeur de l'élément
 */
double TableauDouble_get2(PtrTableauDouble2 ptd, int index);

/**
 * @brief Libère un tableau de double
 * 
 * @param ptd  Le tableau de double
 */
void TableauDouble_liberer2(PtrTableauDouble2* ptd);


/**
 * @brief Exemple d'utilisation
 * 
 * @return int  0
 */
int C_2();

#endif // PTRTABLEAUDOUBLE_2_H