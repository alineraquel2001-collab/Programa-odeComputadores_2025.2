#ATIVIDADE - CONVERSOR DE TEMPERATURA CELSIUS PARA FAHRENHEIT

print('Vamos converter a temperatura de Celsius (°C) para Fahrenheit (°F) !!!')

#USUARIO VAI DIGITAR A TEMPERATURA EM GRAUS CELSIUS
celsius = float(input('Informe a temperatura em graus Celsius °C: '))

#FORMULA PARA CONVERTER GRAUS CELSIUS EM FAHRENHEIT = °C * 9/5 + 32
fahrenheit = (celsius * 9/5) + 32

#RESULTADO
print('---------------------------------------')

print(f'{celsius}°C equivalem a {fahrenheit}°F')