b = float(input("Digite o valor da base do retângulo:"))
h = float(input("Digite o valor da altura do retângulo:"))
area = b * h

print(f"A area do retângulo é: {area}")

if area >= 100 :
    print("Terreno grande!")

else:
    print(f"{area: .1f}")