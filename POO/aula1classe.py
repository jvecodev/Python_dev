"""
    Uma superclasse
"""

class Game:
    # Atributos da classe
    """
        Self, para fazer referência ao objeto atual
        Construtor
    """
    def __init__(self, name = "", yearLaunch = 0, multiplayer = False, note = 0):
        self._name = name
        self.yearLaunch = yearLaunch
        self._multiplayer = multiplayer
        self.note = note
        self.avaliacao = 0
        self.avaliador = 0

    """
        Fazemos isso para não precisar printar o objeto juntamente 
        com o atributo ao lado    

        Se não fizesse isso, retornaria o local na memoria que fica 
        armazenado

    """

    def __str__(self):
        return f"Game: {self._name}, Year Launch: {self.yearLaunch},\
        Multiplayer: {self.multiplayer}, Note: {self.note}"

    """
        Métodos de instância
    """

    def print_info(self):
        # Self.name -> atributo da classe
        print("="*20)
        print(f"nome do jogo é {self._name}")
        print(f"ano de lançamento é {self.yearLaunch}")
        print(f"multiplayer é {self.multiplayer}")
        print(f"nota é {self.note}")
        print("="*20)


    def evaluate(self, note):
        self.avaliacao += note
        self.avaliador += 1

    def average(self):
        print(f"nome {self.name} - media {self.avaliacao / self.avaliador}")