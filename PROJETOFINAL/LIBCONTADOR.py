from tkinter import *

def cadastro():
    def contador():
        arquivo = open("dados.txt", "a+")#abre arquivo dos dados
        cadastro = open("cadastro.txt", "a+")#abre arquivo dos num de cadastro
        nome=entrada1.get()#recebe oq foi escrito em entrada1
        idade=entrada2.get()#recebe entrada2
        peso=entrada3.get()#recebe entrada3
        altura=entrada4.get()#recebe entrada4
        celular=entrada5.get()#recebe entrada5
        objetivo=entrada6.get()#recebe entrada6
        listadados=[f'\n{nome}\n{idade}\n{peso}\n{altura}\n{celular}\n{objetivo}']#coloca oq foi escrito na lista
        arquivo.writelines(listadados)#escreve a lista no arquivo de dados(cada elemento, uma linha)
        arquivo.seek(0)#coloca poteiro no inicio do arquivo de dados
        linhas=arquivo.readlines()#lê todas as linhas do arquivo de dados e gera lista
        numc=len(linhas)#lê tamanho da lista e armazena em variavel
        cadastro.write(f'{numc}\n')#escreve essa variavel no arquivo de cadastro
        ncad=numc/6
        cad=Tk()
        cad.title('N° do cadastro')
        Label(cad, text=f'{ncad}',font='None 14 bold').pack()
        cad.pack()
        arquivo.close()
        cadastro.close()
    janela=Tk()
    janela.title('Cadastro')
    Button(janela, text="Cadastrar",width=22, bg='white', fg='black',command=contador, font='None 14 bold').grid(row=8, column=0,columnspan=3, sticky=W)
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

def consulta():
    def pegardados():
        def calculo_imc (peso, altura):
            imc = peso / (altura)**2
            return imc
        arquivo = open("dados.txt", "a+")#abre arquivo dos dados
        cadastro = open("cadastro.txt", "a+")#abre arquivo dos num de cadastro
        numc=(int(entrada4.get())*6)
        arquivo.seek(0)
        listadados=arquivo.readlines()#ler arquivo de dados e colocar em lista
        obj=listadados[numc-1]
        celular=listadados[numc-2]
        altura=float(listadados[numc-3])
        peso=float(listadados[numc-4])
        idade=int(listadados[numc-5])
        nome=listadados[numc-6]
        IMC=calculo_imc(peso, altura)
        Label(janela, text='Nome:', bg='white', fg='black', font='None 12 ').grid(row=4, column=0, sticky=W)
        Label(janela, text='%s'%nome, bg='white', fg='black', font='None 12 ').grid(row=5, column=0,columnspan=2, sticky=W)
        Label(janela, text='Idade:%d'%idade, bg='white', fg='black', font='None 12 ').grid(row=6, column=0, sticky=W)
        Label(janela, text='Peso:%.2f'%peso, bg='white', fg='black', font='None 12 ').grid(row=7, column=0, sticky=W)
        Label(janela, text='Altura:%.2f'%altura, bg='white', fg='black', font='None 12 ').grid(row=8, column=0, sticky=W)
        Label(janela, text='Telefone:%s'%celular, bg='white', fg='black', font='None 12 ').grid(row=10, column=0,columnspan=2, sticky=W)
        Label(janela, text='IMC:%.2f'% IMC, bg='white', fg='black', font='None 12 ').grid(row=9, column=0, sticky=W)
        Label(janela, text='Objetivo:  %s\n1:Hipertrofia\n2:Emagrecimento\n3:Potência'%obj).grid(row=11, column=0, sticky=W)
        
    janela=Tk()
    janela.title('Consulta')
    janela.configure(background="white")
    Label(janela, text="Consultar cadastro", bg='white', fg='black', font='None 14 bold').grid(row=1, column=0,columnspan=2, sticky=W)
    Label(janela, text="Insira N° de cadastro:", bg='white', fg='black', font='None 12 ').grid(row=2, column=0,columnspan=2, sticky=W)
        
    entrada4=Entry(janela, width=12, bg='white')
    entrada4.grid(row=3, column=0, sticky=W)
        
    Button(janela, text='Consultar', command=pegardados).grid(row=3, column=1, sticky=W)
def info():
    janela=Tk()
    janela.title('Informações')
    janela.configure(background="white")
    Label(janela, text="Informações dos cadastrados:", bg='white', fg='black', font='None 14 bold').grid(row=1, column=0, sticky=W)
    Label(janela, text="Média de altura:", bg='white', fg='black', font='None 12 ').grid(row=2, column=0, sticky=W)
    Label(janela, text="Média de peso:", bg='white', fg='black', font='None 12 ').grid(row=3, column=0, sticky=W)
    Label(janela, text="Média de IMC:", bg='white', fg='black', font='None 12 ').grid(row=4, column=0, sticky=W)
