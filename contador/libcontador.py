def contador():
    arquivo = open("conta.txt", "a+")#abre arquivo
    arquivo.seek(0)#coloca poteiro no inicio da lista
    linhas=arquivo.readlines()#lê arquivo e coloca linhas na lista
    numc=len(linhas)#lê tamanho da lista e armazena em variavel
    arquivo.write(f'{numc}\n')#acrescenta ess
    arquivo.close()

