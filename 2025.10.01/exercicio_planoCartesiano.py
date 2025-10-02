# Solicita ao usuário as coordenadas x e y
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

# Verifica a posição do ponto no plano cartesiano
if  x > 0 and y > 0:
    print("O ponto está no quadrante 1.")
elif x < 0 and y > 0:
    print("O ponto está no quadrante 2.")
elif x < 0 and y < 0:
    print("O ponto está no quadrante 3.")
elif x > 0 and y < 0:
    print("O ponto está no quadrante 4.")
elif x == 0 and y == 0:
    print("O ponto está na origem.")
elif y == 0:
    print("O ponto está sobre o eixo x.")
else:
    print("O ponto está sobre o eixo y.")