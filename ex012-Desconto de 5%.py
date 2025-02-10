#Calculando 5% de desconto de tres formas diferentes.
n=float(input('Qual o preço do produto? R$'))
a=n*0.95
novo=n-(n*5/100)
print('Com 5% de desconto ele vai sair por R${:.2f}.'.format(n*0.95))
