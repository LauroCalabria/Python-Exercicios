#Programa para denunciar multa e valor.
km=int(input('Digite a velocidade do carro: '))
multa=7*(km-80)
if km>80:
    print('Você foi multado em R$:{:.2f}!'.format(multa))
else:
    print('Parabéns Sr. Certinho.')
