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
      - Acima de 35.0: Obesidade Grau II

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
        else:
            classificacao = "Obesidade Grau II"

        print(f"Classificação: {classificacao}")

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

# Executa o programa
calcular_imc()