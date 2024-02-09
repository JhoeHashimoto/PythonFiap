#51. Entrar via teclado com doze valores e armazená-los em uma matriz de ordem 3x4. 
#Após a digitação dos valores solicitar uma constante multiplicativa, 
#que deverá multiplicar cada valor matriz e armazenar o resultado em outra matriz de mesma ordem, 
#nas posições correspondentes. Exibir as matrizes na tela, sob a forma matricial, ou seja, linhas por colunas.


matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matriz2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    
for l in range(0,3,1):
    for c in range(0,4,1):
        matriz[l][c] = int(input(f"Digite um valor para a posição {l+1}x{c+1}:"))
    
for l in range(0,3,1):
    print(matriz[l])

const = int(input("Digite o valor de uma constante para a multiplicação dos elementos da matriz: "))

for l in range(0,3,1):
    for c in range(0,4,1):
        matriz2[l][c]= matriz[l][c] * const
#printa a matriz 1 multiplicada
        
    
print("Matriz 1")
for l in range(0,3,1):
    print(matriz[l])
    
print("***************************")

print("Matriz 2")
for l in range(0,3,1):
    print(matriz2[l])
