#Calculando custo de viagem a depender da distância
km=float(input('Qual a distância em Km da viagem? '))
if km<=200:
    print('O custo da viagem será de R$:{:.2f}.'.format(km*0.5))
else:
    print('O custo da viagem será de R$:{:.2f}.'.format(km*0.45))
print('Boa viagem!')