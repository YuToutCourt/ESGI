/*****************************************************
* \file    livre.h
* \author  Yohann MALEY
* \date    15 décembre 2022
* \brief   Contient les prototypes des fonctions du livre
* \version 1.0
******************************************************/

#include <stdio.h>
#include <stdlib.h>

#ifndef LIVRE_H
#define LIVRE_H

/** @struct Livre
 *  @brief Structure Livre
 *  @var Livre::nom
 *  Member 'nom' contient le nom du livre
 *  @var Livre::auteur
 *  Member 'auteur' contient le nom de l'auteur du livre
 *  @var Livre::editeur
 *  Member 'editeur' contient le nom de l'éditeur du livre
 *  @var Livre::code_barre
 *  Member 'code_barre' contient le code barre du livre
 */
typedef struct {
    char *nom;
    char *auteur;
    char *editeur;
    char code_barre[13];
} Livre;

/** @brief Crée un livre
 *  @param livre Pointeur vers le livre à créer
 *  @param nom Nom du livre
 *  @param auteur Auteur du livre
 *  @param editeur Editeur du livre
 *  @param code_barre Code barre du livre
 *  @return void
 */
void Livre_creer(Livre *livre, char *nom, char *auteur, char *editeur, char *code_barre);


/** @brief Modifie un attribut d'un livre
 *  @param livre Pointeur vers le livre à modifier
 *  @param attribut Attribut à modifier
 *  @param valeur Valeur à attribuer à l'attribut
 *  @return void
 */
void Livre_set(Livre *livre, char *attribut, char *valeur);


/** @brief Récupère la valeur d'un attribut d'un livre
 *  @param livre Pointeur vers le livre à modifier
 *  @param attribut Attribut à modifier
 *  @return char* Valeur de l'attribut
 */
char *Livre_get(Livre *livre, char *attribut);


/** @brief Affiche un livre
 *  @param livre Pointeur vers le livre à afficher
 *  @return void
 */
void Livre_afficher(Livre *livre);

/**
 * @brief Exemple d'utilisation
 * 
 * @return int  0
 */
int C_3();

#endif /*LIVRE_H*/