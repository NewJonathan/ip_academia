#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:46:51 2020

@author: macbookpro
"""


def calculo_imc (peso, altura):
    imc = peso / (altura)**2
    return imc

cadastro = input('Deseja fazer seu cadastro (Sim/Não)?: ')

lista_clientes = []
lista_idades = []
lista_pesos = []
lista_alturas = []
lista_telefones = []
lista_imc = []

if(cadastro == 'Sim'):
    while (cadastro == 'Sim'):
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        peso = float(input('Digite seu peso: '))
        altura = float(input('Digite sua altura: '))
        telefone = input('Digite seu número para contato: ')
        print()
        print(f'Seu IMC é: {calculo_imc(peso, altura)}')
        print()
    
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
            
        lista_clientes.append(nome)
        lista_idades.append(idade)
        lista_pesos.append(peso)
        lista_alturas.append(altura)
        lista_telefones.append(telefone) 
        lista_imc.append(calculo_imc(peso, altura))
            
        continuar = input('Desejar continuar (Sim/Não)?: ')

        
        if (continuar == 'Sim'):
            continue 
        
        else:
            print()
            print('Cadastro realizado com sucesso!')
            print()
            print('Fim do programa.')
            break

else:
    print('Fim do programa.')

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
    
    
    