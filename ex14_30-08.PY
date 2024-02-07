p = float(input("Digite o peso da pessoa:"))
h = float(input("Digite a altura da pessoa:"))

imc = p / h * h

if (imc < 20) :
    print("Abaixo do peso!")

elif imc < 25 :
    print("Acima do peso!")

else :
    print("Peso ideal!")
