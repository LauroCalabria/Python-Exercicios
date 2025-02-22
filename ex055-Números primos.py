#programa para dizer se um número é primo.
n=int(input('Digite um número inteiro: '))
t=0
for c in range(1,n+1):
    if n%c==0:
        print('\033[34m', end='')
        t=t+1
    else:
        print('\033[31m',end='')
    print(c,end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n,t))
if t==2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))
