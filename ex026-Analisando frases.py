#Analisando frases
-frase=str(input('Digite uma frase: ').strip().lower())
print('A frase digitada tem {} letras a.'.format(frase.count('a')))
print('A primeira letra a fica na posição {}.'.format(frase.find('a')+1))
print('A ultima letra a aparece na posição {}.'.format(frase.rfind('a')+1))
