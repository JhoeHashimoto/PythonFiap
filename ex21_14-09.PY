v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

print("MENU")
print("1 - MULTIPLICAÇÃO")
print("2 - ADIÇÃO")
print("3 - DIVISÃO")
print("4 - SUBTRAÇÃO")
print("5 - FIM DE PROCESSO (sair do programa)")

opcao=int(input("Escolha uma opção acima: "))

if opcao == 1:
    MULTIPLICAÇÃO = v1 * v2
    print({MULTIPLICAÇÃO})

elif opcao == 2:
    ADIÇÃO = v1 + v2
    print({ADIÇÃO})

elif opcao == 3:
    DIVISÃO = v1 / v2
    print({DIVISÃO})

elif opcao == 4:
    SUBTRAÇÃO = v1 - v2
    print({SUBTRAÇÃO})

elif opcao == 5:
    print("ENCERRANDO PROGRAMA")
