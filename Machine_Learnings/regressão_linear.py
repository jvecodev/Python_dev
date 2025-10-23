from numpy import *

class LinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__corelation_coefficient = self.__correlacao()
        self.__inclination = self.__inclinacao()
        self.__intercept  = self.__interceptacao()


    def __correlacao(self):
        """
            Calcula o coeficiente de correlação de Pearson
            cov = covariancia
            var = variancia
        """
        covariacao = cov(self.x, self.y, bias=True) [0][1]
        variancia_x = var(self.x)
        variancia_y = var(self.y)

        """
            Correlação
            
        """
        return covariacao / sqrt(variancia_x * variancia_y)
    
    def __inclinacao(self):

        """
            std = desvio padrão
        """
        m = self.__corelation_coefficient * (std(self.y) / std(self.x))
        return m
        
    def __interceptacao(self):

        """
            mean = media
            b = intercepto
        """

        b = mean(self.y) - self.__inclination * mean(self.x)
        return b

    def previsao(self, valor):
            
        return f"valor previsto corretamente {self.__intercept + (self.__inclination * valor)}"
    
x = array([1,2,3,4,5])
y = array([2,4,6,8,10])

objeto1  = LinearRegression(x,y)

prever = objeto1.previsao(6)
print(prever)


"""
    Aqui nos inplmentamos um modelo de regressão linear
    Prevemos um valor y quando o x for 6 
    Ou seja o y sera igual a 12
"""