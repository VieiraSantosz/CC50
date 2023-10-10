#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main()
{
    char nome1[50] = "";
    char nome2[50] = "";
    char palavra1[50] = "";
    char palavra2[50] = "";
    int pontos1 = 0;
    int pontos2 = 0;

    
    printf("Jogador 1: ");
    scanf("%s", nome1);
    
    printf("Jogador 2: ");
    scanf("%s", nome2);
    
    
    printf("\n%s, digite sua palavra - ", nome1);
    scanf("%s", palavra1);
    
    printf("%s, digite sua palavra - ", nome2);
    scanf("%s", palavra2);
    
    
    for(int i = 0; i < 50; i++) 
    {
        if(palavra1[i] == 'a' || palavra1[i] == 'e' || palavra1[i] == 'i' || palavra1[i] == 'l' 
        || palavra1[i] == 'n' || palavra1[i] == 'o' || palavra1[i] == 'r' ||  palavra1[i] =='s' 
        || palavra1[i] == 't' ||  palavra1[i] =='u') {
            pontos1++;
        }
        
        if(palavra2[i] == 'a' || palavra2[i] == 'e' || palavra2[i] == 'i' || palavra2[i] == 'l' 
        || palavra2[i] == 'n' || palavra2[i] == 'o' || palavra2[i] == 'r' || palavra2[i] == 's' 
        || palavra2[i] == 't' || palavra2[i] == 'u') {
            pontos2++;
        }
   
   
        if(palavra1[i] == 'd' || palavra1[i] == 'g') {
            pontos1 = pontos1 + 2;
        }
        
        if(palavra2[i] == 'd' || palavra2[i] == 'g') {
            pontos2 = pontos2 + 2;
        }
   
   
        if(palavra1[i] == 'b' || palavra1[i] == 'c' || palavra1[i] == 'm' || palavra1[i] == 'p') {
            pontos1 = pontos1 + 3;
        }
        
        if(palavra2[i] == 'b' || palavra2[i] == 'c' || palavra2[i] == 'm' || palavra2[i] == 'p') {
            pontos2 = pontos2 + 3;
        }
   
   
        if(palavra1[i] == 'f' || palavra1[i] == 'h' || palavra1[i] == 'v' || palavra1[i] == 'w' || palavra1[i] == 'y') {
            pontos1 = pontos1 + 4;
        }
        
        if(palavra2[i] == 'f' || palavra2[i] == 'h' || palavra2[i] == 'v' || palavra2[i] == 'w' || palavra2[i] == 'y') {
            pontos2 = pontos2 + 4;
        }
   
   
        if(palavra1[i] == 'k') {
            pontos1 = pontos1 + 5;
        }
        
        if(palavra2[i] == 'k') {
            pontos2 = pontos2 + 5;
        }
        
   
        if(palavra1[i] == 'j' || palavra1[i] == 'x') {
            pontos1 = pontos1 + 8;
        }
        
        if(palavra2[i] == 'j' || palavra2[i] == 'x') {
            pontos2 = pontos2 + 8;
        }
        
   
        if(palavra1[i] == 'q' || palavra1[i] == 'z') {
            pontos1 = pontos1 + 10;
        }
        
        if(palavra2[i] == 'q' || palavra2[i] == 'z') {
            pontos2 = pontos2 + 10;
        }
    }
    
    printf("\nPontuação do %s: %d", nome1, pontos1);
    printf("\nPontuação do %s: %d", nome2, pontos2);
    printf("\n\n");
    
    if (pontos1 > pontos2) {
        printf("Parabéns, Jogador 1, %s ganhou!!!", nome1);
    } else if (pontos2 > pontos1) {
        printf("Parabéns, Jogador 2, %s ganhou!!!", nome2);
    } else {
        printf("Empate!!!");
    }
    
}
