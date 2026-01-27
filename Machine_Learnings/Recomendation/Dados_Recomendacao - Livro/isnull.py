
"""

Now, we go to treat numbers

Finished modelize step

"""



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

Tab_cruzada = dados_livros.merge(dados_avaliacao, how='inner', on='ISBN')
Tab_cruzada = Tab_cruzada.merge(dados_usuarios, how ='inner', on='User-ID')


# Number of null values in each column
print(Tab_cruzada.isnull().sum())


# Number unique values in each column

print(Tab_cruzada.nunique())


