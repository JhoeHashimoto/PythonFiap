matriz = []


linhas = int(input('Digite a quantidade de linhas da matriz: '))
while ((linhas < 0) or (linhas > 10)):
    print('Erro! A quantidade de linhas deve ser positiva e no máximo 10!')
    linhas = int(input('Digite a quantidade de linhas da matriz: '))


colunas = int(input('Digite a quantidade de colunas da matriz: '))
while ((colunas < 0) or (colunas > 10)):
    print('Erro! A quantidade de colunas deve ser positiva e no máximo 10!')
    colunas = int(input('Digite a quantidade de linhas da matriz: '))


for i in range(0, linhas, 1):
    matriz.append([])


for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):
        num = int(input(f'Digite um número para a posição [{l+1}, {c+1}] da matriz: '))
        matriz[l].append(num)


while(True):
    num_con = int(input('Digite um número para ser consultado na matriz: '))
    lista_consulta = []


    for i in range(0, linhas, 1):
        if (num_con in matriz[i]):
            lista_consulta.append([i+1, matriz[i].index(num_con)+1])


    if (len(lista_consulta) > 0):
        print(f'O número {num_con} está presente nas seguintes posições da matriz:')
        for c in lista_consulta:
            print(c)
    else:
        print(f'O número {num_con} não existe na matriz!')
   
    continuar = input('Deseja realizar uma nova consulta (s/n): ')


    if (continuar == 'n'):
        break
