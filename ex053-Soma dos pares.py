#Programa para ler 6 números e mostrar a soma dos pares.
s=0
for c in range(1,7):
    n=int(input('Digite o {}º número: '.format(c)))
    if n%2==0:
        s=s+n
print('A soma dos numéros pares é {}.'.format(s))
