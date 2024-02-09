##52. Entrar com uma matriz de ordem LxC, 
#onde a ordem também será escolhida pelo usuário, sendo que no máximo 10x10. A matriz não precisa ser quadrática. 
#Após a digitação dos elementos, criar uma rotina de consulta, 
#onde o usuário digita um valor e a rotina exibe em qual (ou quais) posição da matriz, 
#o valor escolhido se encontra. Enviar mensagem comunicando se por acaso o valor não estiver armazenado na matriz. 
#Perguntar ao usuário, se deseja ou não fazer nova consulta.


matriz = [[]]

xl = int(input("Digite a quantidade de linhas que a matriz irá ter: "))
xc = int(input("Digite a quantidade de colunas que a matriz deverá ter: "))

if (xl and xc >=10):
    print("A quantidade de linhas e colunas deve ser menor que 10")
    xl = int(input("Digite a quantidade de linhas que a matriz irá ter: "))
    xc = int(input("Digite a quantidade de colunas que a matriz deverá ter: "))

#para a quantidde de linhas adicionadas adicione uma sublista
    
else:
    for i in range(0,xl,1):
        matriz.append([])

#para cada sublista"coluna" adicione 1 elemento
    for l in range(0, xl, 1):
        for c in range(0, xc, 1):
            matriz[xl][xc] = int(input("Digite um valor para a posição :"))

   