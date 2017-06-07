import pandas as pd

data_frame = pd.read_csv('buscas.csv')
x_df = data_frame[['home','busca','logado']]
y_df = data_frame['comprou']

xdummies_df = pd.get_dummies(x_df)
ydummies_df = y_df

x = xdummies_df.values
y = ydummies_df.values

print(x)
print(y)
