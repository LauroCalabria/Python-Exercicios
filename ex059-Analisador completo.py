#Programa para ler nome, idade e sexo e dizer a média de idade, quem é o homem mais velho e quantas mulheres tem menos de 20 anos.
novaidade=0
velho=0
novonome=0
menor=0
for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Digite F para feminino ou M para masculino: ')).strip().lower()
    novaidade=idade+novaidade
    if sexo=='m':
        if idade>velho:
            velho=idade
            novonome=nome
    elif sexo=='f':
        if idade<20:
            menor=menor+1
    else:
        print('O gênero digitado está errado.')
print(' ')
print('A média de idade é: {:.0f} anos.'.format(novaidade/4))
if velho!=0:
    print('O homem mais velho é {} que tem {:.0f} anos.'.format(novonome,velho))
if menor!=0:
    print('{} mulheres tem menos de 20 anos.'.format(menor))
