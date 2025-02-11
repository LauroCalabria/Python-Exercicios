#2 formas de descobrir a hipotenusa
co=float(input('Digite o valor do cateto oposto: '))
ca=float(input('Agora digite o valor do cateto adjacente: '))
h1=((co**2)+(ca**2))**(1/2)
print('A hipotenusa deste triangulo é {:.2f}.'.format(h1))

import math
h2=math.hypot(co,ca)
print('A hipotenusa deste triangulo é {:.2f}.'.format(h2))
