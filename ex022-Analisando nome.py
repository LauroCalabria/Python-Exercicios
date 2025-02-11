#Tratando o nome
frase=str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}.'.format(frase.upper()))
print('Seu nome em minúsculas é {}.'.format(frase.lower()))
space=frase.count(' ')
print('Seu nome tem ao todo {} letras.'.format(len(frase)-space))
#print('Seu primeiro nome tem {} letras.'.format(frase.find(' ')))
dividido=frase.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(dividido[0],len(dividido[0])))
