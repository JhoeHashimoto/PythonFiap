"""53. Vamos fazer uma excursão para Santos (Charlie Brown Jr). 
Para isto, vamos de ônibus, e precisaremos controlar as reservas de lugares do ônibus. 
Sabe-se que o ônibus possui quatro fileiras de dez cadeiras cada. 
Fazer um programa para solicitar o nome do usuário e o lugar que pretende reservar (fileira e cadeira), 
e se este lugar estiver disponível o programa deverá concretizar a reserva, caso contrário, 
enviar mensagem comunicando que esta poltrona já está ocupada. 
Perguntar se existe mais alguém que queira viajar para a Baixada, e em caso negativo exibir um “mapa” mostrando os nomes e lugares de cada passageiro que efetuou a reserva, assim como os lugares que permaneceram livres. 
Lembre-se que o ônibus possui uma capacidade limitada de poltronas e que o programa deverá encerrar estas reservas, caso esta capacidade tenha sido alcançada.
"""

onibus = [
    ['v', 'v', 'v', 'v'],
    ['v', 'v', 'v', 'v'],
    ['v', 'v', 'v', 'v'],
    ['v', 'v', 'v', 'v'],
    ['v', 'v', 'v', 'v'],
    ['v', 'v', 'v', 'v'],
    ['v', 'v', 'v', 'v'],
    ['v', 'v', 'v', 'v'],
    ['v', 'v', 'v', 'v'],
    ['v', 'v', 'v', 'v']
]


qtd = 0


while (True):
    fileira = int(input('Digite a fileira que deseja sentar (1 a 10): ')) -1
    cadeira = int(input('Digite a cadeira que deseja sentar (1 a 4): ')) -1


    if (onibus[fileira][cadeira] == 'v'):
        onibus[fileira][cadeira] = input('Digite o seu nome para reserva: ')
        qtd = qtd + 1
    else:
        print('Fileira/Cadeira já reservada, por favor, escolha outro lugar!')


    if (qtd == 40):
        print('O ônibus está lotado! Bora!')
        break


    continuar = input('Deseja realizar uma nova reserva? (s/n)')
    if (continuar == 'n'):
        break


for i in range(0, 10, 1):
    print(onibus[i])
