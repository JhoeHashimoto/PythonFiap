v1 = float(input("Digite o primeiro valor:"))
v2 = float(input("Digite o segundo valor:"))
v3 = float(input("Digite o terceiro valor:"))

if ( ((v1 + v2 >= v3) and (v2 + v3 >= v1) and (v1 + v3 >= v2)) ):
  print("É um triangulo")

  if ((v1 != v2 ) and (v1 != v3 ) and (v2 != v3)):
    print("Escaleno")

  elif ((v1 == v2) and (v1 == v3) and (v2 == v3)):
    print("Equilátero")
  else:
    print("Isósceles")

else:
  print("Não é um triangulo")

  
    

