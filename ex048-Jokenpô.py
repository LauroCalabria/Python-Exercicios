#Jokenpô
import random
from time import sleep
print('Então vamos lá, hora do jogo.')
lista=['PEDRA','PAPEL','TESOURA']
x=random.choice(lista)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
j=int(input('Qual a sua jogada? '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô')
print('-'*22)
print(x)
if (x=='PEDRA' and j==0) or (x=='PAPEL' and j==1) or (x=='TESOURA' and j==2):
    print('Empate!')
elif (x=='PEDRA' and j==2) or (x=='PAPEL' and j==0) or (x=='TESOURA' and j==1):
    print('Eu ganhei, tente novamente!')
else:
    print('Você ganhou, já estou pronto pra revanche.')