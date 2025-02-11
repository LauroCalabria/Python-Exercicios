#Calculando aumentos variáveis
s=float(input('Digite seu salário atual: R$:'))
if s>1250:
    print('Seu novo salário será: R$:{:.2f}.'.format(s*1.10))
else:
    print('Seu novo salário será: R$:{:.2f}.'.format(s*1.15))
print('Parabéns pelo aumento!')