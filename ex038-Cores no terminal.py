#Cores no terminal
print('\033[7;30;45mHello, world!\033[m')
a=3
b=5
cores={'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pretoebranco':'\033[7;30m'}
print('Os valores sao \033[32m{}\033[m e \033[31m{}\033[m.'.format(a,b))
print('O valor e: {}{}{}.'.format('\033[32m',a,'\033[m'))
print('O valor e: {}{}{}.'.format(cores['azul'],b,cores['limpa']))
