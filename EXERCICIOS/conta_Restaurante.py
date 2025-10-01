#SIMULADOR DE CONTA DE RESTAURANTE

print('Simular conta de restaurante!!!')

#USUARIO VAI INFORMAR O VALOR DA CONTA
valorConta = float(input('Informe o valor da sua conta (R$): '))

#USUARIO VAI INFORMAR A PORCENTAGEM DA GORJETA
porcentagemGorjeta = float(input('Informe a porcentagem da gorjeta (%): '))

#CALCULAR GORJETA
gorjeta    = valorConta * (porcentagemGorjeta / 100)

#CALCULAR TOTAL DA CONTA
valorTotal = valorConta + gorjeta

#MOSTAR RESULTADO
print('----------------------------------------------------')
print(f'O valor da conta: R$ {valorConta:.2f}')
print(f'Gorjeta: ({porcentagemGorjeta} %): R$ {gorjeta:.2f}') 
print(f'O valor total a ser pago é: R$ {valorTotal:.2f}')