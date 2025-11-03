'''
   Programa que solicita um número inteiro ao usuário e exiba os n
   primeiros elementos da Série de Fibonacci (usando WHILE).

   Exemplo: n = 10

   Saída: 
      1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''

import sys

try:
    n = int(input('Informe um número inteiro: '))
except ValueError:
    sys.exit('ERRO: O valor informado deve ser inteiro...')
except:
    sys.exit(f'ERRO: {sys.exc_info()}')
else:
    if n <= 0:
        sys.exit('ERRO: Informe um valor inteiro positivo...')

    # Inicializando os dois primeiros termos
    termo1, termo2 = 1, 1

    # Caso o usuário queira apenas 1 termo
    if n == 1:
        print(termo1)
        sys.exit()

    # Exibe os dois primeiros termos
    print(termo1, termo2, end='')

    contador = 3  # Já mostramos dois termos, então começamos no 3º

    # Gera os próximos termos da sequência usando WHILE
    while contador <= n:
        proximo = termo1 + termo2
        print(f', {proximo}', end='')
        termo1, termo2 = termo2, proximo
        contador += 1

    print()  # Quebra de linha final