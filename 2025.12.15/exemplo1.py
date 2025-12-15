'''
   Fazer um programa que leia o conteúdo do arquivo resumo_lotr.txt e imprima na tela.
'''
import os

diretorio = os.path.dirname(__file__)
arqLeitura = open(f'{diretorio}/resumo_lotr.txt','r')

conteudo = arqLeitura.read()

print(conteudo)

arqLeitura.close()