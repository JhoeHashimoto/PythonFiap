x = int(input('Digite o numero da tabuada:'))

while(x<=0):
    print('Erro!')
    x=int(input('Digite o numero novamente:'))

a= int(input('Digite o valor inicial do intervalo:'))
b= int(input('Digite o valor final do intervalo'))

while(b<=a):
    print('Erro')
    b = int(input('Digite novamente o valor do ultimo intervalo, devendo ser positivo e maior que zero'))

for i in range(b, a-1, -1):
    tabuada = x * i
    print(f'{x} X {i} = {tabuada}')

