/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX 9

typedef struct
{
    char name[10];
    int votes;
}
candidate;

candidate candidatos[MAX];

bool vote(char name[10]);
void print_winner(void);


int main()
{
    
    int eleitores;
    int voto;
    
    
    printf("Digite a quantidade de eleitores: ");
    scanf("%i", &eleitores);
    
    printf("\nCandidatos:");
    printf("\n1. Alice \n2. Bob \n3. Charlie\n\n");
    
    
    for(int i = 0; i < eleitores; i++) {
        printf("Eleitor %i, escreva o nome do seu candidato: ", i+1);
        scanf("%s", candidatos[i].name);
        
        vote(candidatos[i].name);
    }
    
    print_winner();
    
}


bool vote(char name[10])
{
    
    if(strcmp(name, "Alice") == 0) {
        candidatos[0].votes++;
    }
        
    if(strcmp(name, "Bob") == 0) {
        candidatos[1].votes++;
    }
        
    if(strcmp(name, "Charlie") == 0) {
        candidatos[2].votes++;
    }
}

void print_winner(void)
{
    printf("\n\nTodos os Votos:");
    printf("\n1. Alice.. - %i", candidatos[0].votes);
    printf("\n2. Bob.... - %i", candidatos[1].votes);
    printf("\n3. Charlie - %i", candidatos[2].votes);
 
    if (candidatos[0].votes > candidatos[1].votes && candidatos[0].votes > candidatos[2].votes) {
        printf ("\n\nAlice ganhou a eleição!");
    }
    
    if (candidatos[1].votes > candidatos[0].votes && candidatos[1].votes > candidatos[2].votes) {
        printf ("\n\nBob ganhou a eleição!");
    }
    
    if (candidatos[2].votes > candidatos[1].votes && candidatos[2].votes > candidatos[0].votes) {
        printf ("\n\nCharlie ganhou a eleição!");
    }
    
    if (candidatos[0].votes == candidatos[1].votes || candidatos[0].votes == candidatos[2].votes) {
        printf ("\n\nEmpate!");
    }
}
