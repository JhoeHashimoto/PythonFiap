p1 = float(input("Digite a nota da P1"))
p2 = float(input("Digite a nota da p2"))

m = (p1 + p2) / 2 

if(m>= 5):
    print(f"Sua média foi {m:.2f} e você está aprovado!")

elif (m>= 3 ):
    print(f"Voce esta de recuperação!")

else:
    print("Reprovado")
    
print("Fim do programa")