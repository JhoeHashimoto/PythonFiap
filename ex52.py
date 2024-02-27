##52. Entrar com uma matriz de ordem LxC, 
#onde a ordem também será escolhida pelo usuário, sendo que no máximo 10x10. A matriz não precisa ser quadrática. 
#Após a digitação dos elementos, criar uma rotina de consulta, 
#onde o usuário digita um valor e a rotina exibe em qual (ou quais) posição da matriz, 
#o valor escolhido se encontra. Enviar mensagem comunicando se por acaso o valor não estiver armazenado na matriz. 
#Perguntar ao usuário, se deseja ou não fazer nova consulta.
matriz = [[]]


xl = int(input("Digite a quantidade de linhas que a matriz irá ter: "))
xc = int(input("Digite a quantidade de colunas que a matriz deverá ter: "))

if (xl>=10 or xc>=10):
    print("A quantidade de linhas e colunas deve ser menor que 10")
    xl = int(input("Digite a quantidade de linhas que a matriz irá ter: "))
    xc = int(input("Digite a quantidade de colunas que a matriz deverá ter: "))

#para a quantidde de linhas adicionadas adicione uma sublista
    
else:
    print("******************")
    print(f"Matriz [{xl}x{xc}]")
    print("******************")
    for i in range(0,xl,1):
        matriz.append([])

#para cada sublista"coluna" adicione 1 elemento
    for l in range(xl):
        for c in range(xc):
            valor = int(input(f"Digite um valor para a posição ({l+1}, {c+1}): "))
            matriz[l].append(valor)
    

    for l in range(0,xl,1):
        print(matriz[l])

    while True:
        resposta=input("Gostaria de consultar a posição do elemento? (S/N)").upper()

        if resposta == ('S'):

            valor_procurado = int(input("Digite o valor a ser retornado o indice: "))
            for l in range(xl):
                if valor_procurado in matriz[l]:
                    print(f'O valor {valor_procurado} está na posição ({l+1},{c+1}), ou seja na linha:{l+1} e coluna:{c+1}')
                    break
                else:
                    print("O valor não está disponível na lista, tente novamente:")
                    
        else:
            break