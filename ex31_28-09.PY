
maior = 0
menor = 0
soma = 0
media=0

for i in range (1, 11, 1):
    n = int(input('Digite o número:'))
    while (n<=0):
        print(f'Erro! O número deve ser positivo')
        n = int(input('Digite novamente:'))

    if (i == 1):
        maior = n

    elif (n > maior):
        maior = n
        
    elif(i == 1):
        menor = n
    elif(n < menor):
        menor = n
    
    soma=soma+n
    media = soma / 10

print(f'O maior número é {n} ')
print(f'a soma é {soma}')
print(f'a media é {media}')
print(f'o menor número é {menor}')