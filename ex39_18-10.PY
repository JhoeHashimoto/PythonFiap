num = int(input('Digite um número para obter o seu fatorial: '))


while (num < 0):
    print('Erro! Digite apenas números positivos!')
    num = int(input('Digite um número para obter o seu fatorial: '))


if (num == 0) or (num == 1):
    fat = 1
else:
    fat = num
    while (num > 1):
        fat = fat * (num-1)
        num = num - 1


print(f'O fatorial é: {fat}')

