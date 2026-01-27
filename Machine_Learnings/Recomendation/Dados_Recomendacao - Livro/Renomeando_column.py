
"""

NRename each column to Portuguese

"""


import pandas as pd  # trabalhar com dados
import numpy as np  # operações matemáticas/matrizes
import matplotlib.pyplot as plt  # visualização de dados
import seaborn as sns  # visualização de dados
import plotly.express as px  # visualização interativa
import warnings
warnings.filterwarnings('ignore')


dados_livros = pd.read_csv('Books.csv')
dados_avaliacao = pd.read_csv('Ratings.csv')
dados_usuarios = pd.read_csv('Users.csv')

Tab_cruzada = dados_livros.merge(dados_avaliacao, how='inner', on='ISBN')
Tab_cruzada = Tab_cruzada.merge(dados_usuarios, how='inner', on='User-ID')


Tab_cruzada.rename(
    columns={
        'Location': 'Localização',
        'Publisher': 'Editora',
        'Book-Title': 'Título do Livro',
        'Book-Author': 'Autor do Livro',
        'Year-Of-Publication': 'Ano de Publicação',
        'ISBN': 'ISBN',
        'User-ID': 'ID do Usuário',
        'Book-Rating': 'Avaliação do Livro',
        'Age': 'Idade',

    }, inplace=True  # work to modify the original DataFrame
)

print(Tab_cruzada.columns)
