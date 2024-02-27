
# # 54. Criar um programa para controlar as reservas de poltronas de 
# um show do Charlie Brown \o/, sabendo que o show será apresentado em 
# três sessões, manhã, tarde e noite e que a casa de show possui “X” fileiras de “Y” cadeiras cada. 
# Os valores de “X” e “Y” serão digitados. O usuário digita seu nome, lança a sessão, 
# o número da fileira e da cadeira que pretende reservar, e se estiver livre a reserva será efetuada, 
# caso contrário, o programa deverá enviar mensagem comunicando que a poltrona está ocupada e solicitar outro lugar. Perguntar ao usuário se mais alguém pretende fazer reservas. As reservas poderão ser efetuadas até completar um máximo de quatro quintos da capacidade total da casa de show. No final do programa de reservas, exibir um “mapa” mostrando as poltronas da casa de show, por sessão, com os nomes de cada ocupante, ou ainda com a informação “Poltrona livre”.

manha = []
tarde = []
noite = []


fileiras = int(input('Digite a quantidade de fileiras: '))
cadeiras = int(input('Digite a quantidade de cadeiras: '))


for i in range(0, fileiras, 1):
    manha.append([])
    tarde.append([])
    noite.append([])


for i in range(0, fileiras, 1):
    for j in range(0, cadeiras, 1):
        manha[i].append('vazio')
        tarde[i].append('vazio')
        noite[i].append('vazio')




while (True):
    nome = input('Digite seu nome para efetuar a reserva: ')
    sessao = int(input('Digite a sessão (1-Manhã, 2-Tarde, 3-Noite): '))
    fil = int(input(f'Digite a fileira que deseja sentar (1 até {fileiras}): ')) -1
    cad = int(input(f'Digite a cadeira que deseja sentar (1 até {cadeiras}): ')) -1


    if (sessao == 1):
        if (manha[fil][cad] == 'vazio'):
            manha[fil][cad] = nome
            print('Reserva efetuada com sucesso!')
        else:
            print('Poltrona já reservada!')
    elif (sessao == 2):
        if (tarde[fil][cad] == 'vazio'):
            tarde[fil][cad] = nome
            print('Reserva efetuada com sucesso!')
        else:
            print('Poltrona já reservada!')
    elif (sessao == 3):
        if (noite[fil][cad] == 'vazio'):
            noite[fil][cad] = nome
            print('Reserva efetuada com sucesso!')
        else:
            print('Poltrona já reservada!')
    else:
        print('Sessão inválida!')


    continuar = input('Deseja continuar fazendo reservas? (s/n): ')


    if (continuar == 'n'):
        break




print('\n=== Mapa de Reservas - Show CBJR ===')


print('\n\nSessão Manhã:')
for i in range(0, fileiras, 1):
    print(manha[i])


print('\n\nSessão Tarde:')
for i in range(0, fileiras, 1):
    print(tarde[i])


print('\n\nSessão Noite:')
for i in range(0, fileiras, 1):
    print(noite[i])


