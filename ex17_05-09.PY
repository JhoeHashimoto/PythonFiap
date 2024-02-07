peso = float(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura:"))
sexo = input("Digite o seu sexo (M/F):")

imc = peso / altura * altura

if (sexo.upper() == "F") :                ##.upper tudo maiusculo .lower tudo minúsculo
    if (imc < 19):
        print("Você esta abaixo do peso")
    elif ((imc >= 19) and (imc <=24 )):
        print("Você esta dentro do peso")

    else:
        print("Você esta acima do pes!o")

elif (sexo.upper() == "M"):
    if (imc < 20):
        print("Você está abaixo do peso")
    elif ((imc >= 20)) and ((imc <=25)):
        print("Você esta dentro do peso!")
    else:
        print("Voce esta acima do peso")

else:
    print("Sexo Inválido")