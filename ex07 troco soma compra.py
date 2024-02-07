a = float(input('Digite o valor do produto 1: '))
b = float(input('Digite o valor do produto 2: '))
c = float(input('Digite o valor do produto 3: '))
d = float(input('Digite o valor do produto 4: '))
e = float(input('Digite o valor do produto 5: '))

Total_compra = a + b + c + d + e 

Valor_Pago = float(input('Digite o Valor a ser Entregue: '))

Troco = Valor_Pago - Total_compra

print(f'O troco da compra é R${Troco:1f}')