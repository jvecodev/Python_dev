import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

dados = [12, 15, 16, 17, 18, 20, 21, 25, 26, 27, 30, 35]


# stat é o valor do teste, quanto mais proximo de 1 melhor
# pval é o valor p, se for maior que 0.05 aceita a hipótese nula
# Este é um teste de normalidade para verificar se os dados seguem uma distribuição normal
stat, pval = stats.shapiro(dados)

print(f"Teste de shapiro-Wilk, stat: {stat} ->  p-value: {pval}")