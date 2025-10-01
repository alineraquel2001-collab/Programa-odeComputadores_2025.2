#CALCULAR MÉDIA DE UMA DISCIPLINA NO IFRN, EM QUE A NOTA1 TEM PESO 2 E NOTA2 TEM PESO 3

# Informando as notas como números inteiros
intNota1 = int(input('Informe a nota da ETAPA 1:'))
intNota2 = int(input('Informe a nota da ETAPA 2:'))

#Colocando a função antes do calculo além de converte vai descartar a parte decimal e pegar apenas a parte inteira
#do numero, mostrando apenas o valor sem decimal mas valor verdadeiro na memória
#intMedia = int((intNota1*2 + intNota2*3) / 5)

#O round com o ,0 ainda vai mostrar uma casa decimal
#intMedia = round((intNota1*2 + intNota2*3) / 5 , 0)

#O round  vai descartar a parte decimal e arredondar para um valor inteiro, diferente do int que vai apenas descartar
# Calculando a média ponderada e arrendondando 
# para o inteiro mais próximo
intMedia = round((intNota1*2 + intNota2*3) / 5)

print(f'Nota da Etapa 1: {intNota1}')
print(f'Nota da Etapa 2: {intNota2}')

#print(f'Média: {intMedia:.0f}') -> Vai imprimir sem as casas decimais, mas na memória ainda está o valor quebrado
print(f'Média: {intMedia}')