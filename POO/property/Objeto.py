
from Conta import Conta

c = Conta(100)
print(c.saldo)   # chama o getter (parece público, mas é privado controlado)
c.saldo = 200    # chama o setter
c.saldo = -50    # levanta exceção
