p1 = float(input("Digite a nota da Prova 1: "))
media_aprovacao= 5.0
p2 = (15 - p1) / 2

if (p2 <= 10.0):
    print(f"Você deverá tirar {p2} na p2, para ser aprovado")

else:
    print(f"Reprovado!s")