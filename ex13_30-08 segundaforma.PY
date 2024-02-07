v1 = float(input("Digite o primeiro valor:"))
v2 = float(input("Digite o segundo valor:"))
v3 = float(input("Digite o terceiro valor:"))

if ( (v1 > v2)) and ( (v1 > v3)):
    print("O v1 é o maior!")
elif ( (v2 > v1)) and ( (v2 > v3) ):
    print("O v2 é o maior")
else :
    print("O v3 é o maior")