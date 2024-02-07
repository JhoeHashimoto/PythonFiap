numeros = []
for i in range (0,10,1):
    numero = input('Digite o números: ')
    numeros.append(numero) #inclusao do numero na lista numeros

for i in range (9,-1,-1): #vai diminuindo de 1 em 1 -1
    print(numeros[i])
