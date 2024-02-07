nomes = []
rms = []
cursos = []
qtd_alunos = 0


print('Cadastro de Alunos')


while(True):
    print('Menu:')
    print('1 - Incluir')
    print('2 - Excluir')
    print('3 - Exibir')
    print('4 - Sair')
    opcao = int(input('Digite uma opção: '))


    if (opcao == 1):
        nome = input('Digite o nome do aluno: ')  
        rm = input('Digite o RM do aluno: ')
       
        possuiCurso = input('O aluno possui curso? S/N').upper()


        if (possuiCurso == 'S'):
            curso = input('Digite o nome do curso: ')
        else:
            curso = 'Sem curso'


        nomes.append(nome)
        rms.append(rm)
        cursos.append(curso)


        qtd_alunos+=1


        print('Aluno cadastrado com sucesso!')
        input()
    elif (opcao == 2):
        print('Alunos cadastrados:')
        for i in range(0, qtd_alunos, 1):
            print(f'Id: {i} | Nome: {nomes[i]} | RM: {rms[i]} | Curso: {cursos[i]}')
       
        id = int(input('Digite o ID do aluno que deseja excluir: '))


        while( (id < 0) or (id > qtd_alunos-1) ):
            print('Erro! O ID digitado não existe!')
            id = int(input('Digite o ID do aluno que deseja excluir: '))


        nomes.pop(id)
        rms.pop(id)
        cursos.pop(id)


        qtd_alunos-=1


        print('Aluno excluído com sucesso!')
        input()
    elif (opcao == 3):
        print('Alunos cadastrados:')
        for i in range(0, qtd_alunos, 1):
            print(f'Id: {i} | Nome: {nomes[i]} | RM: {rms[i]} | Curso: {cursos[i]}')


        input()
    else:
        break
