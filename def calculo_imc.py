#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:50:02 2020

@author: macbookpro
"""


def calculo_imc (peso, altura):
    imc = peso / (altura)**2
    return imc

cadastro = input('Deseja fazer seu cadastro (S/N)?: ')
lista_clientes = []
lista_imc = []

if(cadastro == 'S'):
    while (cadastro == 'S'):
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        peso = float(input('Digite seu peso: '))
        altura = float(input('Digite sua altura: '))
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
        lista_imc.append(calculo_imc(peso, altura))
        
        continuar = input('Desejar continuar (S/N)?: ')
        
        if (continuar == 'S'):
            continue
        else:
            print()
            print('Cadastro realizado com sucesso!')
            print()
            print('Fim do programa.')
            break
else:
    print('Fim do programa.')
    
    