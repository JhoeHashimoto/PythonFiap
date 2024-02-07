s = input("Digite o sexo (F/M)")

while (s.upper() != "M") and (s.upper() != "F"):    
    print ("Erro! Digite apenas F ou M!")     #upper converte o valor para maiúsculo
    s = input("Digite o sexo (F/M): ")


print("Obrigado!")