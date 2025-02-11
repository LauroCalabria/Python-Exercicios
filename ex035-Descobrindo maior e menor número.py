#Descobrindo o menor e o maior valor entre tres digitados
n1=float(input('Primeiro número: '))
n2=float(input('Segundo número: '))
n3=float(input('Terceiro número: '))
if n1>n2:
    if n1>n3:
        print('O maior número é: {}.'.format(n1))
    else:
        print('O maior número é: {}.'.format(n3))
else:
    if n2>n3:
        print('O maior número é: {}.'.format(n2))
    else:
        print('O maior número é: {}.'.format(n3))

if n1<n2:
    if n1<n3:
        print('O menor número é: {}.'.format(n1))
    else:
        print('O menor número é: {}.'.format(n3))
else:
    if n2<n3:
        print('O menor número é: {}.'.format(n2))
    else:
        print('O menor número é: {}.'.format(n3))
# Verificar o menor
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
# Verificar o maior
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
