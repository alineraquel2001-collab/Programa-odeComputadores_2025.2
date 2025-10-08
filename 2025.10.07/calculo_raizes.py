'''
	Crie um programa em Python que calcule as raízes de uma equação do 2º grau.
	
	O programa deve:
	
		- Ler os valores de a, b e c como entrada;
		
		- Verificar se o valor de a é zero. Caso seja, a equação não será do 
		  2º grau e o programa deve informar o usuário sobre isso e encerrar;
		  
		- Calcular o discriminante(delta) e, com base no valor de delta:
			
			- delta > 0 : a equação possui duas raízes reais distintas. 
			  O programa deve calcular e exibir ambas as raízes;
			  
			- delta = 0 : a equação possui uma única raiz real. 
			  O programa deve calcular e exibir a raiz única;
			  
			- delta < 0 : a equação não possui raízes reais. 
			  O programa deve informar ao usuário que não existem raízes reais.
			  
		- Tratar as exceções devidas.
'''

import math

def calcular_raizes():
    try:
        print("Calculadora de equações do 2º grau (ax² + bx + c = 0)")

        # Entrada dos coeficientes
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))

        # Verificação se é equação do 2º grau
        if a == 0:
            print("Este não é uma equação do 2º grau (a = 0). Encerrando o programa.")
            return

        # Cálculo do discriminante (delta)
        delta = b**2 - 4*a*c
        print(f"Delta = {delta}")

        if delta > 0:
            # Duas raízes reais
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            print("A equação possui duas raízes reais distintas:")
            print(f"x1 = {raiz1}")
            print(f"x2 = {raiz2}")
        elif delta == 0:
            # Uma raiz real
            raiz = -b / (2 * a)
            print("A equação possui uma raiz real:")
            print(f"x = {raiz}")
        else:
            # Nenhuma raiz real
            print("A equação não possui raízes reais (delta < 0).")

    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de digitar números válidos.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Executar o programa
calcular_raizes()