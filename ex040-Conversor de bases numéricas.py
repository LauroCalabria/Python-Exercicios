#Convertendo números inteiros em binário, octal ou hexadecimal.
num=int(input('Digite um número inteiro: '))
n=int(input('''Digite 1 para converter para binário, 
2 pra converter para octal ou 
3 para converter para hexadecimal: '''))
b=bin(num)[2:]
o=oct(num)[2:]
h=hex(num)[2:]
if n==1:
   print('O número {} em binário fica {}.'.format(num,b))
elif n==2:
    print('O número {} em octal fica {}.'.format(num,o))
elif n==3:
    print('O número {} em hexadecimal fica {}.'.format(num,h))
else:
    print('{} não é uma opção válida.'.format(n))
