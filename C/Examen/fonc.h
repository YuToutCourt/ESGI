/***********************************************************************
/***********************************************************************
* \file    fonc.h
* \author  Yohann MALEY
* \date    10 mars 2023
* \brief   Fichier qui contient des fonctions a coder
* \version 1.0
************************************************************************/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

#ifndef FONC_H
#define FONC_H

/** @typedef ElementTableau
 *  @brief Un tableau de double
 */
typedef double ElementTableau;


/** @typedef Tableau
 *  @brief Un tableau de ElementTableau
 */
typedef ElementTableau *Tableau;

/**
 * @brif Enumération des types d'articles
*/
typedef enum {DIVERS, VETEMENT, NOURRITURE, LIVRE} Type;

/**
 * @brief Structure d'un article
*/
typedef struct {
    char a_nom[256];
    float a_prix;
    char a_description[1024];
    Type a_type;
} Article;


/**
 * @brief Fonction qui calcule la puissance d'un nombre
 * @param n Le nombre
 * @param e L'exposant
 * @return n^e
*/
int mypow(int n, int e);

/**
 * @brief Fonction qui calcule une suite
 * @param n Le nombre d'entiers à sommer
 * @return La somme des n premiers entiers
*/
double suite(double x, unsigned N);

/**
 * @brief Fonction qui permute deux éléments d'un tableau
 * @param a Un élément du tableau
 * @param b Un élément du tableau
*/
void permuter(ElementTableau *a, ElementTableau *b);

/**
 * @brief Fonction qui permute un tableau
 * @param tab Le tableau à permuter
 * @param size La taille du tableau
*/
void permuter_tableau(Tableau tab, unsigned size);

/**
 * @brief Fonction qui crée un tableau
 * @param size La taille du tableau
 * @return Le tableau
*/
Tableau creer_tableau(unsigned size);

/**
 * @brief Fonction qui libère un tableau
 * @param tab Le tableau à libérer
*/
void liberer_tableau(Tableau *tab);

/**
 * @brief Fonction qui affiche un tableau
 * @param tab Le tableau à afficher
 * @param size La taille du tableau
*/
void afficher_tableau(Tableau tab, unsigned size);

/**
 * @brief Fonction qui crée un article
 * @return L'article
*/
Article* creer_article();

/**
 * @brief Fonction qui affiche un article
 * @param article L'article à afficher
*/
void afficher_article(const Article *article);

/**
 * @brief Fonction qui modifie un article
 * @param article L'article à modifier
*/
void modifier_article(Article *article);

/**
 * @brief Fonction qui libère un article
 * @param article L'article à libérer
*/
void liberer_article(Article **article);

/**
 * @brief Fonction qui sauvegarde un article dans un fichier
 * @param article L'article à sauvegarder
 * @param nomFichier Le nom du fichier
*/
void save_articile(const Article *article, const char* nomFichier);

/**
 * @brief Fonction qui charge un article depuis un fichier
 * @param article L'article à charger
 * @param ficher Le fichier
*/
void load_article(Article *article, FILE *ficher);

/**
 * @brief Fonction qui fait des trucs la
 * @return 0
*/
int main_article();

#endif /* FONC_H */