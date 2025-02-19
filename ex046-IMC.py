#Programa para cálculo de IMC.
p=float(input('Insira o seu peso em kg: '))
a=float(input('Insira a sua altura em metros: '))
imc=(p/(a*a))
if imc<18.5:
    print('Seu IMC é: {:.1f}. Você está abaixo do peso.'.format(imc))
elif imc<25:
    print('Seu IMC é: {:.1f}. Você está no peso ideal.'.format(imc))
elif imc<30:
    print('Seu IMC é: {:.1f}. Você está com sobrepeso.'.format(imc))
elif imc<40:
    print('Seu IMC é: {:.1f}. Você está com obesidade.'.format(imc))
else:
    print('Seu IMC é: {:.1f}. Você está com obesidade mórbida'.format(imc))
