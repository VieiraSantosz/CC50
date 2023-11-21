
moeda25 = 0
moeda10 = 0
moeda5  = 0
moeda1  = 0


reais = float(input("Digite o seu valor:"))

while reais < 0:
    reais = float(input("Digite o seu valor:"))
    
centavos = round(reais * 100)


if centavos >= 25:
    for i in range(centavos // 25):
        centavos    -= 25
        moeda25     += 1
        
if centavos >= 10:
    for i in range(centavos // 10):
        centavos    -= 10
        moeda10     += 1
        
if centavos >= 5:
    for i in range(centavos // 5):
        centavos    -= 5
        moeda5      += 1
        
if centavos >= 1:
    for i in range(centavos // 1):
        centavos    -= 1
        moeda1      += 1

total = moeda25 + moeda10 + moeda5 + moeda1


print("\nMoeda de 25     - ", moeda25)
print("Moeda de 10     - ", moeda10)
print("Moeda de 5      - ", moeda5)
print("Moeda de 1      - ", moeda1)
print("Total de Moedas - ", total)
    
