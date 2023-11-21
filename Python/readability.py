
texto = input("Digite seu texto:")
    
letras   = 0
palavras = 0
frases   = 0
L = 0
F = 0

for caractere in texto:
    
    if caractere.isalpha():
        letras += 1
        
    if caractere.isspace():
        palavras += 1
            
    if caractere == '.' or caractere == '!' or caractere == '?':
        frases += 1
    
    L = letras / (palavras+1) * 100
    F = frases / (palavras+1) * 100
    indice = int(0.0588 * L - 0.296 * F - 15.8)
        
        
print("Quantidade de Letras   - ", letras)
print("Quantidade de Palavras - ", palavras + 1)
print("Quantidade de Frases   - ", frases)

if indice < 0:
    print("Índice menor que 1")
elif indice > 16:
    print("Índice maior que 16")
else:
    print("Índice                 - ", indice)
    