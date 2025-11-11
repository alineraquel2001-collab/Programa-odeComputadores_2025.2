'''
   Faça um programa que solicite ao usuário um número inteiro e
   informe se ele é primo ou não.
'''
#USANDO FOR
# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Números menores que 2 não são primos
if numero < 2:
    print(f"{numero} não é um número primo.")
else:
    # Verifica se o número é divisível por algum número entre 2 e sua raiz quadrada
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    
    # Exibe o resultado
    if eh_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")

'''
#USANDO WHILE
# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Números menores que 2 não são primos
if numero < 2:
    print(f"{numero} não é um número primo.")
else:
    i = 2
    eh_primo = True

    # Enquanto i for menor ou igual à raiz quadrada de numero
    while i * i <= numero:
        if numero % i == 0:
            eh_primo = False
            break
        i += 1

    # Exibe o resultado
    if eh_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")

  
'''