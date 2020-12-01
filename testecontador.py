from tkinter import *
from acad import *
def contador():
    print()
janela=Tk()
janela.title('Academia')
Button(janela, text="SOMAR CONTADOR",width=22, bg='white', fg='black',command=contador, font='None 14 bold').grid(row=1, column=0,columnspan=3, sticky=W)

