from collections import Counter
import pandas as pd

data_frame = pd.read_csv('buscas2.csv')
x_df = data_frame[['home','busca','logado']]
y_df = data_frame['comprou']

xdummies_df = pd.get_dummies(x_df)
ydummies_df = y_df

x = xdummies_df.values
y = ydummies_df.values


porcentagem_de_treino = 0.8
porcentagem_de_teste = 0.1

tamanho_de_treino = int(porcentagem_de_treino * len(y))
tamanho_de_teste = int(porcentagem_de_teste * len(y))
tamanho_de_validacao = int(len(y) - tamanho_de_treino - tamanho_de_teste)

treino_dados = x[0:tamanho_de_treino]
treino_marcacoes = y[0:tamanho_de_treino]

fim_de_teste = (tamanho_de_treino+tamanho_de_teste)
teste_dados = x[tamanho_de_treino:fim_de_teste]
teste_marcacoes = y[tamanho_de_treino:fim_de_teste]

validacao_dados = x[fim_de_teste:]
validacao_marcacoes = y[fim_de_teste:]

def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
    modelo.fit(treino_dados, treino_marcacoes)

    resultado = modelo.predict(teste_dados)

    acertos = (resultado == teste_marcacoes)

    total_acertos = sum(acertos)
    total_elementos = len(teste_dados)

    taxa_de_acerto = 100.0 * total_acertos / total_elementos

    msg = "Taxa de acerto do {0}: {1}".format(nome, taxa_de_acerto)
    print(msg)
    return taxa_de_acerto

from sklearn.naive_bayes import MultinomialNB
modeloMultinomialNB = MultinomialNB() ## Baseado em probabilidade
resultadoMultinomialNB = fit_and_predict("MultinomialNB", modeloMultinomialNB, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoostClassifier = AdaBoostClassifier() ## Baseado na capacidade de sempre melhorar o algoritmo
resultadoAdaBoostClassifier = fit_and_predict("AdaBoostClassifier", modeloAdaBoostClassifier, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

if resultadoMultinomialNB > resultadoAdaBoostClassifier:
    vencedor = modeloMultinomialNB
else:
    vencedor = modeloAdaBoostClassifier

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

