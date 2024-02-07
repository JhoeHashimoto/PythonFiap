continuar = 's'


while(continuar == 's'):
   qtd = int(input('Digite a quantidade de valores à serem digitados: '))


   while((qtd <= 0) or (qtd > 20)):
       print('Quantidade inválida! Favor escolher entre 1 e 20.')
       qtd = int(input('Digite a quantidade de valores à serem digitados: '))


   maior_valor = 0
   menor_valor = 0
   zeros = 0
   soma = 0
   num_pos = 0
   num_neg = 0


   for i in range(1, qtd+1, 1):
       numero = int(input(f'Digite o numero {i}: '))


       soma = soma + numero


       if (numero > 0):
           num_pos = num_pos + 1
       elif (numero < 0):
           num_neg = num_neg + 1
       else:
           zeros = zeros + 1


       if (i == 1):
           maior_valor = numero
           menor_valor = numero
       else:
           if (numero > maior_valor):
               maior_valor = numero


           if (numero < menor_valor):
               menor_valor = numero


   print(f'O maior valor é: {maior_valor}')
   print(f'O menor valor é: {menor_valor}')
   print(f'A soma dos números é: {soma}')
   print(f'A quantidade de números zeros: {zeros}')


   media = soma / qtd
   print(f'A média aritmética é: {media:.2f}')


   por_num_pos = (num_pos / qtd) * 100
   print(f'Porcentagem dos valores positivos: {por_num_pos}%')


   por_num_neg = (num_neg / qtd) * 100
   print(f'Porcetagem dos valores negativos: {por_num_neg}%')


   continuar = input('Deseja realizar uma nova execução? (s/n): ')
   while((continuar != 's') and (continuar != 'n')):
       print('Opção inválida! Apenas digite s ou n!')
       continuar = input('Deseja realizar uma nova execução? (s/n): ')
