turma = ('André', 'Fernanda', 'Luiz')

nome = input('Qual o aluno que deseja consultar? ')
if nome in turma:
    print('{} está na turma'.format(nome))
else:
    print('{} não está na turma'.format(nome))