'''
   Desenvolva um programa que calcula o IMC de uma pessoa. 
   
   O programa deve pedir o peso em quilogramas (ex: 70.5) e a 
   altura em metros (ex: 1.75). 
   
   A fórmula do IMC é: peso / (altura * altura). 
   
   Após calcular o IMC, o programa deve exibir o valor e a 
   classificação correspondente, de acordo com a tabela:

      - Abaixo de 18.5: Abaixo do peso
      - 18.5 a 24.9: Peso ideal
      - 25.0 a 29.9: Sobrepeso
      - 30.0 a 34.9: Obesidade Grau I
      - 35.0 a 39.9: Obesidade Grau II
      - 40.0 ou mais: Obesidade Grau III

   O programa deve tratar entradas inválidas (não numéricas) e 
   também verificar se a altura informada é maior que zero para evitar 
   um erro de divisão.      
'''

def calcular_imc():
    try:
        peso = float(input("Digite seu peso em kg (ex: 70.5): "))
        altura = float(input("Digite sua altura em metros (ex: 1.75): "))

        if altura <= 0:
            print("Erro: A altura deve ser maior que zero.")
            return

        imc = peso / (altura * altura)

        print(f"\nSeu IMC é: {imc:.2f}")

        # Classificação de acordo com o IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25.0:
            classificacao = "Peso ideal"
        elif imc < 30.0:
            classificacao = "Sobrepeso"
        elif imc < 35.0:
            classificacao = "Obesidade Grau I"
        elif imc < 39.9:
            classificacao = "Obesidade Grau Ii"
        else:
            classificacao = "Obesidade Grau IIi"

        print(f"Classificação: {classificacao}")

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

# Executa o programa
calcular_imc()

'''
import sys

# Entrada de dados com tratamento de erro
try:
   fltPeso   = float(input('Informe o seu peso em quilogramas (ex: 70.5): '))
   fltAltura = float(input('Informe a sua altura em metros (ex: 1.75)...: '))
# Tratamento de erro para valores não numéricos
except ValueError:
   sys.exit('ERRO: Você deve digitar um valor numérico.')
# Tratamento de erro para outros tipos de erro
except Exception as strErro:
   sys.exit(f'ERRO: {strErro}')
# Cálculo do IMC caso tenha passado pelas validações
else:
   # Verifica se a altura é menor ou igual a zero
   if fltAltura <= 0:
      sys.exit('ERRO: A altura deve ser maior que zero.')

   # Verifica se o peso é menor ou igual a zero
   if fltPeso <= 0:
      sys.exit('ERRO: O peso deve ser maior que zero.')

if:
    float_peso <= 0 or float_altura <= 0
    sys.exit('ERRO: Info de peso e altura devem ser maiores que Zero.')
'''