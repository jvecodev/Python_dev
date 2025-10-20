class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo   # privado

    @property  
    def saldo(self): 
        """Getter - acesso controlado"""
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        """Setter - só aceita valores positivos"""
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self.__saldo = valor
