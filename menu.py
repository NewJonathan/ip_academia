from tkinter import *
from acad import *
janela=Tk()
janela.title('Academia')
janela.configure(background="white")

#imagem de fundo
'''
img=PhotoImage(file='.gif')
Label(janela, image=img, bg='white').grid(row=0, column=0, sticky=W)
'''

Button(janela, text="LOGO DA ACADEMIA",width=22, bg='white', fg='black', font='None 14 bold').grid(row=1, column=0,columnspan=3, sticky=W)
Button(janela, text="Informações",width=9, bg='white', fg='black',command=info, font='None 12 ').grid(row=2, column=0, sticky=W)
Button(janela, text="Cadastro",width=9, bg='white', fg='black',command=cadastro, font='None 12 ').grid(row=2, column=1, sticky=W)
Button(janela, text="Consulta",width=9, bg='white', fg='black',command=consulta, font='None 12 ').grid(row=2, column=2, sticky=W)
