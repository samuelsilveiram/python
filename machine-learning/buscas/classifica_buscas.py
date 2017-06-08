from collections import Counter
import pandas as pd

data_frame = pd.read_csv('buscas.csv')
x_df = data_frame[['home','busca','logado']]
y_df = data_frame['comprou']

xdummies_df = pd.get_dummies(x_df)
ydummies_df = y_df

x = xdummies_df.values
y = ydummies_df.values


porcentagem_de_treino = 0.9

tamanho_de_treino = int(porcentagem_de_treino * len(x))
tamanho_de_teste = int(len(y) - tamanho_de_treino)

treino_dados = x[:tamanho_de_treino]
treino_marcacoes = y[:tamanho_de_treino]


teste_dados = x[-tamanho_de_teste:]
teste_marcacoes = y[-tamanho_de_teste:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()

modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)

acertos = (resultado == teste_marcacoes)

total_acertos = sum(acertos)
total_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_acertos / total_elementos

acerto_base = max(Counter(teste_marcacoes).itervalues())
taxa_de_acerto_base = 100.0 * acerto_base / len(teste_marcacoes)

print("Taxa de acerto base: %f" % taxa_de_acerto_base)
print("Taxa de acerto: %f" % taxa_de_acerto)
print(total_elementos)
