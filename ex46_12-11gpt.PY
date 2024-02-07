pessoas = []
for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ") 
    while True:
        sexo = input(f"Digite o sexo da {i+1}ª pessoa (F/M): ").upper()
        if sexo == 'F' or sexo == 'M':
            break
        else:
            print("Sexo inválido. Digite 'F' para feminino ou 'M' para masculino.")
            sexo = input(f"Digite o sexo da {i+1}ª pessoa (F/M): ").upper()
    while True:
            idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
            if idade >= 0:
                break
            else:
                print("Idade deve ser um valor positivo.")
    pessoas.append({"Nome": nome, "Sexo": sexo, "Idade": idade})
print("\nDados das pessoas do sexo feminino:")
for pessoa in pessoas:
    if pessoa["Sexo"] == 'F':
        print(f"Nome: {pessoa['Nome']}, Sexo: {pessoa['Sexo']}, Idade: {pessoa['Idade']}")