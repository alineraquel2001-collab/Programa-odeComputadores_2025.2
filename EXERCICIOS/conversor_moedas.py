#ATIVIDADE - CONVERSOR DE MOEDA

print('Vamos converter o valor em reais (R$) para dólar (US$) !!!')

#USUARIO VAI DIGITAR O VALOR EM REAL
valorReais = float(input('Informe o valor em R$: '))

#USUARIO VAI DIGITAR O VALOR EM DOLAR
cotacaoDolar = float(input('Informe a cotação do dólar US$:'))

#CONVERTER REAL EM DOLAR
converter = valorReais / cotacaoDolar

#MOSTRA RESULTADO - REAL CONVERTIDO EM DOLAR
print('-----------------------------------------------------------------------')
print(f'Com {valorReais} você poderá comprar aproxidamente US$ {converter:.2f}')