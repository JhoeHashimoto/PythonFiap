valores = []
valoresmultiplicacao = []



for i in range (0,5,1):
    n = int(input('Digite a quantidade de números: '))
    valores.append(n)

constante=int(input('Digite o valor da constante para realizar a multiplicação: '))

for i in range(0,5,1):
    valoresmultiplicacao.append(constante * valores[i])

print('Valores da primeira lista:')

for i in range(0,5,1):
    print(valores[i])

print('Valores segunda lista multiplicada: ')

for i in range(0,5,1):
    print(valoresmultiplicacao[i])