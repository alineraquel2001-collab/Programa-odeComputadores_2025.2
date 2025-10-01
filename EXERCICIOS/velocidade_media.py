#CALCULAR VELOCIDADE MÉDIA

print('Vamos Calcular a velocidade média!!!')

#USUARIO VAI DIGITAR A DISTÂNCIA PERCORRIDA EM KM
distancia = float(input("Informe a distância percorrida em KM: "))

#USUARIO VAI DIGITAR O TEMPO GASTO EM HORAS
tempo = float(input('Informe o tempo gasto em horas: '))

#CALCULE A VELOCIDADE MÉDIA
velocidadeMedia = distancia / tempo

#MOSTRAR RESULTADO
print('-----------------------------------------------------')
print(f'A velocidade média foi de {velocidadeMedia:.2f} km/h')