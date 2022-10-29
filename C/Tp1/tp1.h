/*****************************************************
* \file    tp1.h
* \author  Yohann MALEY
* \date    22 octobre 2022
* \brief   Contient les prototypes des fonctions du tp1
* \version 1.0
******************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846

#ifndef TP1_H
#define TP1_H

/* prototype des fonctions */

/**
 * @brief calcule la surface d'un pentagone
 * 
 * @return float 
 */
float surface_pentagone();

/**
 * @brief calcule la somme et multiplie entrer par l'utilisateur
 */
void somme_multiple();

/**
 * @brief affiche le plus grand nombre parmis les nombres entrer par l'utilisateur
 */
void the_greatest();

/**
 * @brief affiche la suite U(n) = U(n)-1 + 1
 */
void suite(); 

/**
 * @brief affiche la table ASCII de 33 à 127
 * 
 */
void table_ascii();

/**
 * @brief affiche un sapin de hauteur n et de caractère c
 * 
 * @param hauteur [in] hauteur du sapin
 * @param symbole [in] caractère du sapin
 */
void afficheTriangleSapin(const unsigned int hauteur, char symbole);

/**
 * @brief Affiche une matrice de taille n avec la moyenne de chaque ligne et de chaque colonne
 * 
 */
void tableau();


#endif /* TP1_H */