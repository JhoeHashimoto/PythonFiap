valores = []

for i in range (0,5,1):
    x = int(input('Digite o valor x:'))
    valores.append(x) ##adição de xnumeros na lista e populando

primeiro = valores[0]  #cria uma variavel com qualquer valor para servir de comparação
#atribui o maior valor ao indice 0 de inicio para servir de comparação
for x in valores:
    if (valores[i] > primeiro):
        m = valores[i]

print(f'O maior número é {primeiro}')