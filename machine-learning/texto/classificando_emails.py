#!-*- coding: utf8 -*-
## -- configuração de encoding somente no python2
# texto1 = "Se eu comprar cinco anos antecipados, eu ganho algum desconto?"
# texto2 = "O exercício 15 do curso de Java 1 está com a resposta errada. Pode Conferir pf?"
# texto3 = "Existe algum curso para cuidar do marketing da minha empresa?"

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.cross_validation import cross_val_score

classificacoes = pd.read_csv('emails.csv')

textos_puros = classificacoes['email']
textos_quebrados = textos_puros.str.lower().str.split(' ')

dicionario = set()
for lista in textos_quebrados: 
    dicionario.update(lista)

total_de_palavras = len(dicionario)

tuplas = zip(dicionario, xrange(total_de_palavras))

tradutor = {palavra:indice for palavra, indice in tuplas}

def vetorizar_texto(texto, tradutor):
    vetor = [0] * len(tradutor)

    for palavra in texto:
        if palavra in tradutor:
            posicao = tradutor[palavra]
            vetor[posicao] += 1
    
    return vetor

vetores_de_texto = [vetorizar_texto(texto, tradutor) for texto in textos_quebrados]

marcas = classificacoes['classificacao']

x = np.array(vetores_de_texto)
y = np.array(marcas.tolist())

porcentagem_de_treino = 0.8

tamanho_do_treino = int(porcentagem_de_treino * len(y))
tamanho_de_validacao = len(y) - tamanho_do_treino

treino_dados = x[0:tamanho_do_treino]
treino_marcacoes = y[0:tamanho_do_treino]

validacao_dados = x[tamanho_do_treino:]
validacao_marcacoes = y[tamanho_do_treino:]

def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes):
    k = 10
    scores = cross_val_score(modelo, treino_dados, treino_marcacoes, cv = k)
    taxa_de_acerto = np.mean(scores)
    msg = "Taxa de acerto do {0}: {1}".format(nome, taxa_de_acerto)
    print msg
    return taxa_de_acerto

resultados = {}

from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
modeloOneVersusRest = OneVsRestClassifier(LinearSVC(random_state=0))  ## Roda varias vezes o LinearSVC e define a probabilidade de classificacao quando a resposta nao e booleana
resultadoOneVersusRest = fit_and_predict("OneVersusRest", modeloOneVersusRest, treino_dados, treino_marcacoes)
resultados[resultadoOneVersusRest] = modeloOneVersusRest

from sklearn.multiclass import OneVsOneClassifier ## tomar cuidado com a performance, pois esse algoritmo compara todas as categorias com todas.
modeloOneVersusOne = OneVsOneClassifier(LinearSVC(random_state=0))
resultadoOneVersusOne = fit_and_predict("OneVersusOne", modeloOneVersusOne, treino_dados, treino_marcacoes)
resultados[resultadoOneVersusOne] = modeloOneVersusOne

from sklearn.naive_bayes import MultinomialNB
modeloMultinomialNB = MultinomialNB() ## Baseado em probabilidade
resultadoMultinomialNB = fit_and_predict("MultinomialNB", modeloMultinomialNB, treino_dados, treino_marcacoes)
resultados[resultadoMultinomialNB] = modeloMultinomialNB

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoostClassifier = AdaBoostClassifier() ## Baseado na capacidade de sempre melhorar o algoritmo
resultadoAdaBoostClassifier = fit_and_predict("AdaBoostClassifier", modeloAdaBoostClassifier, treino_dados, treino_marcacoes)
resultados[resultadoAdaBoostClassifier] = modeloAdaBoostClassifier

maximo = max(resultados)
vencedor = resultados[maximo]

print "vencedor: "
print vencedor

vencedor.fit(treino_dados, treino_marcacoes)
resultado = vencedor.predict(validacao_dados)
acertos = (resultado == validacao_marcacoes)
total_acertos = sum(acertos)
total_elementos = len(validacao_dados)
taxa_de_acerto = 100.0 * total_acertos / total_elementos

msg = "Taxa de acerto do vencedor no mundo real: {0}".format(taxa_de_acerto)
print(msg)


acerto_base = max(Counter(validacao_marcacoes).itervalues())
taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_marcacoes)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)
print("Total de testes: %d" % len(validacao_dados))