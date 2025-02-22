#Programa para descobrir palíndromos
f=str(input('Digite uma frase: ')).strip().upper()
palavras=f.split()
junto=''.join(palavras)
inverso=junto[::-1]
'''inverso=''
for l in range(len(junto)-1,-1,-1):
    inverso=inverso+junto[l]'''
print('Você digitou a frase {} que ao contrário fica {}.'.format(junto,inverso))
if junto==inverso:
    print('Esta frase é palíndromo.')
else:
    print('Esta frase não é palíndromo.')
