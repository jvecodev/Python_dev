from aula1classe import Game 
from herença import SinglePlayerGame

game1 = Game()

# Aqui ele trara um objeto da classe Game
# O local da memoria também virá


"""
    Abordagem sem construtores
"""

game1.name = "Zelda"
game1.yearLaunch = 1986 
game1.multiplayer = True
game1.note = 10


game2  = Game()
print(game2)



game2.name = "GTA"
game2.yearLaunch = 2000
game2.multiplayer = True
game2.note = 10

print(game1)
print(game2)


"""
    Nova abordagem com construtores
"""

game1 = Game("Forza Horizon", 2012, True, 9)
game2 = Game("Fifa", 1993, True, 8)

print(game1)
print(game2)

outroGame = Game("fortnite", 2017, True, 9)
outroGame.print_info()
 # Aqui nos temos o atributo especifico de da classe SinglePlayerGame
game_heranca = SinglePlayerGame("The Last of Us", 2013, 10, "Pós apocalipse")
game_heranca.print_info()

