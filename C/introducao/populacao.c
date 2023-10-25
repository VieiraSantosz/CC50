#include <stdio.h>
#include <math.h>

int main(void) 
{
    int popInicial;
    int popFinal;
    int populacao;
    int ganho;
    int perda;
    int count = 0;
      
    while (popInicial < 9)
    {
        printf("Digite o Tamanho Inicial da população: ");
        scanf("%i", &popInicial);
        populacao = popInicial;
    }
    
    while (popFinal < popInicial)
    {
        printf("\nDigite o Tamanho Final da população: ");
        scanf("%i", &popFinal);
    }
    
    
    for (int i = 0; populacao < popFinal; i++)
    {
        ganho = populacao / 3;
        perda = populacao / 4;
        populacao = populacao + (ganho - perda);
        count++;
    }
    
    printf("\nPopulação Inicial: %i", popInicial);
    printf("\nPopulação Final: %i", popFinal);
    printf("\nPopulação: %i", populacao);
    printf("\nAnos: %i", count);
}