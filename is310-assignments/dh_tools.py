import pandas as pd

df = pd.read_csv('tools_dh_proceedings.csv')

df['sum'] = df.sum(axis=1)
for i, row in df.iterrows():
    print(row['Tool'],': 2015:', row['2015'], ', 2019:', row['2019'], ', sum:', row['sum'])

def dataTools(data, name):
    data['sum'] = data.sum(axis=1)
    print(data.loc[data['Tool'] == name])

