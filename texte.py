minha_lista = [10, 20, 30, 40, 50]

# Valor que você quer encontrar
try:
    elemento_procurado = input("Digite o valor procurado: ")

except ValueError:
    print(f'O elemento {elemento_procurado} não está na lista.')   

try:
    # Encontrar a posição do elemento na lista
    posicao = minha_lista.index(elemento_procurado)
    print(f'O elemento {elemento_procurado} está na posição {posicao} da lista.')
except ValueError:
    print(f'O elemento {elemento_procurado} não está na lista.')