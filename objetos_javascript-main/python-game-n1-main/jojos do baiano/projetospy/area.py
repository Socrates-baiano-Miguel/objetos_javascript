import math

def aTriangulo():
     
    altura = float(input('Digite a Altura do Triangulo: '))
    
    base = float(input('Digite a Base do Triangulo: '))
    
    areat = round(((base * altura)/ 2),2)
    print('A área do Triangulo É De ',areat)
    
def aQuadrado(): 
    
    lado = float(input('Digite a Altura do Quadrado: '))
    
    areaq = lado**2
    
    print('A área do quadrado é de ', areaq)
    
def aRetângulo():
    
    alturaret = float(input('Digite a Altura do Retangulo: '))
    
    baseret = float(input('Digite a Base do Retangulo: '))
    
    arearet = round((alturaret * baseret),2)
    
    print('A área do retângulo é de ', arearet)
    
def aCirculo():
    
    raio = float(input('Digite o raio do circulo: '))
    
    areac = round((math.pi * raio**2),2)
    
    print('A área do círculo  é de ', areac)
    
escolha=True

while escolha:
    print('/n')
    print('Calculadora De Areas')
    print("""""")
    
    escolha= input("Escolha uma opção:  ")
    if escolha == "1":
        print('/n')
        aTriangulo()
    
    elif escolha == "2":
      print('/n')
      aQuadrado()

    elif escolha == "3":
     print('/n')
     aRetângulo()
     
    elif escolha == "4":
     print('/n')
     aCirculo()
    
    elif escolha == "5":
     print("/n Adeus")
     escolha = None
    
    else:
       print("\n Escolha não válida.\n Tente outra vez.")
     
     
    
   