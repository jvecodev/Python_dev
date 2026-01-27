"""

Arrumando localização de arquivos
Na tentaviva de trazer apenas o país
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


# print(Tab_cruzada['Location'].head())

# Técnica de tratamento de textos



def Extrair_Pais( Regiao):
    """
    Docstring para Extrair_Pais
    
    :param Regiao: Descrição
    """

    Registro  = Regiao.split(',')  # Dividir a string em partes usando a vírgula como separador
    Pais = Registro[-1].upper().strip()  # Pega a última parte e remove espaços em branco

    return Pais

# apply, eu aplico uma funcao a uma coluna.
# é um metodo do pandas.
# Just show the location column
Tab_cruzada['Location'].apply(Extrair_Pais)

print(Tab_cruzada.head())

