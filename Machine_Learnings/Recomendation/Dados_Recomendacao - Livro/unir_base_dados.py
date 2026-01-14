# Vamos unir as bases de dados para criar um sistema de recomendação de livros.

import pandas as pd #trabalhar com dados
import numpy as np #operações matemáticas/matrizes
import matplotlib.pyplot as plt #visualização de dados
import seaborn as sns #visualização de dados
import plotly.express as px #visualização interativa
import warnings
warnings.filterwarnings('ignore')


dados_livros = pd.read_csv('Books.csv')
dados_avaliacao = pd.read_csv('Ratings.csv')
dados_usuarios = pd.read_csv('Users.csv')

"""
inner é o nosso inner join do sql, ou o lookup no mongodb.
"""



Tab_cruzada = dados_livros.merge(dados_avaliacao, how='inner', on='ISBN')
Tab_cruzada = Tab_cruzada.merge(dados_usuarios, how ='inner', on='User-ID')


print("Dimensões da Tabela Cruzada (Livros + Avaliações):")

print(Tab_cruzada.shape)
print(Tab_cruzada.head())


