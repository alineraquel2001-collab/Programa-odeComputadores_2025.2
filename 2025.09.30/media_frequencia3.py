# Função para validar notas
def nota_valida(nota):
    return 0 <= nota <= 100

# Entrada das notas
nota1 = float(input("Digite a primeira nota (peso 2): "))
nota2 = float(input("Digite a segunda nota (peso 3): "))

# Verificação da validade das notas
if not nota_valida(nota1) or not nota_valida(nota2):
    print("\n❌ ERRO: As notas devem estar entre 0 e 100.")
    exit()  # Encerra o programa

# Entrada da carga horária e faltas
carga_horaria = int(input("Digite a carga horária da disciplina (em horas/aula): "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))

# Cálculo da média ponderada
media = ((nota1 * 2) + (nota2 * 3)) / 5

# Cálculo da frequência
frequencia = ((carga_horaria - faltas) / carga_horaria) * 100

# Exibição dos resultados
print("\n📊 RESULTADOS:")
print(f"Média final: {media:.2f}")
print(f"Frequência: {frequencia:.1f}%")