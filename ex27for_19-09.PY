num = int(input('Digite um numero positivo:'))

while(num<=0):
    print('Erro')
    num = int(input('Digite um numero positivo novamente:'))

for i in range (1,10,1):
    tabuada = num * i
    print(f'{num} X {i} = {tabuada}')