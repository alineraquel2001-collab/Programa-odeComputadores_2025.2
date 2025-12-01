'''
   Reescreva o código do exercício anterior, mas desta vez utilizando listas
   compostas (listas dentro de listas) para armazenar as informações dos alunos.
'''

# Lista composta para armazenar todos os alunos
# Estrutura: [ [nome, nota1, nota2, media], ... ]
alunos = []

# Entrada de dados
for i in range(5):
    print(f"\n--- Aluno {i+1} ---")
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota da Etapa 1: "))
    nota2 = float(input("Digite a nota da Etapa 2: "))

    # Cálculo da média IFRN
    media = ((nota1 * 2) + (nota2 * 3)) / 5

    # Adiciona todos os dados em uma única lista interna
    alunos.append([nome, nota1, nota2, media])

# Impressão formatada
print("\nNome do Aluno\t\tEtapa 1\tEtapa 2\tMédia")
print("--------------------------------------------------")

for aluno in alunos:
    print(f"{aluno[0]:20}\t{aluno[1]:.1f}\t{aluno[2]:.1f}\t{aluno[3]:.1f}")

print("--------------------------------------------------")