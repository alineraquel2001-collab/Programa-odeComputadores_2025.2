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
'''
# EQUAÇÃO DO SEGUNDO GRAU: ax² + bx + c = 0

# Importa o módulo math, que fornece funções matemáticas, como math.sqrt() para calcular raízes quadradas.
import math   

# input(): Lê o valor digitado pelo usuário como texto (string).
# float(): Converte a string para número decimal (ponto flutuante).
# Solicita os coeficientes da equação ao usuário
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

# Verifica se a = 0
if a == 0:
    print("Não é uma equação do 2º grau. (a = 0)")
else:
    # Caso a não seja = 0. Calcula o discriminante (delta) : Δ = b² - 4ac
    # Vai determinar o número de raízes reais da equação 
    delta = b**2 - 4*a*c
    print(f"Delta (Δ) = {delta}")

    if delta > 0:
        # Se delta > 0 a equação tem duas raízes reais diferentes
        # Para calcular as raizes usa Bhaskara: x1 = -b+raiz(Δ)/2a & x2 = -b-raiz(Δ)/2a
        # math.sqrt(delta) calcula a raiz quadrada de delta.
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equação possui duas raízes reais distintas:")
        print(f"x1 = {raiz1}")
        print(f"x2 = {raiz2}")

    elif delta == 0:
        # Se delta = 0, a equação tem uma única raiz real (dupla).
        # Calcula a única raiz real
        raiz = -b / (2 * a)
        print("A equação possui uma raiz real (raiz dupla):")
        print(f"x = {raiz}")

    else:
        # Caso delta < 0, não existem raízes reais, então o programa informa isso ao usuário.
        print("A equação não possui raízes reais (delta < 0).")
