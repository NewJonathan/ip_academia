
def calculo_imc (peso, altura):
    imc = peso / (altura)**2
    return imc


        if (calculo_imc(peso, altura) < 18.5):
            print('Você encontra-se abaixo do peso')
          
        if (18.5 < calculo_imc(peso, altura) <= 24.9):
            print('Você encontra-se com o peso normal')
          
        if (25 <= calculo_imc(peso, altura) <= 29.9):
            print('Você encontra-se com sobrepeso')
       
        if (30 <= calculo_imc(peso, altura) <= 34.9):
            print('Você encontra-se com obesidade de grau I')
        
        if (35 <= calculo_imc(peso, altura) <= 39.9):
            print('Você encontra-se com obesidade de grau II')
    
        if (calculo_imc(peso, altura) >= 40):
            print('Você encontra-se com obesidade de grau III ou mórbida')

        lista_imc.append(calculo_imc(peso, altura))

soma_idades = 0
soma_pesos = 0
soma_alturas = 0
soma_imc = 0

for i in range(0, len(lista_idades)):
    soma_idades += lista_idades[i]
    
    soma_pesos += lista_pesos[i]
    
    soma_alturas += lista_alturas[i]
    
    soma_imc += lista_imc[i]

media_idades = [(soma_idades) / len(lista_idades)]
media_pesos = [(soma_pesos) / len(lista_pesos)]
media_alturas = [(soma_alturas) / len(lista_alturas)]
media_imc = [(soma_imc) / len(lista_imc)]
    
    
    
