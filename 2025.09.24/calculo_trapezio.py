#ATIVIDADE - CALCULAR ÁREA DO TRAPÉZIO

print('Vamos calcular a área do trapézio!')

#VALOR DA BASE MAIOR DO TRAPÉZIO
base_maior = input('Informe o valor da base maior do trapézio:')

#VALOR DA BASE MENOR DO TRAPÉZIO
base_menor = input('Informe o valor da base menor do trapézio:')

#VALOR DA ALTURA DO TRAPÉZIO
altura = input('Informe o valor da altura do trapézio:')

base_maior = float(base_maior)
base_menor = float(base_menor)
altura = float(altura)

#CALCULAR ÁREA
area = (base_maior + base_menor) * altura / 2

#iMPRIMIR O VALOR DA ÁRE DO TRAPÉZIO
print(f'A Área do trapézio é: {area} .')