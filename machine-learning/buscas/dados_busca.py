import csv

def carregar_buscas():

    x = [] 
    y = []

    arquivo = open('buscas.csv', 'rb')
    leitor = csv.reader(arquivo)
    leitor.next()

    for home,busca,logado,comprou in leitor:

        dados = [int(home), busca, int(logado)]
        x.append(dados)
        y.append(int(comprou))

    return x, y