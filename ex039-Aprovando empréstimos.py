#Programa para avaliar empréstimo bancário levando em consideração o valor da casa, o salário e o tempo de prestação. O valor da prestação não pode exceder 30% do salário.
valor=float(input('Qual o valor da casa? R$:'))
salario=float(input('Qual o seu salário? R$:'))
tempo=int(input('Em quantos anos pretende financiar? '))
parcela=valor/(tempo*12)
if parcela<=salario*0.3:
    print('Seu crédito foi aprovado e sua parcela mensal custará {:.2f} por {:.0f} anos.'.format(parcela,tempo))
else:
    print('Seu crédito não foi aprovado.')
