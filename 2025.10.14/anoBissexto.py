'''
   Escreva um programa que pede ao usuário para inserir um ano e 
   determina se ele é bissexto ou não. 
   
   Um ano é bissexto se atender a uma das seguintes regras:

      - É divisível por 4, mas não é divisível por 100.

      - É divisível por 400.

      (Por exemplo, 2000 e 2400 são bissextos; 1800, 1900 e 2100 não são). 
      
   O programa deve exibir "O ano [ano] é bissexto." ou 
   "O ano [ano] não é bissexto.". 
   
   Use try...except para validar a entrada.
'''

import sys
#Inicia um bloco try para tentar executar um código que pode gerar erro
try:
        #Usa int() para tentar converter esse texto em um número inteiro.
        ano = int(input("Digite um ano: "))
        
        #Verifica se o ano é bissexto com as regras:
        #O ano é divisível por 400 (ano % 400 == 0)
        #O ano é divisível por 4, mas não por 100 (ano % 4 == 0 and ano % 100 != 0).
        if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
            print(f"O ano {ano} é bissexto.")
        else: #Se a condição de cima não for verdadeira o ano não é bissexto
            print(f"O ano {ano} não é bissexto.")
#Se a conversão falhar (ex: o usuário digitou "abc"), será gerado um erro e o programa pula para o except.
#Captura o erro do tipo ValueError que acontece se a conversão para inteiro falhar            
except ValueError:
        print("Por favor, insira um número inteiro válido para o ano.")