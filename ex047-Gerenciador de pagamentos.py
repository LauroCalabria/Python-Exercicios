#Programa para calcular valor de produto com desconto de 10% em dinheiro, 5% a vista no cartão e juros quando parcelado em mais de duas vezes.
p=float(input('Digite o valor do produto: R$:'))
m=int(input('Em quantas vezes pretende pagar? '))
if m==1:
    x=int(input('Digite 1 se pretende pagar em dinheiro ou 2 se pretende pagar a vista no cartão: '))
    if x==1:
        print('O valor total do produto é de R$:{:.2f} mas como irá pagar em dinheiro o produto sairá por R$:{:.2f}.'.format(p,p*0.9))
    else:
        print('O valor total do produto é de R$:{:.2f} mas como irá pagar a vista em cartão o produto sairá por R$:{:.2f}.'.format(p,p*0.95))
elif m==2:
    print('O valor total do produto é de R$:{:.2f} e cada parcela sairá por R$:{:.2f}'.format(p,p/2))
elif m>=3:
    print('O valor do produto é R$:{:.2f} mas com juros de 20% ficará por R$:{:.2f} e cada parcela sairá por R$:{:.2f}'.format(p,p*1.2,(p*1.2)/m))
