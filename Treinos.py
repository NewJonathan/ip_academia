tipo = 3


def rotina(tipo):
    objetivo = {'1': '3 Séries de 8-12 repetições com 1 min de descanso entre elas\n '
                     'PEITO: Supino Reto, Cross Over\n'
                     'COSTAS: Pulley Frente, Remada curvada\n'
                     'PERNAS: Leg press, Flexora\n',
                '2': '3 Séries de 15-20 repetições com 30s de descanso entre elas\n'
                     'PEITO: Flexão de Braços, Crucifixo inclinado\n'
                     'COSTAS: Crucifixo invertido, Pull over\n'
                     'PERNAS: Adução de coxa, Panturrilha Sentado\n',
                '3': '4 Séries de 4-6 repetições com 2 min de descanso entre elas\n'
                     'PEITO: Voador, Supino declinado\n'
                     'COSTAS: Remada Baixa, Pull down\n'
                     'PERNAS: Agachamento, Abdução de coxa\n'}
    if tipo == 1:
        resultado = objetivo['1']
    elif tipo == 2:
        resultado = objetivo['2']
    elif tipo == 3:
        resultado = objetivo['3']
    return resultado

print(rotina(tipo))
