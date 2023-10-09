
altura = int(input("Digite a altura do muro: "))

for linha in range(altura):
    
    for espaco1 in range(altura - 1):
        print(" ", end="")
    
    for coluna1 in range(linha + 1):
        print("#", end="")
        
    for espaco2 in range(1):
        print("  ", end="")
    
    for coluna2 in range(linha + 1):
        print("#", end="")
        
    print()
    altura -= 1