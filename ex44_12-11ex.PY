numeros = []
quantidade = int(input("Digite a quantidade de valores a serem adicionados na lista: "))

for i in range(0,quantidade, 1):
    if(quantidade<=20):
        num = int(input("Digite os valores da lista: "))
        numeros.append(num)
    else:
        print("Erro! A lista deve conter no máximo 20 valores: ")
        quantidade = int(input("Digite novamente os  valores: "))
        num = int(input("Digite os valores da lista: "))
        numeros.append(num)

while(True):
    print('Deseja consultar a lista? (S/N)')
    opcao = input("Digite (S ou N): ").upper()

    if (opcao == 'S'):
        x=int(input('Digite o valor a ser consultado: '))
        indice = numeros.index(x)
        while(x=False):
            print('Erro! Valor não encontrado: ')
            x=int(input('Digite o Valor a ser encontrado: '))
            print(numeros[x] + {indice})
    else:
        break

    

