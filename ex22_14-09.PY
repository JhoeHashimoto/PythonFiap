print("1 - TRIÂNGULO")
print("2 - QUADRADO")
print("3 - RETÂNGULO")
print("4 - CIRCULO")
print("5 - FIM DE PROCESSO")

opcao=int(input("Escolha uma opção acima: "))

b = float(input("Digite a base do poligono: "))
h = float(input("Digite a altura do poligono: "))

if (opcao == 1):
    TRIÂNGULO = b * h / 2
    print({TRIÂNGULO})
elif (opcao == 2):
    QUADRADO = b * h
    print({QUADRADO})
elif (opcao == 3):
    RETÂNGULO = b * h
    print({RETÂNGULO})
elif (opcao == 4):
    CIRCULO = 3.14 * (b * b / 2)
    print(f'A area do circulo é {CIRCULO}')
else:
    print("OPÇÃO INVALIDA")
