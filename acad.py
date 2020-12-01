from tkinter import *
def info():
    janela=Tk()
    janela.title('Informações')
    janela.configure(background="white")
    #imagem de fundo
    '''
    img=PhotoImage(file='.gif')
    Label(janela, image=img, bg='white').grid(row=0, column=0, sticky=W)
    '''
    Label(janela, text="Informações dos cadastrados:", bg='white', fg='black', font='None 14 bold').grid(row=1, column=0, sticky=W)
    Label(janela, text="Média de altura:", bg='white', fg='black', font='None 12 ').grid(row=2, column=0, sticky=W)
    Label(janela, text="Média de peso:", bg='white', fg='black', font='None 12 ').grid(row=3, column=0, sticky=W)
    Label(janela, text="Média de IMC:", bg='white', fg='black', font='None 12 ').grid(row=4, column=0, sticky=W)
def cadastro():
    janela=Tk()
    janela.title('Cadastro')
    janela.configure(background="white")
    Label(janela, text="Cadastro:", bg='white', fg='black', font='None 14 bold').grid(row=1, column=0, sticky=W)
    Label(janela, text="Nome:", bg='white', fg='black', font='None 12 ').grid(row=2, column=0, sticky=W)
    Label(janela, text="Idade:", bg='white', fg='black', font='None 12 ').grid(row=3, column=0, sticky=W)
    Label(janela, text="Altura:", bg='white', fg='black', font='None 12 ').grid(row=4, column=0, sticky=W)
    Label(janela, text="Peso:", bg='white', fg='black', font='None 12 ').grid(row=5, column=0, sticky=W)
    Label(janela, text="Telefone:", bg='white', fg='black', font='None 12 ').grid(row=6, column=0, sticky=W)
    entrada1=Entry(janela, width=70, bg='white')
    entrada1.grid(row=2, column=1, sticky=W)

    entrada2=Entry(janela, width=12, bg='white')
    entrada2.grid(row=3, column=1, sticky=W)
    
    entrada3=Entry(janela, width=12, bg='white')
    entrada3.grid(row=4, column=1, sticky=W)

    entrada4=Entry(janela, width=12, bg='white')
    entrada4.grid(row=5, column=1, sticky=W)

    entrada5=Entry(janela, width=12, bg='white')
    entrada5.grid(row=6, column=1, sticky=W)
    
    Button(janela, text='Cadastrar').grid(row=7, column=0, sticky=W)
def consulta():
    janela=Tk()
    janela.title('Consulta')
    janela.configure(background="white")
    Label(janela, text="Consultar cadastro", bg='white', fg='black', font='None 14 bold').grid(row=1, column=0,columnspan=2, sticky=W)
    Label(janela, text="Insira N° de cadastro:", bg='white', fg='black', font='None 12 ').grid(row=2, column=0,columnspan=2, sticky=W)
    Label(janela, text="Nome:", bg='white', fg='black', font='None 12 ').grid(row=4, column=0, sticky=W)
    Label(janela, text="Idade:", bg='white', fg='black', font='None 12 ').grid(row=5, column=0, sticky=W)
    Label(janela, text="Peso:", bg='white', fg='black', font='None 12 ').grid(row=6, column=0, sticky=W)
    Label(janela, text="Altura:", bg='white', fg='black', font='None 12 ').grid(row=7, column=0, sticky=W)
    Label(janela, text="Telefone:", bg='white', fg='black', font='None 12 ').grid(row=8, column=0, sticky=W)
    
    entrada4=Entry(janela, width=12, bg='white')
    entrada4.grid(row=3, column=0, sticky=W)
    
    Button(janela, text='Consultar').grid(row=3, column=1, sticky=W)
