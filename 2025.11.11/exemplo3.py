'''strTexto = 'natal'

for letra in strTexto:
    print(letra, end='')
'''
strTexto = input('Digite algo:')

palavras = strTexto.split()

for palavra in palavras:
    print(palavra)

'''
strTexto = input('Digite algo:')

for letra in strTexto:
    if letra != ' ':
        print (letra, end='')
    else:
        print('')

print (letra, end='' if letra != '' else '\n') - Ternário

'''
