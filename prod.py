# entendendo o desafio e a empresa
# importação da base de dados
# usar modelo em um cenário real
import pandas as pd
from sklearn.preprocessing import LabelEncoder
tabela = pd.read_csv("clientes.csv")
print(tabela)
# print(tabela.info())