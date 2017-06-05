import csv

def carregar_acessos():

    x = [] 
    y = []

    arquivo = open('acesso_pagina.csv', 'rb')
    leitor = csv.reader(arquivo)

    leitor.next()

    for home,como_funciona,contato,comprou in leitor:

        dados = [int(home), int(como_funciona), int(contato)]
       
        x.append(dados)

        y.append(int(comprou))

    return x, y