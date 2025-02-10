#Aprendendo as operações matemáticas
nome=str(input('Qual o seu nome?'))
print('Prazer em te conhecer {:-^10}!'.format(nome))

n1=int(input('Um valor inteiro:'))
n2=int(input('Outro valor inteiro:'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
r=n1%n2
e=n1**n2
print('A soma vale {}.'.format(n1+n2))
print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}.'.format(s,m,d), end=' ')
print('Divisão inteira é {}, o resto é {} e a potencia é {}.'.format(di,r,e))
