from tkinter import *

def click():#recebe os dados e envia para aquivo
    nome=entrada1.get()
    altura=entrada2.get()
    peso=entrada3.get()
def click2():#consulta dados gravados, armazena em variaveis, exibe essas variaveis
    nome='a'
    altura='b'
    peso='c'
    Label(janela, text=nome, bg='black', fg='white', font='None 12 bold').grid(row=10, column=1, sticky=W)
    Label(janela, text=altura, bg='black', fg='white', font='None 12 bold').grid(row=11, column=1, sticky=W)
    Label(janela, text=peso, bg='black', fg='white', font='None 12 bold').grid(row=12, column=1, sticky=W)
#main:
janela=Tk()
janela.title('Academia')
janela.configure(background="black")

'''
#imagem de fundo
img=PhotoImage(file='.gif')
Label(janela, image=img, bg='black').grid(row=0, column=0, sticky=W)
'''

#labels
Label(janela, text="Cadastro:", bg='black', fg='white', font='None 12 bold').grid(row=1, column=0, sticky=W)
Label(janela, text="Nome:", bg='black', fg='white', font='None 12 bold').grid(row=2, column=0, sticky=W)
Label(janela, text="Altura", bg='black', fg='white', font='None 12 bold').grid(row=3, column=0, sticky=W)
Label(janela, text="Peso", bg='black', fg='white', font='None 12 bold').grid(row=4, column=0, sticky=W)
Label(janela, text="Consultar cadastro", bg='black', fg='white', font='None 12 bold').grid(row=6, column=0,columnspan=2, sticky=W)
Label(janela, text="Insira N° de cadastro:", bg='black', fg='white', font='None 12 bold').grid(row=7, column=0,columnspan=2, sticky=W)
Label(janela, text="N° de cadastro: exibe num de cadastro", bg='black', fg='white', font='None 12 bold').grid(row=5, column=1,columnspan=2, sticky=W)
Label(janela, text="Nome:", bg='black', fg='white', font='None 12 bold').grid(row=10, column=0, sticky=W)
Label(janela, text="Peso:", bg='black', fg='white', font='None 12 bold').grid(row=11, column=0, sticky=W)
Label(janela, text="Altura:", bg='black', fg='white', font='None 12 bold').grid(row=12, column=0, sticky=W)
Label(janela, text="IMC:", bg='black', fg='white', font='None 12 bold').grid(row=13, column=0, sticky=W)

#entradas de texto
entrada1=Entry(janela, width=75, bg='white')
entrada1.grid(row=2, column=1, sticky=W)

entrada2=Entry(janela, width=75, bg='white')
entrada2.grid(row=3, column=1, sticky=W)

entrada3=Entry(janela, width=75, bg='white')
entrada3.grid(row=4, column=1, sticky=W)

entrada4=Entry(janela, width=12, bg='white')
entrada4.grid(row=8, column=0,columnspan=2, sticky=W)

#botões
Button(janela, text='Cadastrar',width=7, command=click).grid(row=5, column=0, sticky=W)
Button(janela, text='Consultar',width=7, command=click2).grid(row=8, column=1, sticky=W)







janela.mainloop()
