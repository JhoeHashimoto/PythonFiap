valores = []


for i in range (0,5,1):
    x = int(input('Digite o valor x:'))
    valores.append(x) ##adição de x numeros na lista e populando

constante=int(input('Digite uma constante multiplicativa: '))

for i in range (0,5,1):
    valores[i] = constante * valores[i]
    print(valores[i])
 