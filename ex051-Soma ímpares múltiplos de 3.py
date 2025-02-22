#Programa para calcular a soma de todos os números ímpares que são multiplos de 3 entre 1 e 500.
s=0
v=0
for c in range(3,501,3):
    if c%2==1:
        v=v+1
        print(c, end=' ')
        s=s+c
print(' ')
print('A soma dos {} valores foi {}.'.format(v,s))
