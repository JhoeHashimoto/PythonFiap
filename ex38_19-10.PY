soma = 0
qtd_pos = 0
qtd_neg = 0
exec = 's'
historico = ''

while (exec.upper() == "S"):
    qtd = int(input('Digite a quantidade de valores que deseja digitar: '))


    while((qtd <= 0) or (qtd > 20)):
        print('Erro! Valor inválido, a quantidade deve estar entre 1 e 20!')
        qtd = int(input('Digite a quantidade de valores que deseja digitar: '))


    for i in range(1, qtd+1, 1):
        num = int(input(f'Digite o {i}° número: '))


        if (i == 1):
            maior = num
            menor = num


        if (num > maior):
            maior = num
   
        if (num < menor):
            menor = num


        if (num >= 0):
            qtd_pos = qtd_pos + 1
        else:
            qtd_neg = qtd_neg + 1
   
        soma = soma + num


    media = soma / qtd


    por_pos = (qtd_pos * 100) / qtd
    por_neg = (qtd_neg * 100) / qtd


    print(f'O maior número é: {maior}')
    print(f'O menor número é: {menor}')
    print(f'A soma dos valores é: {soma}')
    print(f'A média é: {media:.1f}')
    print(f'O percentual de positivos é: {por_pos:.2f}%')
    print(f'O percentual de negativos é: {por_neg:.2f}%')


    
    print('----------------------')
    
    exec= input('Deseja calcular novamente? \n Digite (S/N): ')
    if (exec != 's' .upper):
        input('Pressione Enter...')
