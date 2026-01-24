"""

Arrumando localização de arquivos

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

