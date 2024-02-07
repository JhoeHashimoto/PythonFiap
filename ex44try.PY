pessoas = []

while True:
    n = int(input('Digite a quantidade de valores a serem armazenados: '))
    if n >= 20 or n < 1:
        print("Erro!")
        print("A quantidade de valores deve ser menor que 20 e positiva! ")
    else:
        break

for i in range(n):
    valor = int(input("Digite o número: "))
    pessoas.append(valor)

while True:
    continuar = input("Gostaria de fazer uma nova consulta? Digite (S/N)").upper()
    if continuar != 'S':
        break
    else:
        consulta = int(input("Digite o valor para saber a posição: "))
        if consulta in pessoas:
            print(f'Valor encontrado na posição {pessoas.index(consulta)} da lista.')
        else:
            print("Valor não encontrado!")
