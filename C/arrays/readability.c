#include <stdio.h>
#include <conio.h>
#include <ctype.h>

int main()
{
    char texto[10000] = "";
    int letras;
    int frases;
    float L = 0;
    float F = 0;
    float palavras;
    float indice;
    
    printf("Digite seu texto:");
    gets(texto);
    
    
    for (int i = 0; i < 10000; i++)
    {
        if (isalpha(texto[i])) {
            letras++;
        }
        
        if (isspace(texto[i])) {
            palavras++;
        }
        
        if (texto[i] == '.' || texto[i] == '!' || texto[i] == '?') {
            frases++;
        }
    }
    
    L = letras / (palavras+1) * 100;
    F = frases / (palavras+1) * 100;
    indice = 0.0588 * L - 0.296 * F - 15.8;
    

    printf("\nLetras: %d", letras);
    printf("\nFrases: %d", frases);
    printf("\nPalavras: %.f", palavras+1);
    printf("\nIndice: %.f", indice);

    return 0;
}