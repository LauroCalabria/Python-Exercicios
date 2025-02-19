#Programa para calcular média aritimétrica mais completo.
n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
media=(n1+n2)/2
if media<5:
    print('Reprovado. Sua média foi {:.2f}.'.format(media))
elif media>=7:
    print('Aprovado. Sua média foi {:.2f}.'.format(media))
else:
    print('Recuperação. Sua média foi {:.2f}.'.format(media))
