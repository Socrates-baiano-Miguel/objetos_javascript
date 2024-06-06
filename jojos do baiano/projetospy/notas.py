print('**************')
print('Receber A Nota')
print('**************')

nota = float(input('Digite A Nota: '))

if nota < 3:
    print('Você Tirou Um D Está Reprovado')
    
elif nota < 6:
    print('Você Tirou Um C Está De Recuperação')
     
elif nota < 8:     
    print('Você Tirou Um B Está Aprovado')
    
else:
    print('Você Tirou Um A+ Está De Parabéns')