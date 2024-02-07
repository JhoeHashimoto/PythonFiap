n = int(input("digite o valor de n: "))


while (n <= 0) or (n > 50):
    print("O valor deve ser positivo e menor que 50")
    n = int(input("digite n novamente: "))


a = 2
b = 1
c = 1
soma = 0.0


for i in range(1, n+1, 1):
    print(f'{a} / {b}')


    soma = soma + (a/b)


    c = c + 2
    a = a + c
   
    b = ((i+1) * (i+1) * (i+1))


print(f'A soma da sequência é: {soma:.2f}')