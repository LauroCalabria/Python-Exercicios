#Programa para verificar quando deve se alistar
import datetime
nascimento=int(input('Digite a seu ano de nascimento: '))
ano=datetime.date.today().year
idade=ano-nascimento
if idade>=18 and idade<=45:
    print('Você deve se alistar.')
elif idade<18:
    print('Você deverá se listar em {} anos.'.format(18-idade))
else:
    print('Você deveria ter se alistado a no mínimo {} anos.'.format(idade-45))
