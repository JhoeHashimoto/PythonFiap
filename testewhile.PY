qntd = int(input('Digite a quantidade de alunos'))
i = 0
somaidade = 0
while (i < qntd):
    idade = int(input("Digite a idade dos alunos:"))
    somaidade= somaidade + idade
    i += 1 
mediaidade = somaidade/qntd
print(f'Media das idades é{mediaidade}')