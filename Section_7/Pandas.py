import pandas as pd
import numpy as np


# Faz a leitura do arquivo CSV
dados = pd.read_csv("Credit.csv")

# Mostra a quantidade de dados lidos do arquivo
#print(dados.shape)

# Mostra os dados da tabela
#print(dados.describe())

# Mostra os 3 primeiros registros
#print(dados.head(3))

# Mostra os 2 últimos registros
#print(dados.tail(2))

# Mostra os dados somente da coluna especificada
#print(dados[["duration"]])

# Mostra os dados das linhas 1 a 3
#print(dados.loc[1:3])

# Mostra os dados das linhas 1 e 3 (É possível passar uma lista de n valores e serão obtidos os valores das linhas correspondentes)
#print(dados.loc[[1,3]])

# Aplica um filtro e mostra somente as linhas onde a coluna 'purpose' é igual a radio/tv
#print(dados.loc[dados['purpose'] == "radio/tv"])

# Aplica um filtro e mostra somente as linhas onde a coluna 'credit_amount' é maior de 18000
#print(dados.loc[dados['credit_amount'] > 18000])

# Podemos aplicar filtros e gerar uma tabela filtrados a outra variável
#dados_filtrados = dados[['checking_status','duration']].loc[dados['credit_amount'] > 18000]
#print(dados_filtrados)

'''
    Séries
    
    Pode ser criado a partir de uma lista, um array do numpy ou uma coluna de uma tabela (data frame)
'''

# Criando uma série a partir de uma lista
s1 = pd.Series([2,5,3,34,54,23,1,16])
#print(s1)

# Criando uma série a partir de um array do numpy
array1 = np.array([2,5,3,34,54,23,1,16])
s2 = pd.Series(array1)
#print(s2)

# Criando uma série a partir de uma coluna do data frame
s3 = dados['purpose']
#print(s3)
#print(type(s3))

# O código acima gera uma variável do tipo pandas.core.series.Series
# Que é diferente do comando abaixo, que gera um pandas.core.frame.DataFrame
dados2 = dados[['purpose']]
#print(dados2)
#print(type(dados2))

# É possível renomear as colunas de um data frame de duas formas
# 1- Atribuir o dataframe renomeado a variável novamente
#dados = dados.rename(columns={'duration':'duração','purpose':'propósito'})
# 2 - Passar o parâmetro inplace=True. O parâmetro inplace é usado em várias funções para indicar quando as mudanças devem ser aplicadas de fato
dados.rename(columns={'duration':'duração','purpose':'propósito'}, inplace=True)
#print(dados.columns)

# Excluir uma coluna
dados.drop('checking_status',axis=1,inplace=True)
#print(dados.columns)

# Verificar se existem dados nulos
# 1 - Mostra uma tabela no mesmo formato do dataframe, com True ou False nas linhas. Indicando se naquela posição existe um valor nulo
#print(dados.isnull())
# 2 - Mostra a quantidade de linhas com valores nulos em cada coluna
#print(dados.isnull().sum())

# Remove as linhas com NaN
#print(dados.dropna())

# É feito o preenchimento de todas as linhas vazias com o valor 0 na coluna duração
dados['duração'] = dados['duração'].fillna(0)
#print(dados['duração'])

# Podemos vizualizar somente algumas linhas e colunas do dataframe com iloc
# 1 - Abaixo são mostradas as linhas de 0 a 3 e as colunas de 0 a 5
#print(dados.iloc[0:3,0:5])
# 2 - Podemos especificar as linhas e colunas usando listas
#print(dados.iloc[[0,1,4,5,6,7],[4,5,6]])
