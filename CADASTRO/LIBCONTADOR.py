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
