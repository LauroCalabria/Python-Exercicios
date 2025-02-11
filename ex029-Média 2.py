#Calculadora de média
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2
print('A sua media foi {:.2f}.'.format(m))
if m>=7:
    print('Parabéns, você passou por média')
else:
    print('Nos vemos na final')
