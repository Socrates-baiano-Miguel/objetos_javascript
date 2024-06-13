import random;

print ('*********************************')
print ('Bem Vindo Ao Jogo De Adivinnhação')
print ('*********************************')

#Definindo o número secreto
numeroS = random.randrange(1,101)
rodada = 1
point = 1000
#print(numeroS)
#Definindo o número de tentativas

print("Qual o Nivel de Dificuldade ?")
print("(1)-Ezeez, (2)-Ai é Foda, (3)-Hardicori, (4)-Tá Di Haki, (5)-EU SOU UM DEUUSSS!!!!!!!")

nivel = int(input("ESCOLHA: "))

if(nivel == 1):
    numero_tentativas = 20
elif(nivel == 2):
    numero_tentativas = 10  
elif(nivel == 3):
    numero_tentativas = 7    
elif(nivel == 4):
    numero_tentativas = 3   
else:
    numero_tentativas = 1

while(rodada <= numero_tentativas):
    print('Tentativa ', rodada,'de ', numero_tentativas, 'tentativas restantes')
    chute_string = input('Digite Um número entre 0 e 100: ')
    chute = int(chute_string)

#declarando as condições
    if numeroS == chute: 
        print('Tu é Foda')
        break
    elif(chute < numeroS):
        print('BATEU NA TRRRRRRAVE!!!!!!! É um Numero Menor')
        print('END GAME O NUMERO ERA', numeroS )
    else:
        print('Tu é Mt Ruim Meu Nobre É Maior') 
        backpoint = abs(numeroS - chute)
        point = point - backpoint
        numero_tentativas -= 1
        rodada = rodada +1  

if(_name_=="_main_"):
    jogar_adivinhação()