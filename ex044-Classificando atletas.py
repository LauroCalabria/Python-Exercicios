#Programa para definir categorias competitivas por idade.
import datetime
hoje=datetime.date.today().year
ano=int(input('Digite seu ano de nascimento: '))
idade=hoje-ano
if idade<=9:
    print('{} anos. Categoria mirim.'.format(idade))
elif idade<=14:
    print('{} anos. Categoria infantil.'.format(idade))
elif idade<=19:
    print('{} anos. Categoria junior.'.format(idade))
elif idade==25:
    print('{} anos. Categoria sênior.'.format(idade))
else:
    print('{} anos. Categoria master.'.format(idade))
