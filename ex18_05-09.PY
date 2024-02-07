a = float(input("Digite o valor da aceleração em (m/s): "))
vo = float(input("Digite o valor da velocidade inicial em (m/s): "))
t = float(input("Digite o valor do tempo em s: "))

v = (vo + (a * t)) * 3.6

if (v <= 40) :
    print("Veiculo muito lento")
elif (v <= 60):
    print("Velocidade permitida")
elif (v <= 80):
    print("Velocidade de cruzeiro")
elif (v <= 120):
    print("Veiculo rapido")
else:
    print("Veiculo muito rapido")