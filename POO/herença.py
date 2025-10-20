"""
    subclasses
"""

from aula1classe import Game


# estamos herdando
class SinglePlayerGame(Game):
    """
        Nós podemos criar novos atributos especificos
        porem precisamos chamar o construtor
    """

    def __init__(self, name="", yearLaunch=0, note=0, storyLine = ""):
        # fazemos isso para reutilizar os valores dos atributos do Game
        super().__init__(name, yearLaunch, False, note)

        # Atributo específico da classe SinglePlayerGame
        self.storyLine = storyLine

    # Sobrescrevendo os metodos tbm 

    def print_info(self):
        super().print_info()
        # assim acrescentamos a informação referenta apenas a subclase
        print(f"historia do jogo é {self.storyLine}")

    
    