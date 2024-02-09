#carro = [["Modelo", "HRV"]
            #["Fabricante","HONDA"],
            #["Ano", "2016"]]
#print(carro[0][0])
#Modelo
#print(carro[0][1])
#HRV

#for l,c in carros:
    #print(l + c)

   # Modelo HRV
   # Fabricante Honda
   # Ano 2016

#alterar valor da matriz
    #carro[2][1]
    #2019

#adicionar outro elemento
#carro.append(["cor", "prata"])

matriz = [ [0,0,0], [0,0,0] ]


for l in range(0, 2, 1):
    for c in range(0, 3, 1):
        matriz[l][c] = int(input('Digite um numero: '))


# Mostra a matriz de forma real
for i in range(0, 2, 1):
    print(matriz[i])
