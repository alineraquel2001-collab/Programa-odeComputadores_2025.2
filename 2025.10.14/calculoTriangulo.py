'''
   Desenvolva um código em Python que solicite ao usuário que informe os 
   comprimentos dos três lados de um triângulo. 
   
   Em seguida, verifique se esses comprimentos podem formar um triângulo. 
   Caso afirmativo, calcule e informe os valores dos ângulos do triângulo e 
   classifique-o quanto aos lados e aos ângulos.

   Instruções:
      - Peça ao usuário para inserir os comprimentos dos três lados do triângulo;
      - Verifique se os comprimentos fornecidos podem formar um triângulo. 
        Caso contrário, informe que não é possível formar um triângulo com esses lados;
      - Se for possível formar um triângulo, calcule os três ângulos do triângulo;
      - Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) 
        e aos ângulos (agudo, obtuso ou retângulo);
      - Exiba a classificação do triângulo quanto aos lados e aos ângulos.

   Observações:
      - Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, 
        é necessário verificar a seguinte condição: A soma de quaisquer dois lados de 
        um triângulo deve ser sempre maior que o terceiro lado;
      - Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo;
      - Para classificar quanto aos lados, verifique se os três lados são iguais 
        (equilátero), se dois lados são iguais (isósceles) ou se todos os lados são 
        diferentes (escaleno);
      - Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 
        90 graus (obtuso), se um dos ângulos é igual a 90 graus (retângulo) 
        ou se todos os ângulos são menores que 90 graus (agudo);
      - Considere que os ângulos são expressos em graus.

   Dica: Utilize a biblioteca math.
     Dica: Utilize a biblioteca math.
   https://docs.python.org/3/library/math.html
'''
import math 

try:
    #Digitar lados dos triangulos
    ladoA = float(input("Digite o comprimento do lado a: "))
    ladoB = float(input("Digite o comprimento do lado b: "))
    ladoC = float(input("Digite o comprimento do lado c: "))

    # Verifica se os lados são positivos
    if ladoA <= 0 or ladoB <= 0 or ladoC <= 0:
        print("Os comprimentos dos lados devem ser maiores que zero.")
    else:
        # Verifica se os lados formam um triângulo
        if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
            
            # Calcula os ângulos usando a Lei dos Cossenos
            # cos(C) = (a² + b² - c²) / (2ab)
            def calcula_angulo(a, b, c):
                cos_c = (a**2 + b**2 - c**2) / (2 * a * b)
                cos_c = min(1, max(-1, cos_c))  # Corrige possíveis erros numéricos
                return math.degrees(math.acos(cos_c))
            
            ang_a = calcula_angulo(ladoB, ladoC, ladoA)
            ang_b = calcula_angulo(ladoA, ladoC, ladoB)
            ang_c = calcula_angulo(ladoA, ladoC, ladoB)

            print(f"Ângulos do triângulo: A={ang_a:.2f}°, B={ang_b:.2f}°, C={ang_c:.2f}°")

            # Classificação quanto aos lados
            if ladoA == ladoB == ladoC:
                tipo_lados = "Equilátero"
            elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
                tipo_lados = "Isósceles"
            else:
                tipo_lados = "Escaleno"

            # Classificação quanto aos ângulos
            if any(abs(angulo - 90) < 1e-5 for angulo in [ang_a, ang_b, ang_c]):
                tipo_angulo = "Retângulo"
            elif any(angulo > 90 for angulo in [ang_a, ang_b, ang_c]):
                tipo_angulo = "Obtuso"
            else:
                tipo_angulo = "Agudo"

            print(f"Classificação do triângulo quanto aos lados: {tipo_lados}")
            print(f"Classificação do triângulo quanto aos ângulos: {tipo_angulo}")
        else:
            print("Não é possível formar um triângulo com esses lados.")

except ValueError:
    print("Por favor, insira valores numéricos válidos para os lados.")

