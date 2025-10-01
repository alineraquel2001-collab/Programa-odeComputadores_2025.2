ano_atual      = 2025
#ano_nascimento = 2001

#CONVERTER VARIAVEL QUE VAI SER DIGITADA NO INPUT DE STRING EM INTEIRO
ano_nascimento = int(input('Em que ano você nasceu?'))

#ESPECIFICAR QUE A VARIAVEL ANO_NASCIMENTO É INTEIRO
idade          = ano_atual - (ano_nascimento)

#print(idade)

#IMPRIMIR A IDADE
#print('Você tem' ,idade, 'anos')

#iMPRIMIR IDADE - CONCATENAR TEXTO - TRANSFORMA VARIAVEL IDADE QUE É UM INTEIRO EM STRING QUE É TEXTO
#print('Você tem ' + str(idade) + ' anos')

#COLOCAR ENTRE CHAVES PARA IMPRIMIR A VARIAVEL
#print(f'Você tem {idade} anos.')

#VOCÊ NASCEU EM 2001 E TEM 21 ANOS
print(f'Você nasceu em {ano_nascimento} e tem {idade} anos.')