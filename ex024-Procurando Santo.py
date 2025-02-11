#Procurando uma palavra
cidade=str(input('Digite sua cidade: ')).strip()
print(cidade[:5].upper()=='SANTO')
cidade=cidade.lower()
print('santo' in cidade[:5])
print(cidade[:5]=='santo')
