'''

   Faça um programa que solicite ao usuário um número de até 4 dígitos inteiro positivo e exiba a soma dos seus algarismos.

   Exemplo: 2456 = 17 (2 + 4 + 5 + 6)

   DICA: Vocês irão usar o operador de divisão inteira (//) e o operador de resto de divisão inteiro (%)

'''

# input - Solicita o número do usuário, int - converte o texto digitado para inteiro
num = int(input("Digite um número inteiro positivo de até 4 dígitos: "))

# Verifica se o número está no intervalo correto
if num < 0 or num > 9999:
    print("Número inválido! Digite um número entre 0 e 9999.")
else:
    # Extrai cada dígito usando divisão inteira e resto
    dig1 = num // 1000            # milhar
    dig2 = (num % 1000) // 100    # centena
    dig3 = (num % 100) // 10      # dezena
    dig4 = num % 10               # unidade

    soma = dig1 + dig2 + dig3 + dig4

    print(f"A soma dos algarismos de {num} é {soma}.")