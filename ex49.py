matriz = [ ['','',''], ['','',''] ]


for l in range(0, 2, 1):
    for c in range(0, 3, 1):
        matriz[l][c] = input('Digite um nome: ')


# Mostra a matriz de forma real
for i in range(0, 2, 1):
    print(matriz[i])
