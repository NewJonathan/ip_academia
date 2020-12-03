from tkinter import *
from LIBCONTADOR import *
janela=Tk()
janela.title('Academia')
janela.configure(background="white")

Button(janela, text="LOGO DA ACADEMIA",width=22, bg='white', fg='black', font='None 14 bold').grid(row=1, column=0,columnspan=3, sticky=W)
Button(janela, text="Informações",width=9, bg='white', fg='black', font='None 12 ').grid(row=2, column=0, sticky=W)
Button(janela, text="Cadastro",width=9, bg='white', fg='black',command=cadastro, font='None 12 ').grid(row=2, column=1, sticky=W)
Button(janela, text="Consulta",width=9, bg='white', fg='black', font='None 12 ').grid(row=2, column=2, sticky=W)
