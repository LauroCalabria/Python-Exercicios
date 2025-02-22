#Programa para ler o peso de 5 pessoas e dizer qual o maior e o menor peso.
maior=0
menor=999999999999999
for c in range(1,6):
    p=float(input('Digite o peso em kg: '))
    if p>maior:
        maior=p
    if p<menor:
        menor=p
print('O maior peso é {}kg.'.format(maior))
print('O menor peso é {}kg.'.format(menor))
