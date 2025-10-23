import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

dados = [12, 15, 16, 17, 18, 20, 21, 25, 26, 27, 30, 35]

# o hist cria histograma

plt.hist(dados, bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Idades')
plt.ylabel('Frequência')
plt.title('Distribuição de Idades')
plt.show()



# Cria o QQ plot diagrama de normalidade
stats.probplot(dados, dist="norm", plot=plt)

# Título
plt.title("Q–Q Plot (Normalidade)")
plt.show()