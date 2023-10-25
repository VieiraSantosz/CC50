#include <stdio.h>
#include <math.h>

int main()
{

    float reais;
    int centavos;
    int count = 0;
    
    int cent25 = 25;
    int moeda25 = 0;
    
    int cent10 = 10;
    int moeda10 = 0;
    
    int cent5 = 5;
    int moeda5 = 0;
    
    int cent1 = 1;
    int moeda1 = 0;
    
    
    printf("Digite o Valor: ");
    scanf("%f", &reais);

    centavos = round(reais * 100);
    
    if (centavos >= 25) {
        for (int i = 0; cent25 <= centavos; i++)
        {
            centavos = centavos - cent25;
            moeda25++;
        }  
    }
        
    if (centavos >= 10) {
        for (int i = 0; cent10 <= centavos; i++)
        {
            centavos = centavos - cent10;
            moeda10++; 
        }
    }
    
    if (centavos >= 5) {
        for (int i = 0; cent5 <= centavos; i++)
        {
            centavos = centavos - cent5;
            moeda5++; 
        }
    }
        
    if (centavos >= 1) {
        for (int i = 0; cent1 <= centavos; i++)
        {
            centavos = centavos - cent1;
            moeda1++; 
        }
    }
    
    printf("\nMoeda de 25 - %i", moeda25);
    printf("\nMoeda de 10 - %i", moeda10);
    printf("\nMoeda de 5 - %i", moeda5);
    printf("\nMoeda de 1 - %i", moeda1);
    

    return 0;
}