pessoas = []
for i in range(3):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))
    pessoas.append({"Nome": nome, "Idade": idade})

print("\nDados de todas as pessoas:")
for pessoa in pessoas:
    print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}")