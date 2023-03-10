/***********************************************************************
/***********************************************************************
* \file    TP2.h
* \author  Yohann MALEY
* \date    29 octobre 2022
* \brief   Fichier qui contient des fonctions utiles pour le tp2 (dice)
* \version 1.0
************************************************************************/

#include "fonc.h"

int mypow(int n, int e){
    int res = 1;
    for (int i = 0; i < e; i++) res *= n;
    return res;
}

double suite(double x, unsigned N){
    double U0 = x;
    for (short i = 1; i < N; i++)
        U0 += U0 + mypow(-1, i) * mypow(x, 2*i-1)/2*i+1;
    return U0;
}

void permuter(ElementTableau *a, ElementTableau *b){
    ElementTableau tmp = *a;
    *a = *b;
    *b = tmp;
}

void permuter_tableau(Tableau tab, unsigned size){
    for (int i = 0; i < size/2; i++)
        permuter(&tab[i], &tab[size-i-1]);
}

Tableau creer_tableau(unsigned size){
    Tableau tab = malloc(size * sizeof(ElementTableau));
    return tab;
}

void liberer_tableau(Tableau *tab){
    free(*tab);
    *tab = NULL;
}

void afficher_tableau(Tableau tab, unsigned size){
    for (int i = 0; i < size; i++)
        printf("%lf ", tab[i]);
    printf("\n");
}

Article* creer_article(){
    // Créer un article avec les valeurs par défaut
    Article *article = malloc(sizeof(Article));
    
    if (article == NULL) {
        printf("Erreur : impossible d'allouer la mémoire nécessaire pour créer un nouvel article.\n");
        return NULL;
    }
    strcpy(article->a_nom, "Article");
    article->a_prix = 0.0;
    strcpy(article->a_description, "DEFAULT");
    article->a_type = DIVERS;
    return article;
}

void afficher_article(const Article *article){
    printf("---Article---\n");
    printf("Nom : %s\n", article->a_nom);
    printf("Prix : %f\n", article->a_prix);
    printf("Description : %s\n", article->a_description);
    printf("Type : %d\n", article->a_type);
    printf("-------------\n");
}

void modifier_article(Article *article){
    printf("\nEntrez le nouveau nom : ");
    scanf("%s", article->a_nom);
    printf("\nEntrez le nouveau prix : ");
    scanf("%f", &article->a_prix);
    printf("\nEntrez la nouvelle description : ");
    scanf("%s", article->a_description);
    printf("\nEntrez le nouveau type : ");
    scanf("%d", &article->a_type);
}

void liberer_article(Article **article){
    free(*article);
    *article = NULL;
}

void save_article(const Article *article, const char* nomFichier){
    FILE *f = fopen(nomFichier, "w");
    if (f == NULL){
        printf("Erreur lors de l'ouverture du fichier %s\n", nomFichier);
        return;
    }
    fprintf(f, "%s\n", article->a_nom);
    fprintf(f, "%f\n", article->a_prix);
    fprintf(f, "%s\n", article->a_description);
    fprintf(f, "%d\n", article->a_type);
    fclose(f);
}

void load_article(Article *article, FILE *ficher){
    printf("Chargement des articles depuis le fichier\n");
    fscanf(ficher, "%s", article->a_nom);
    fscanf(ficher, "%f", &article->a_prix);
    fscanf(ficher, "%s", article->a_description);
    fscanf(ficher, "%d", &article->a_type);
}

int main_article() {
    Article *a = creer_article();
    if (a == NULL) {
        printf("Erreur lors de la création de l'article.\n");
        return 1;
    }
    afficher_article(a);
    modifier_article(a);
    afficher_article(a);
    save_article(a, "article.txt");
    liberer_article(&a);

    FILE *f = fopen("article.txt", "r");
    if (f == NULL) {
        printf("Erreur lors de l'ouverture du fichier %s.\n", "article.txt");
        return 1;
    }
    Article *b = malloc(sizeof(Article));
    if (b == NULL) {
        printf("Erreur : impossible d'allouer la mémoire nécessaire pour charger l'article.\n");
        return 1;
    }
    load_article(b, f);
    afficher_article(b);
    liberer_article(&b);
    fclose(f);

    return 0;
}