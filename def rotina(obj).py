#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:24:37 2020

@author: macbookpro
"""
Hipertrofia = ['Supino reto', 'Cross over',
               'Pulley frente','Remada curvada', 
               'Flexora']
                   
Emagrecimento = ['Flexão de braço', 'Crucifixo inclinado',
                 'Crucifixo invertido', 'Pull over', 'Adução de coxa',
                 'Panturrilha sentado']

Potencia = ['Supino declinado', 'Remada baixa', 'Pull down',
            'Agachamento', 'Abdução de coxa']

def rotina(obj): 
    if obj == 1:
        print()
        print('3 séries entre 8-12 repetições')
        print()
        for i in range(0, len(Hipertrofia)):
            print(Hipertrofia[i])
            
    if obj == 2:
        print()
        print('3 séries entre 12-15 repetições')
        print()
        for j in range(0, len(Emagrecimento)):
            print(Emagrecimento[j])
    if obj == 3:
        print()
        print('4 séries entre 4-6 repetições')
        print()
        for k in range(0,len(Potencia)):
            print(Potencia[k])

obj = int(input('Objetivo: '))
rotina(obj)
