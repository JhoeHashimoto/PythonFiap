x0 = 2
x1 = 5
x2 = 10
i=0
impar=1

soma = 0
n = int(input("Digite a a quantidade de números: "))

while (n<=0 or n>=100):
    print("Erro!")
    n = int(input("Digite novamente: "))

for i in range(n):
    i = i + 1
    impar =impar +2
    s = x2+impar
    print(s)
    x0=x1+impar
    x1=x2+impar
    x2=s+impar