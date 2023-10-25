#include <stdio.h>

int main()
{
    int count = 0;
    int altura;
    
    while (altura < 1 || altura > 8)
    {
        printf("Digite altura do muro:");
        scanf("%d", &altura);
    }
    
    for (int i = 1; i <= altura; i++) 
    {
        printf("\n");
        count++;
        
        for (int z = 7; z >= count; z--)
        {
            printf(" ");
        }
        
        for (int y = 1; y <= count; y++)
        {
            printf("#");
        }
        
        printf("  ");
        
        for (int y = 1; y <= count; y++)
        {
            printf("#");
        }
    }
    

    return 0;
}