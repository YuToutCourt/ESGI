

void equation_second_degre(){
    float a, b, c;
    float delta;
    float x1, x2;

    printf("Entrez les coefficients a, b et c de l equation ax^2 + bx + c = 0 : \n");
    scanf("%f %f %f", &a, &b, &c);

    delta = b*b - 4*a*c;

    if (delta < 0) printf("Pas de solution dans R\n");

    else if (delta == 0){
        x1 = -b / (2*a);
        printf("Une solution : x = %.2f\n", x1);

    } else {
        x1 = (-b - sqrt(delta)) / (2*a);
        x2 = (-b + sqrt(delta)) / (2*a);
        printf("Deux solutions : x1 = %.2f et x2 = %.2f\n", x1, x2);
    }
}


void suite(){
    int n;
    float u0 = 2;
    float un, un1;

    printf("Entrez la valeur de n : ");
    scanf("%d", &n);

    for (int i = 0; i < n-1; i++){
        un1 = 0.5 * (u0 + 2/u0);
        u0 = un1;
        if (i % 10 == 0) printf("U%d = %.2f\n", i, u0);
    }
    un1 = 0.5 * (u0 + 2/u0);
    u0 = un1;
    printf("Le resultat de U[%d] est : %.2f\n", n, u0);
}

unsigned long long int fibonacci(){

    unsigned long long int n;
    printf("Entrez la valeur de n : ");
    scanf("%d", &n);
    unsigned long long int val = n;
    unsigned long long int first = 0, second = 1;
    unsigned long long int tmp;

    while (n--) {
        tmp = first + second;
        first = second;
        second = tmp;
    }
    printf("Fibonacci de %d est %d : F[%d] = %d\n", val, first, val, first);
    return first;
}

void nombre_or_fibo(){

    int n;
    printf("Entrez la valeur de n : "); 
    scanf("%d", &n);

    for(int i = 1; i <= n; i++){
        if (i % 5 == 0) printf("O[%d] = %f\n", i, fibonacci(i+1)/fibonacci(i));
    }

    printf("Le resultat de O[%d] est %f\n", n, fibonacci(n+1)/fibonacci(n));
    printf("Le nombre d'or est egal a : %f\n", fibonacci(n+1)/fibonacci(n));

}