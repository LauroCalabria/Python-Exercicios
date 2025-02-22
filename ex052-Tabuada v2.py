#Tabuada reformulada
n=int(input('Digite um número inteiro para ver sua tabuada: '))
print('A tabuada de {} é:'.format(n))
for c in range(1,11):
    print('{} x {:2} = {}'.format(n,c,n*c))
