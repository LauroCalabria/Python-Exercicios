#Programa para dizer se um triângulo é equilátero, isosceles ou escaleno.
l1=float(input('Digite o tamanho do primeiro lado do triângulo: '))
l2=float(input('Digite o tamanho do segundo lado do triângulo: '))
l3=float(input('Digite o tamanho do terceiro lado do triângulo: '))
if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
    if l1==l2 and l1==l3:
        print('O triângulo formado pelos lados {}, {} e {} é um triângulo equilátero.'.format(l1,l2,l3))
    elif l1==l2 or l1==l3 or l2==l3:
        print('O triângulo formado pelos lados {}, {} e {} é um triângulo isóceles.'.format(l1,l2,l3))
    elif l1!=l2 and l1!=l3 and l2!=l3:
        print('O triângulo formado pelos lados {}, {} e {} é um triângulo escaleno.'.format(l1,l2,l3))
else:
    print('Estes três valores não conseguem formar um triângulo.')
