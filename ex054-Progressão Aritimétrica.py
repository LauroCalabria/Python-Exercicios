#Programa que lê o primeiro termo e a razão de uma PA
t=int(input('Digite o primeiro termo da PA: '))
r=int(input('Agora digite a razão: '))
for c in range(t,t+r*10,r):
    print(c,end=' ')
