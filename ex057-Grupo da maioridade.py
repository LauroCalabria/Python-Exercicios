#Programa que lê o ano de nascimento de 7 pessoas e diz quem ja fez 21 anos.
import datetime
hoje=datetime.date.today().year
menor=0
maior=0
for c in range(1,8):
    a=int(input('Digite o ano de nascimento: '))
    if hoje-a<21:
        menor=menor+1
    else:
        maior=maior+1
print('Temos {} pessoas que são menores de idade.'.format(menor))
print('Temos {} pessoas que são maiores de idade.'.format(maior))
