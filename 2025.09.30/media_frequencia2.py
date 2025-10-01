# Informando as notas como números inteiros
intNota1 = int(input('Informe a nota da ETAPA 1: '))
intNota2 = int(input('Informe a nota da ETAPA 2: '))

# Verificando se as notas são válidas (entre 0 e 100)

# Informando a carga horária da disciplina (horas/aula)
# e a quantidade de faltas do aluno
intCargaHoraria = int(input('Informe a Carga Horária da Disciplina (h/a): '))
intFaltas = int(input('Informe a quantidade de faltas do aluno: '))

# Calculando a média ponderada e arredondando 
# para o inteiro mais próximo
intMedia = round( (intNota1*2 + intNota2*3) / 5)

# Calculando a frequência do aluno
fltFrequencia = round( (1 - (intFaltas / intCargaHoraria)) * 100, 1)

# Mostrando as notas e a média
print(f'Nota da Etapa 1: {intNota1}')
print(f'Nota da Etapa 2: {intNota2}')
print(f'Média..........: {intMedia}')

# Mostrar a Frequência
print(f'Total de Aulas.: {intCargaHoraria}')
print(f'Total de Faltas: {intFaltas}')
print(f'Frequência.....: {fltFrequencia}%')

# Mostrando se o aluno está APROVADO, PROVA FINAL ou REPROVADO
# TODO: implementar a lógica para mostrar se o aluno foi 
# reprovado por nota, por frequência ou por ambos
if (intMedia >= 60) and (fltFrequencia>=75):
   print('APROVADO')
elif (intMedia >= 20) and (fltFrequencia>=75):
   print('PROVA FINAL')
else:
   print('REPROVADO')