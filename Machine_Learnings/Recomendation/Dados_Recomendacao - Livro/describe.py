
"""

Now, we go to explorer, with data visualization and statistics

"""


import pandas as pd  # trabalhar com dados
import numpy as np  # operações matemáticas/matrizes
import matplotlib.pyplot as plt  # visualização de dados
import seaborn as sns  # visualização de dados
import plotly.express as px  # visualização interativa
import warnings
warnings.filterwarnings('ignore')


def renomear_colunas(minha_tabela):


    minha_tabela.rename(
        columns={
            'Location': 'Localização',
            'Publisher': 'Editora',
            'Book-Title': 'Título do Livro',
            'Book-Author': 'Autor do Livro',
            'Year-Of-Publication': 'Ano',
            'ISBN': 'ISBN',
            'User-ID': 'ID_cliente',
            'Book-Rating': 'Avaliacao',
            'Age': 'Idade',
            

        }, inplace=True  # work to modify the original DataFrame
    )

def main():

    """Função principal que executa a análise descritiva"""
    
    dados_livros = pd.read_csv('Books.csv')
    dados_avaliacao = pd.read_csv('Ratings.csv')
    dados_usuarios = pd.read_csv('Users.csv')

    Tab_cruzada = dados_livros.merge(dados_avaliacao, how='inner', on='ISBN')
    Tab_cruzada = Tab_cruzada.merge(dados_usuarios, how='inner', on='User-ID')
    
    renomear_colunas(Tab_cruzada)

    # é um metodo do pandas que gera estatísticas descritivas que resumem a tendência central,
    print(Tab_cruzada.describe())

    """
    count  1.031136e+06  1.031136e+06  753301.000000 -> Contagem
    mean   1.405945e+05  2.839051e+00      37.397648 -> Média
    std    8.052466e+04  3.854157e+00      14.098254 -> Desvio padrão
    min    2.000000e+00  0.000000e+00       0.000000 -> Valor mínimo
    25%    7.041500e+04  0.000000e+00      28.000000 -> 1º Quartil
    50%    1.412100e+05  0.000000e+00      35.000000 -> Mediana
    75%    2.114260e+05  7.000000e+00      45.000000 -> 3º Quartil
    max    2.788540e+05  1.000000e+01     244.000000 -> Valor máximo
    """

    print("\n\nApós remover as avaliações zeradas:\n")

    # Remover avaliações zeradas
    Tab_cruzada = Tab_cruzada.loc[Tab_cruzada['Avaliacao'] > 0]

    print(Tab_cruzada.describe())

    # analise grafica
    plt.title('Analisando das Avaliações dos Livros')
    sns.boxplot( data=Tab_cruzada, x='Avaliacao')

    plt.show()


if __name__ == "__main__":
    main()
