#Jogo para tentar advinhar o número
import random
from time import sleep
n=random.randint(0,5)
u=int(input('Tente advinhar o número inteiro entre 0 e 5 que escolhi: '))
print('Processando...')
sleep(1)
if n==u:
    print('Parabéns você advinhou! O número é {}.'.format(n))
else:
    print('Tente novamente, o número era {}.'.format(n))
