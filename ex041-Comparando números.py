#Programa que lê dois números inteiros e dis qual o maior.
n1=int(input('Digite o primeiro número inteiro: '))
n2=int(input('Digite o segundo número inteiro: '))
if n1==n2:
    print('Os números {} e {} são iguais.'.format(n1,n2))
elif n1>n2:
    print('{} é maior que {}.'.format(n1,n2))
else:
    print('{} é maior que {}.'.format(n2,n1))
