import sys

strTexto = input ('Digite uma palavra: ')

if ' ' in strTexto:
    sys.exit('Você digitou mais de uma palavra!')

#Inverter palavra
strTextoInvertido = strTexto[::-1]
print(strTexto)
print(strTextoInvertido)
if strTexto.lower() == strTextoInvertido.lower():
    print('Palindromo')
else:
    print('Não é palindromo')


#lower - converter todas as letras de uma string para minúsculas.