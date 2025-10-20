"""
    Métodos de instancia

"""

from aula1classe import Game


game1 = Game("Zelda", 1986, True, 10)
game2 = Game("GTA", 2000, True, 10)


game1.print_info()
game2.print_info()


game1.evaluate(8)
game1.evaluate(10)

game2.evaluate(7)
game2.evaluate(9)

game1.average()
game2.average()

