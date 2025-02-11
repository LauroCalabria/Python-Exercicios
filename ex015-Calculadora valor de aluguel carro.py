#Programa para calcular o custo do aluguel de um carro levando em consideração R$: 60.00 por dia mais R$: 0.15 por km rodado.
d=int(input('Quantos dias alugados? '))
k=float(input('Quantos km rodados? '))
v=(d*60)+(k*0.15)
print('O total a pagar é R${:.2f}.'.format(v))
