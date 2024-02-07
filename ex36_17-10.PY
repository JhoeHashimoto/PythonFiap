n = int(input("digite o valor de n: "))


while (n <= 0) or (n > 50):
    print("O valor deve ser positivo e menor que 50")
    n = int(input("digite n novamente: "))


a = 1
b = 2
soma = 0.0


for i in range(1, n+1, 1):
    print(f'{a} / {b}')
    a += 1
    b += 1
    soma = soma + a/b


print(f'A soma da sequência é: {soma:.2f}')
