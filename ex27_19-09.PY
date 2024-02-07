num = int(input("Digite um número para obter sua tabuada: "))

while(num<=0):
    print('Erro! Digite apenas valores positivos!')
    num = int(input("Digite um número para obter sua tabuada: "))


while (i<=10):
    r = num * 1
    print(f"{num} X {i} {r}")

    i = i+1
