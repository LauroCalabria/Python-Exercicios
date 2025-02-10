#Medindo a área de uma parede e a quantidade de tinta que será utilizada para pintar.
a=float(input('Qual a altura da parede?'))
l=float(input('Qual a largura da parede?'))
ar=(a*l)
t=(ar/2)
print('Sua parede tem uma área de {:.2f}m².'.format(ar))
print('Será necessário {:.1f} latas de tinta.'.format(t))
