
"""
Docstring para Machine_Learnings.Recomendation.Dados_Recomendacao - Livro.groupby
Agora vamos trabalhar com o método groupby do pandas.
"""



import pandas as pd  # trabalhar com dados
import numpy as np  # operações matemáticas/matrizes
import matplotlib.pyplot as plt  # visualização de dados
import seaborn as sns  # visualização de dados
import plotly.express as px  # visualização interativa
import warnings
from describe import renomear_colunas
warnings.filterwarnings('ignore')


dados_livros = pd.read_csv('Books.csv')
dados_avaliacao = pd.read_csv('Ratings.csv')
dados_usuarios = pd.read_csv('Users.csv')

Tab_cruzada = dados_livros.merge(dados_avaliacao, how='inner', on='ISBN')
Tab_cruzada = Tab_cruzada.merge(dados_usuarios, how='inner', on='User-ID')


"""
Analise
"""

renomear_colunas(Tab_cruzada)

Analise = Tab_cruzada.groupby(by=['Título do Livro']).agg(
    Quantidade = ('Título do Livro', 'count'),
    Media = ('Avaliacao', 'mean'),
    Max = ('Avaliacao', 'max'),
    Min = ('Avaliacao', 'min'),
    Mediana = ('Avaliacao', 'median')
)

# print(Analise.head())


Analise = Analise.sort_values('Quantidade', ascending=False)

print(Analise.head())