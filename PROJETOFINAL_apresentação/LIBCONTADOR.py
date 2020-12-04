from tkinter import *

def cadastro():
    def salvadados():
        arquivo = open("dados.txt", "a+")
        nome=entrada1.get()
        idade=entrada2.get()
        peso=entrada3.get()
        altura=entrada4.get()
        celular=entrada5.get()
        objetivo=entrada6.get()
        listadados=[f'\n{nome}\n{idade}\n{peso}\n{altura}\n{celular}\n{objetivo}']
        arquivo.writelines(listadados)
        janela.destroy()
        arquivo.close()
    arquivo = open("dados.txt", "a+")
    arquivo.seek(0)
    ncad=(len(arquivo.readlines())/6)+1
    janela=Tk()
    janela.title('Cadastro')
    Button(janela, text="Cadastrar",width=22, bg='white', fg='black',command=salvadados, font='None 14 bold').grid(row=8, column=0,columnspan=3, sticky=W)
    entrada1=Entry(janela, width=25, bg='white')
    entrada1.grid(row=1, column=1, sticky=W)
    entrada2=Entry(janela, width=25, bg='white')
    entrada2.grid(row=2, column=1, sticky=W)
    entrada3=Entry(janela, width=25, bg='white')
    entrada3.grid(row=3, column=1, sticky=W)
    entrada4=Entry(janela, width=25, bg='white')
    entrada4.grid(row=4, column=1, sticky=W)
    entrada5=Entry(janela, width=25, bg='white')
    entrada5.grid(row=5, column=1, sticky=W)
    entrada6=Entry(janela, width=12, bg='white')
    entrada6.grid(row=6, column=1, sticky=W)
    Label(janela, text="Nome").grid(row=1, column=0, sticky=W)
    Label(janela, text="Idade").grid(row=2, column=0, sticky=W)
    Label(janela, text="Peso").grid(row=3, column=0, sticky=W)
    Label(janela, text="Altura").grid(row=4, column=0, sticky=W)
    Label(janela, text="Telefone").grid(row=5, column=0, sticky=W)
    Label(janela, text="Objetivo:\n1:Hipertrofia\n2:Emagrecimento\n3:Potência").grid(row=6, column=0, sticky=W)
    Label(janela, text='N° de cadastro:\n%d'%ncad).grid(row=6, column=2, sticky=W)
def consulta():
    def pegardados():
        def calculo_imc (peso, altura):
            imc = peso / (altura)**2
            return imc
        def rotina():
            resultado=None
            dict_objetivo = {'1': '3 Séries de 8-12 repetições com 1 min de descanso entre elas\n '
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
            if obj == 1:
                resultado = dict_objetivo['1']
            elif obj == 2:
                resultado = dict_objetivo['2']
            elif obj == 3:
                resultado = dict_objetivo['3']
            L=Label(janela, text=resultado)
            L.grid(row=13, column=0,columnspan=4, sticky=W)
        arquivo = open("dados.txt", "a+")
        numc=(int(entrada4.get())*6)
        arquivo.seek(0)
        listadados=arquivo.readlines()
        obj=int(listadados[numc-1])
        celular=listadados[numc-2]
        altura=float(listadados[numc-3])
        peso=float(listadados[numc-4])
        idade=int(listadados[numc-5])
        nome=listadados[numc-6]
        IMC=calculo_imc(peso, altura)
        Label(janela, text='Nome:', bg='white', fg='black', font='None 12 ').grid(row=4, column=0, sticky=W)
        N=Label(janela, text=' '*50, bg='white', fg='black', font='None 12 ')
        N.grid(row=5, column=0,columnspan=2, sticky=W)
        N=Label(janela, text=nome, bg='white', fg='black', font='None 12 ')
        N.grid(row=5, column=0,columnspan=2, sticky=W)
        Label(janela, text='Idade:%d anos'%idade, bg='white', fg='black', font='None 12 ').grid(row=6, column=0, sticky=W)
        Label(janela, text='Peso:%.2f kg'%peso, bg='white', fg='black', font='None 12 ').grid(row=7, column=0, sticky=W)
        Label(janela, text='Altura:%.2f m'%altura, bg='white', fg='black', font='None 12 ').grid(row=8, column=0, sticky=W)
        Label(janela, text='Telefone:%s'%celular, bg='white', fg='black', font='None 12 ').grid(row=10, column=0,columnspan=2, sticky=W)
        Label(janela, text='IMC:%.2f'% IMC, bg='white', fg='black', font='None 12 ').grid(row=9, column=0, sticky=W)
        Label(janela, text='Objetivo:  %s'%obj).grid(row=11, column=0, sticky=W)
        Button(janela, text='Consultar rotina', command=rotina).grid(row=12, column=0, sticky=W)
    
    janela=Tk()
    janela.title('Consulta')
    janela.configure(background="white")
    Label(janela, text="Consultar cadastro", bg='white', fg='black', font='None 14 bold').grid(row=1, column=0,columnspan=2, sticky=W)
    Label(janela, text="Insira N° de cadastro:", bg='white', fg='black', font='None 12 ').grid(row=2, column=0,columnspan=2, sticky=W)
        
    entrada4=Entry(janela, width=12, bg='white')
    entrada4.grid(row=3, column=0, sticky=W)
        
    Button(janela, text='Consultar', command=pegardados).grid(row=3, column=1, sticky=W)
def info():
    arquivo = open("dados.txt", "a+")
    arquivo.seek(0)
    lista_dados=arquivo.readlines()
    soma_idades = 0
    soma_pesos = 0
    soma_alturas = 0
    soma_imc = 0
    for i in range(0, len(lista_dados),6):
        soma_idades += int(lista_dados[i+1])
        
        soma_pesos += float(lista_dados[i+2])
        
        soma_alturas += float(lista_dados[i+3])

        imc=float(lista_dados[i+2])/float(lista_dados[i+3])**2
        
        soma_imc += imc

    media_idades = (soma_idades) / (len(lista_dados)/6)
    media_pesos = (soma_pesos) / (len(lista_dados)/6)
    media_alturas = (soma_alturas) / (len(lista_dados)/6)
    media_imc = (soma_imc) / (len(lista_dados)/6)

    janela=Tk()
    janela.title('Informações')
    janela.configure(background="white")
    Label(janela, text="Informações dos cadastrados:", bg='white', fg='black', font='None 14 bold').grid(row=0, column=0, sticky=W)
    Label(janela, text="Média das idades:%.2f anos"%media_idades, bg='white', fg='black', font='None 12 ').grid(row=1, column=0, sticky=W)
    Label(janela, text="Média das alturas:%.2f m"%media_alturas, bg='white', fg='black', font='None 12 ').grid(row=2, column=0, sticky=W)
    Label(janela, text="Média dos pesos:%.2f kg"%media_pesos, font='None 12 ').grid(row=3, column=0, sticky=W)
    Label(janela, text="Média do IMC:%.2f"%media_imc, bg='white', fg='black', font='None 12 ').grid(row=4, column=0, sticky=W)

