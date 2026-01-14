import pandas as pd #trabalhar com dados
import numpy as np #operações matemáticas/matrizes
import matplotlib.pyplot as plt #visualização de dados
import seaborn as sns #visualização de dados
import plotly.express as px #visualização interativa
import warnings
warnings.filterwarnings('ignore')


# Ajustes do pandas

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)

# Ajustes no matplotlib
# Tamanho do grafico
plt.rcParams['figure.figsize'] = (15, 6)
plt.style.use('dark_background') # estilo do grafico


# Ler os dados 

dados_livros = pd.read_csv('Books.csv')
dados_avaliacao = pd.read_csv('Ratings.csv')
dados_usuarios = pd.read_csv('Users.csv')

# Dimensões dos dados

# print("Dimensões dos dados:")

# .shape retorna uma tupla com o número de linhas e colunas
# print(f"Avaliações: {dados_avaliacao.shape}")
# print(f"Livros: {dados_livres.shape}")
# print(f"Usuários: {dados_usuarios.shape}")

# comando .head() exibe as primeiras linhas do DataFrame
# print("\nPrimeiras linhas dos dados de Avaliações:")
# print(dados_avaliacao.head())
# print("\nPrimeiras linhas dos dados de Livros:")
# print(dados_livros.head())


# comando info() exibe informações sobre o DataFrame
# print("\nInformações dos dados de Livros:")
# print(dados_livros.info())
# print("\nInformações dos dados de Avaliações:")
# print(dados_avaliacao.info())

# Verificando dados do user

print(dados_livros.head())
print(dados_avaliacao.head())