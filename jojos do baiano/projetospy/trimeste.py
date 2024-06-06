print('***************************')
print('Saber Se Você Passou De Ano')
print('***************************')

n1 = float(input('Digite Sua Nota Do Primeiro Trimestre: '))
n2 = float(input('Digite Sua Nota Do Segundo Trimestre: '))
n3 = float(input('Digite Sua Nota Do Terceiro Trimestre: '))

m = ((n1+n2+n3))/3

if m < 6:
    print('Sua Média É: ', m, 'Você Foi De Americanas')
    
elif m > 6:
    print('Sua Média É: ', m, 'Você Está Aprovado')

